#!/usr/bin/env python3
"""Generate Submission/Gen19/ Lean modules from snaky19.cards.txt (snaky-cards-txt-v1).

Mirrors the Gen17 layout (tools/cards2lean.py pattern):
  DataNN.lean   -- `def c<i> : Card := ...` literals, ~435 cards per file
  Tree.lean     -- block subtrees tK, the composed `tree`, and `getK := tree.get`
  ChunkNNN.lean -- `tK_ok : tK.all (cardOK getK) = true := by decide +kernel`
  split cards (>200 replies) get Head + R-part files + a `cardOK_of_split` aggregate
  All.lean      -- `tree_ok` composed with CTree.all_node / CTree.all_leaf

Before emitting, every card is checked against a Python replica of `cardOK`, so a
malformed certificate fails here instead of in the kernel.

Usage: python3 tools/gen19.py [cards.txt] [out_dir]
"""
import os
import sys

ORIENT = [(1, 0, 0, 1), (-1, 0, 0, 1), (0, -1, 1, 0), (0, 1, 1, 0),
          (-1, 0, 0, -1), (1, 0, 0, -1), (0, 1, -1, 0), (0, -1, -1, 0)]
SNACKY = [(0, 0), (1, 0), (2, 0), (3, 0), (3, 1), (4, 1)]

MAX_CARDS_PER_BLOCK = 60      # Gen17 chunk sizing
HEAVY_REPLIES = 120           # >120 replies: own chunk
SPLIT_REPLIES = 200           # >200 replies: cardOK_of_split parts
PART_SIZE = 15                # replies per split part (Gen17: 223->15, 250->17)
DATA_CARDS_PER_FILE = 434     # 3469 cards -> 8 Data files


# ---------------------------------------------------------------- parse

def parse(path):
    with open(path) as f:
        toks = f.read().split()
    assert toks[0] == 'snaky-cards-txt-v1', toks[0]
    ints = [int(t) for t in toks[1:]]
    i = 0

    def take(n):
        nonlocal i
        v = ints[i:i + n]
        i += n
        return v

    rows, cols, root, k, dx, dy = take(6)
    cards = []
    while i < len(ints):
        h, px, py, na = take(4)
        A = [tuple(take(2)) for _ in range(na)]
        ns, = take(1)
        S = [tuple(take(2)) for _ in range(ns)]
        j, = take(1)
        pass_h = None if j < 0 else (j,) + tuple(take(3))
        nr, = take(1)
        replies = []
        for _ in range(nr):
            w = tuple(take(2))
            replies.append((w, (take(1)[0],) + tuple(take(3))))
        cards.append({'h': h, 'p': (px, py), 'A': A, 'S': S,
                      'pass': pass_h, 'replies': replies})
    assert i == len(ints)
    return rows, cols, root, (k, dx, dy), cards


# ------------------------------------------------- Python replica of cardOK

def app(g, q):
    (k, dx, dy) = g
    a, b, c, d = ORIENT[k]
    return (a * q[0] + b * q[1] + dx, c * q[0] + d * q[1] + dy)


def _norm(s):
    mx = min(p[0] for p in s)
    my = min(p[1] for p in s)
    return [(p[0] - mx, p[1] - my) for p in s]


def _orientations(s):
    def rot(p): return (-p[1], p[0])
    def refl(p): return (p[0], -p[1])
    def mp(f): return [f(p) for p in s]
    out = [s, [rot(p) for p in s],
           [rot(rot(p)) for p in s], [rot(rot(rot(p))) for p in s],
           [refl(p) for p in s], [rot(refl(p)) for p in s],
           [rot(rot(refl(p))) for p in s], [rot(rot(rot(refl(p)))) for p in s]]
    return [_norm(o) for o in out]


ORIENTED = _orientations(SNACKY)  # f.head varies per orientation (normalize)


def won_plane(B):
    B = set(B)
    for f in ORIENTED:
        fh = f[0]
        for q in B:
            t = (q[0] - fh[0], q[1] - fh[1])
            if all((u[0] + t[0], u[1] + t[1]) in B for u in f):
                return True
    return False


def hint_ok(cards, h, B, R, hint):
    j, k, dx, dy = hint
    g = (k, dx, dy)
    if j >= len(cards):
        return False
    c2 = cards[j]
    if not c2['h'] < h:
        return False
    if not all(app(g, a) in B for a in c2['A']):
        return False
    return all(R(app(g, s)) for s in c2['S'])


def card_ok(cards, c):
    if not (1 <= c['h']):
        return False
    if c['p'] not in c['S']:
        return False
    B = set([c['p']]) | set(c['A'])
    if won_plane([c['p']] + c['A']):
        return True
    if c['pass'] is None:
        return False
    S = set(c['S'])
    if not hint_ok(cards, c['h'], B, lambda s: s in S, c['pass']):
        return False
    rmap = {}
    for w, h in c['replies']:
        rmap.setdefault(w, h)  # Lean List.lookup: first occurrence wins
    for w in c['S']:
        if w in B:
            continue
        hint = rmap.get(w)
        if hint is None:
            return False
        if not hint_ok(cards, c['h'], B, lambda s, w=w: s in S and s != w, hint):
            return False
    return True


# ---------------------------------------------------------------- rendering

def i2s(n):
    return '(%d)' % n if n < 0 else '%d' % n


def pt(p):
    return '(%s, %s)' % (i2s(p[0]), i2s(p[1]))


def hint(h):
    j, k, dx, dy = h
    a, b, c, d = ORIENT[k]
    return '(%d, ⟨%s, %s, %s, %s, %s, %s⟩)' % (
        j, i2s(a), i2s(b), i2s(c), i2s(d), i2s(dx), i2s(dy))


def pts(lst):
    return '[' + ', '.join(pt(p) for p in lst) + ']'


def card_def(i, c):
    pass_s = 'none' if c['pass'] is None else 'some ' + hint(c['pass'])
    rep = ', '.join('(%s, %s)' % (pt(w), hint(h)) for w, h in c['replies'])
    return ('def c%d : Card := { A := %s, S := %s, p := %s, h := %d, '
            'pass := %s, replies := [%s] }' %
            (i, pts(c['A']), pts(c['S']), pt(c['p']), c['h'], pass_s, rep))


HEADER = ('-- Generated by tools/gen19.py from snaky19.cards.txt; do not edit.\n')


def block_subtree(lo, hi):
    """Balanced CTree over card indices lo..hi inclusive."""
    if lo == hi:
        return '(.leaf %d c%d)' % (lo, lo)
    mid = (lo + hi + 1) // 2
    return '(.node %d %s %s)' % (mid, block_subtree(lo, mid - 1), block_subtree(mid, hi))


# ---------------------------------------------------------------- main

def main():
    src = sys.argv[1] if len(sys.argv) > 1 else 'snaky19.cards.txt'
    out = sys.argv[2] if len(sys.argv) > 2 else 'Submission/Gen19'
    rows, cols, root, rootxf, cards = parse(src)
    n = len(cards)
    print('parsed %d cards (root %d, board %dx%d, rootXf %s)' %
          (n, root, rows, cols, rootxf))

    # --- verify (Python replica of cardOK / rootOK) --------------------
    bad = [i for i, c in enumerate(cards) if not card_ok(cards, c)]
    assert not bad, 'cardOK fails for %r' % bad[:10]
    rc = cards[root]
    assert rc['A'] == [], 'root A nonempty'
    g = rootxf
    assert all(0 <= app(g, s)[0] < cols and 0 <= app(g, s)[1] < rows for s in rc['S'])
    assert 2 * rc['h'] <= rows * cols
    assert rc['h'] <= 19
    for i, c in enumerate(cards):
        for w, hh in c['replies']:
            j = hh[0]
            assert j < i, 'hint %d->%d not back' % (i, j)
            assert cards[j]['h'] < c['h'], 'hint %d->%d height' % (i, j)
    print('python replica: all %d cards justified, root ok' % n)

    os.makedirs(out, exist_ok=True)

    # --- blocks ------------------------------------------------------
    blocks = []  # (kind, indices) kind in {'plain','heavy','split'}
    i = 0
    while i < n:
        r = len(cards[i]['replies'])
        if r > SPLIT_REPLIES:
            blocks.append(('split', [i]))
            i += 1
        elif r > HEAVY_REPLIES:
            blocks.append(('heavy', [i]))
            i += 1
        else:
            j = i
            while (j < n and (j - i) < MAX_CARDS_PER_BLOCK
                   and len(cards[j]['replies']) <= HEAVY_REPLIES):
                j += 1
            blocks.append(('plain', list(range(i, j))))
            i = j
    print('blocks: %d (%d plain, %d heavy, %d split)' %
          (len(blocks), sum(1 for k, _ in blocks if k == 'plain'),
           sum(1 for k, _ in blocks if k == 'heavy'),
           sum(1 for k, _ in blocks if k == 'split')))

    # --- Data files --------------------------------------------------
    ndata = (n + DATA_CARDS_PER_FILE - 1) // DATA_CARDS_PER_FILE
    for d in range(ndata):
        lo = d * DATA_CARDS_PER_FILE
        hi = min(n, lo + DATA_CARDS_PER_FILE)
        with open(os.path.join(out, 'Data%02d.lean' % d), 'w') as f:
            f.write(HEADER)
            f.write('import Submission.Cards\n\nnamespace Snaky.Gen19\n\n')
            for i in range(lo, hi):
                f.write(card_def(i, cards[i]) + '\n')
            f.write('\nend Snaky.Gen19\n')

    # --- Tree.lean ---------------------------------------------------
    with open(os.path.join(out, 'Tree.lean'), 'w') as f:
        f.write(HEADER)
        for d in range(ndata):
            f.write('import Submission.Gen19.Data%02d\n' % d)
        f.write('\nnamespace Snaky.Gen19\n\n')
        for b, (kind, idx) in enumerate(blocks):
            lo, hi = idx[0], idx[-1]
            f.write('/-- Block %d: cards %d-%d (%s). -/\n' % (b, lo, hi, kind))
            f.write('def t%d : CTree := %s\n\n' % (b, block_subtree(lo, hi)))

        def compose(lo, hi):
            """(term, proof) for blocks lo..hi (block indices)."""
            if lo == hi:
                return 't%d' % lo, 't%d_ok' % lo
            mid = (lo + hi + 1) // 2
            lt, lp = compose(lo, mid - 1)
            rt, rp = compose(mid, hi)
            m = blocks[mid][1][0]
            return ('(.node %d %s %s)' % (m, lt, rt),
                    '(CTree.all_node %s %s)' % (lp, rp))

        tree_term, tree_proof = compose(0, len(blocks) - 1)
        f.write('/-- All %d cards, indexed `0 … %d`. -/\n' % (n, n - 1))
        f.write('def tree : CTree := %s\n\n' % tree_term)
        f.write('def getK : Nat → Option Card := tree.get\n\n')
        f.write('end Snaky.Gen19\n')

    # --- Chunk files -------------------------------------------------
    for b, (kind, idx) in enumerate(blocks):
        lo, hi = idx[0], idx[-1]
        if kind == 'split':
            i = lo
            c = cards[i]
            S = c['S']
            with open(os.path.join(out, 'Chunk%03dHead.lean' % b), 'w') as f:
                f.write(HEADER)
                f.write('import Submission.Gen19.Tree\n\nnamespace Snaky.Gen19\n\n')
                f.write('set_option maxHeartbeats 0 in\n')
                f.write('/-- Card %d: move, height, and pass hint. -/\n' % i)
                f.write('theorem c%d_head : cardHead getK c%d = true := by decide +kernel\n\n' % (i, i))
                f.write('end Snaky.Gen19\n')
            nparts = (len(S) + PART_SIZE - 1) // PART_SIZE
            for m in range(nparts):
                part = S[m * PART_SIZE:(m + 1) * PART_SIZE]
                with open(os.path.join(out, 'Chunk%03dR%d.lean' % (b, m)), 'w') as f:
                    f.write(HEADER)
                    f.write('import Submission.Gen19.Tree\n\nnamespace Snaky.Gen19\n\n')
                    f.write('def c%d_part%d : List Pt := %s\n\n' % (i, m, pts(part)))
                    f.write('set_option maxHeartbeats 0 in\n')
                    f.write('/-- Card %d: White replies at %d cells of its region (piece %d of %d). -/\n'
                            % (i, len(part), m + 1, nparts))
                    f.write('theorem c%d_r%d : c%d_part%d.all (replyOK getK c%d) = true := by decide +kernel\n\n'
                            % (i, m, i, m, i))
                    f.write('end Snaky.Gen19\n')
            with open(os.path.join(out, 'Chunk%03d.lean' % b), 'w') as f:
                f.write(HEADER)
                f.write('import Submission.Gen19.Chunk%03dHead\n' % b)
                for m in range(nparts):
                    f.write('import Submission.Gen19.Chunk%03dR%d\n' % (b, m))
                f.write('import Submission.CardsSound\n\nnamespace Snaky.Gen19\n\n')
                L = ' ++ '.join('c%d_part%d' % (i, m) for m in range(nparts))
                rthms = ', '.join('c%d_r%d' % (i, m) for m in range(nparts))
                f.write('/-- Card %d is justified (checked in %d pieces). -/\n' % (i, nparts + 1))
                f.write('theorem t%d_ok : t%d.all (cardOK getK) = true :=\n' % (b, b))
                f.write('  CTree.all_leaf (cardOK_of_split (%s) c%d_head (by decide +kernel)\n' % (L, i))
                f.write('    (by simp only [List.all_append, %s, Bool.and_self]))\n\n' % rthms)
                f.write('end Snaky.Gen19\n')
        else:
            with open(os.path.join(out, 'Chunk%03d.lean' % b), 'w') as f:
                f.write(HEADER)
                f.write('import Submission.Gen19.Tree\n\nnamespace Snaky.Gen19\n\n')
                f.write('set_option maxHeartbeats 0 in\n')
                f.write('/-- Cards %d-%d are justified. -/\n' % (lo, hi))
                f.write('theorem t%d_ok : t%d.all (cardOK getK) = true := by decide +kernel\n\n' % (b, b))
                f.write('end Snaky.Gen19\n')

    # --- All.lean ----------------------------------------------------
    with open(os.path.join(out, 'All.lean'), 'w') as f:
        f.write(HEADER)
        for b in range(len(blocks)):
            f.write('import Submission.Gen19.Chunk%03d\n' % b)
        f.write('import Submission.CardsSound\n\nnamespace Snaky.Gen19\n\n')
        f.write('/-- Every card in the lookup tree is justified. -/\n')
        f.write('theorem tree_ok : tree.all (cardOK getK) = true := %s\n\n' % tree_proof)
        f.write('end Snaky.Gen19\n')
    print('wrote %d data + 1 tree + %d chunk files + All.lean to %s' %
          (ndata, sum(1 + (len(idx) and kind == 'split') * 0 for kind, idx in blocks), out))


if __name__ == '__main__':
    main()
