#!/usr/bin/env python3
"""The one gate for Volume 16, declared once and run from here.

This file exists because the record carried two incompatible sets of second-gate
figures for the same ten mornings and neither set reproduced under a reading
anybody could name.  One implementation, one paragraph unit, one
normalisation, and every figure in the state layer derived from it.

THE PARAGRAPH UNIT, as declared by the batch prompt's ninth section:
  every non-blank line below a heading, a block-quote separator line carrying
  no words excluded, apparatus quote lines counted as paragraphs of their own,
  headings excluded, apparatus inside the scope of both gates.

THE NORMALISATION, in this order and no other order:
  1. case folded
  2. every hyphen replaced by a space, so a hyphenated compound is split
  3. an apostrophe inside a word deleted, every other punctuation mark replaced
     by a space, so that words either side of a comma do not fuse
  4. every run of digits replaced by the single token '#'
  5. every spelled cardinal number word replaced by the single token '#'
  6. every spelled ordinal number word replaced by the single token '#'
  7. the word 'and' left alone

THE READINGS:
  sliding       every eighteen-token window at every offset inside a paragraph
  whole-paragraph  non-overlapping eighteen-token chunks inside a paragraph,
                a remainder shorter than eighteen discarded

A SHAPE is a distinct normalised chunk string.  EXCESS is the number of chunk
instances over the number of distinct shapes.

GATE ONE is every paragraph of thirty words or more, counted on the whitespace
split of the raw line with no hyphen normalisation, compared for exact equality.

Usage:
    python3 reviews/gate.py <file-or-glob> [...]
    python3 reviews/gate.py --controls
"""

import glob
import os
import re
import sys
from collections import Counter

CHUNK = 18
FLOOR = 30

CARDINALS = set("""
zero one two three four five six seven eight nine ten eleven twelve thirteen
fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty
sixty seventy eighty ninety hundred thousand million billion
""".split())

ORDINALS = set("""
first second third fourth fifth sixth seventh eighth ninth tenth eleventh
twelfth thirteenth fourteenth fifteenth sixteenth seventeenth eighteenth
nineteenth twentieth thirtieth fortieth fiftieth sixtieth seventieth
eightieth ninetieth hundredth thousandth millionth
""".split())

NUMBERWORDS = CARDINALS | ORDINALS

HASH = "#"


def files_from(patterns):
    out = []
    for p in patterns:
        hits = sorted(glob.glob(p)) if any(c in p for c in "*?[") else [p]
        out.extend(h for h in hits if os.path.isfile(h))
    seen, uniq = set(), []
    for f in out:
        if f not in seen:
            seen.add(f)
            uniq.append(f)
    return uniq


def paragraphs(path):
    """The declared unit: one paragraph per non-blank, non-heading line.

    A block-quote separator line carrying no words is excluded, as the unit
    declares.  Such a line is a lone block-quote marker or a rule, which is one
    whitespace token and no alphanumeric character at all.  Note that a line
    reading '>' does carry a token to a whitespace split, so the test is
    alphanumerics and not tokens.  A line excluded this way can never be thirty
    words or more and can never produce an eighteen-token chunk, so the
    exclusion moves the paragraph count and no gate figure.
    """
    out = []
    for line in open(path, encoding="utf-8").read().split("\n"):
        s = line.strip()
        if not s or s.startswith("#"):
            continue
        if not any(ch.isalnum() for ch in s):
            continue
        out.append(s)
    return out


def normalize(text):
    s = text.casefold()
    s = s.replace("-", " ")
    s = re.sub(r"(?<=\w)'(?=\w)", "", s)
    s = "".join(" " if not (ch.isalnum() or ch == " ") else ch for ch in s)
    toks = []
    for t in s.split():
        if t.isdigit():
            toks.append(HASH)
        elif t in NUMBERWORDS:
            toks.append(HASH)
        else:
            toks.append(t)
    return toks


def chunks_nonoverlapping(tokens):
    return [tuple(tokens[i:i + CHUNK]) for i in range(0, len(tokens) - CHUNK + 1, CHUNK)]


def chunks_sliding(tokens):
    return [tuple(tokens[i:i + CHUNK]) for i in range(0, len(tokens) - CHUNK + 1)]


def tally(chunks):
    c = Counter(chunks)
    shapes = sum(1 for v in c.values() if v > 1)
    excess = sum(v - 1 for v in c.values() if v > 1)
    return len(chunks), shapes, excess, c


def report(paths, label):
    paras = []
    for p in paths:
        paras.extend((p, x) for x in paragraphs(p))
    raw_words = [len(x.split()) for _, x in paras]

    sliding = []
    whole = []
    for p, x in paras:
        toks = normalize(x)
        sliding.extend(chunks_sliding(toks))
        whole.extend(chunks_nonoverlapping(toks))

    n_s, sh_s, ex_s, cs = tally(sliding)
    n_w, sh_w, ex_w, cw = tally(whole)

    big = [x for _, x in paras if len(x.split()) >= FLOOR]
    gc = Counter(big)
    dup_pairs = sum(v - 1 for v in gc.values() if v > 1)

    print("== %s ==" % label)
    print("files: %d" % len(paths))
    print("paragraph unit: %d paragraphs, %d of %d words or more, gate one exact pairs %d"
          % (len(paras), len(big), FLOOR, dup_pairs))
    print("sliding: %d windows, %d repeated shapes, %d excess" % (n_s, sh_s, ex_s))
    print("whole-paragraph: %d chunks, %d repeated shapes, %d excess" % (n_w, sh_w, ex_w))
    top = sorted(((v, " ".join(k)) for k, v in cs.items() if v > 1), reverse=True)[:5]
    for v, k in top:
        print("   top sliding shape x%d: %s" % (v, k))
    return {"paras": len(paras), "big": len(big), "gate1": dup_pairs,
            "sliding": (n_s, sh_s, ex_s), "whole": (n_w, sh_w, ex_w)}


def controls():
    """A paragraph built to collide with itself, checked against itself.

    Two controls.  The long one carries a repeated run with enough distinct
    alphabetic words around it to survive the normalisation; the short one is
    the same construction at half the length.  Both are measured as a single
    paragraph, which is the case no gate in this repository can otherwise see.
    """
    filler = ("the launder runs behind the tool house and the barrow stands "
              "against the wall until somebody comes back for it again").split()
    long_ctrl = []
    for i in range(6):
        long_ctrl.extend(filler)
        long_ctrl.extend(filler[i * 3:i * 3 + 9])
    short_ctrl = []
    for i in range(2):
        short_ctrl.extend(filler)
        short_ctrl.extend(filler[i * 5:i * 5 + 9])
    for name, ctrl in (("long", long_ctrl), ("short", short_ctrl)):
        toks = normalize(" ".join(ctrl))
        n_s, sh_s, ex_s, cs = tally(chunks_sliding(toks))
        n_w, sh_w, ex_w, cw = tally(chunks_nonoverlapping(toks))
        print("control %s: %d tokens; sliding %d repeated shapes / %d excess; "
              "whole-paragraph %d shapes / %d excess"
              % (name, len(toks), sh_s, ex_s, sh_w, ex_w))


def main(argv):
    if not argv:
        print(__doc__)
        return 1
    if argv[0] == "--controls":
        controls()
        return 0
    paths = files_from(argv)
    if not paths:
        print("no files matched")
        return 1
    report(paths, " ".join(argv))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))