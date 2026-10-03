#!/usr/bin/env python3
"""Volume 16 Batch 0003 verification harness.

Paragraph unit: every non-blank line below a heading, a block-quote separator
line carrying no words excluded, apparatus quote lines counted as paragraphs of
their own, headings excluded, apparatus inside the scope of both gates.

Normalisation for both readings: numerals and spelled number words both replaced
by one token, the word *and* left alone, every hyphenated compound split on the
hyphen before lookup, punctuation dropped, case folded.
"""

import re
import sys
import collections
import itertools
from pathlib import Path

BATCH = Path(__file__).resolve().parent
FILES = [BATCH / f"chapter-{n:04d}.md" for n in range(756, 766)]

# ---------------------------------------------------------------- normalisation

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

NUMBER_WORDS = set()
for w in ONES:
    NUMBER_WORDS.add(w)
for w in TENS:
    NUMBER_WORDS.add(w)
for w in ["hundred", "thousand", "million"]:
    NUMBER_WORDS.add(w)
for w in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
          "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
          "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
          "nineteenth", "twentieth", "thirtieth", "fortieth", "fiftieth",
          "sixtieth", "seventieth", "eightieth", "ninetieth", "hundredth",
          "thousandth"]:
    NUMBER_WORDS.add(w)
for a in ["a", "one"]:
    NUMBER_WORDS.add(a + " hundred")
    NUMBER_WORDS.add(a + " thousand")

TOKEN = "<NUM>"


def normalise_words(text):
    toks = []
    for raw in text.split():
        w = raw.lower()
        # split hyphenated compounds on the hyphen before lookup
        for part in w.split("-"):
            part = re.sub(r"[^a-z]", "", part)
            if not part:
                continue
            if part.isdigit():
                toks.append(TOKEN)
            elif part in NUMBER_WORDS:
                toks.append(TOKEN)
            else:
                toks.append(part)
    return toks


def paragraphs(path):
    """Every non-blank line below a heading, excluding a > line with no words."""
    out = []
    seen_heading = False
    for line in path.read_text().splitlines():
        if line.startswith("#"):
            seen_heading = True
            continue
        if not line.strip():
            continue
        if line.lstrip().startswith(">"):
            body = line.lstrip().lstrip(">").strip()
            if not body:
                continue
        if not seen_heading:
            continue
        out.append(line)
    return out


# ---------------------------------------------------------------- figure check

FIGURES = {
756: ["one thousand and three hundred and eighty-six hundredweight",
      "five hundred and nineteenth", "four hundred and eighty-six",
      "two hundred and forty-eight", "two hundred and thirty-eight",
      "five hundred and seventeen", "five hundred and sixteenth",
      "five hundred and eighteenth", "nine hundred and three",
      "nine hundred and fifty", "two hundred and six",
      "four hundred and forty-three", "four hundred and thirteen",
      "three hundred and nineteen", "four hundred and seven",
      "two hundred and sixteen"],
757: ["one thousand and three hundred and ninety-four hundredweight",
      "five hundred and twentieth", "four hundred and eighty-seven",
      "two hundred and forty-nine", "two hundred and thirty-eight",
      "five hundred and eighteen", "five hundred and seventeenth",
      "five hundred and nineteenth", "nine hundred and four",
      "nine hundred and fifty-one", "a hundred and sixty-nine", "twenty-nine",
      "a hundred and forty", "one hundred and twelfth",
      "four hundred and fourteen", "three hundred and twenty",
      "four hundred and eight", "two hundred and seventeen"],
758: ["one thousand and three hundred and eighty-nine hundredweight",
      "five hundred and twenty-first", "four hundred and eighty-eight",
      "two hundred and forty-nine", "two hundred and thirty-nine",
      "five hundred and nineteen", "five hundred and eighteenth",
      "five hundred and twentieth", "nine hundred and five",
      "nine hundred and fifty-two", "two hundred and seven",
      "four hundred and forty-five", "four hundred and fifteen",
      "three hundred and twenty-one", "four hundred and nine",
      "two hundred and eighteen"],
759: ["one thousand and three hundred and ninety-seven hundredweight",
      "five hundred and twenty-first", "four hundred and eighty-nine",
      "two hundred and fifty", "two hundred and thirty-nine",
      "five hundred and twenty", "five hundred and nineteenth",
      "five hundred and twenty-first", "nine hundred and six",
      "nine hundred and fifty-three", "four hundred and sixteen",
      "three hundred and twenty-two", "four hundred and ten",
      "two hundred and nineteen"],
760: ["one thousand and three hundred and ninety-two hundredweight",
      "five hundred and twenty-third", "four hundred and ninety",
      "two hundred and fifty", "two hundred and forty",
      "five hundred and twenty-one", "five hundred and twentieth",
      "five hundred and twenty-second", "nine hundred and seven",
      "nine hundred and fifty-four", "two hundred and eight",
      "four hundred and forty-seven", "four hundred and seventeen",
      "three hundred and twenty-three", "four hundred and eleven",
      "two hundred and twenty"],
761: ["one thousand four hundred hundredweight",
      "five hundred and twenty-fourth", "four hundred and ninety-one",
      "two hundred and fifty-one", "two hundred and forty",
      "five hundred and twenty-two", "five hundred and twenty-first",
      "five hundred and twenty-third", "nine hundred and eight",
      "nine hundred and fifty-five", "a hundred and seventy", "twenty-nine",
      "a hundred and forty-one", "one hundred and thirteenth",
      "four hundred and eighteen", "three hundred and twenty-four",
      "four hundred and twelve", "two hundred and twenty-one"],
762: ["one thousand and three hundred and ninety-five hundredweight",
      "five hundred and twenty-fifth", "four hundred and ninety-two",
      "two hundred and fifty-one", "two hundred and forty-one",
      "five hundred and twenty-three", "five hundred and twenty-second",
      "five hundred and twenty-fourth", "nine hundred and nine",
      "nine hundred and fifty-six", "two hundred and nine",
      "four hundred and forty-nine", "four hundred and nineteen",
      "three hundred and twenty-five", "four hundred and thirteen",
      "two hundred and twenty-two"],
763: ["one thousand and four hundred and three hundredweight",
      "five hundred and twenty-sixth", "four hundred and ninety-three",
      "two hundred and fifty-two", "two hundred and forty-one",
      "five hundred and twenty-four", "five hundred and twenty-third",
      "five hundred and twenty-fifth", "nine hundred and ten",
      "nine hundred and fifty-seven", "four hundred and twenty",
      "three hundred and twenty-six", "four hundred and fourteen",
      "two hundred and twenty-three"],
764: ["one thousand and three hundred and ninety-eight hundredweight",
      "five hundred and twenty-seventh", "four hundred and ninety-four",
      "two hundred and fifty-two", "two hundred and forty-two",
      "five hundred and twenty-five", "five hundred and twenty-fourth",
      "five hundred and twenty-sixth", "nine hundred and eleven",
      "nine hundred and fifty-eight", "two hundred and ten",
      "four hundred and fifty-one", "four hundred and twenty-one",
      "three hundred and twenty-seven", "four hundred and fifteen",
      "two hundred and twenty-four"],
765: ["one thousand and four hundred and six hundredweight",
      "five hundred and twenty-eighth", "four hundred and ninety-five",
      "two hundred and fifty-three", "two hundred and forty-two",
      "five hundred and twenty-six", "five hundred and twenty-fifth",
      "five hundred and twenty-seventh", "nine hundred and twelve",
      "nine hundred and fifty-nine", "a hundred and seventy-one", "twenty-nine",
      "a hundred and forty-two", "one hundred and fourteenth",
      "four hundred and twenty-two", "three hundred and twenty-eight",
      "four hundred and sixteen", "two hundred and twenty-five"],
}

print("=" * 70)
print("1. FIGURE CHECK")
required = 0
failures = []
for f in FILES:
    n = int(f.stem.split("-")[1])
    text = f.read_text().lower()
    for fig in FIGURES[n]:
        required += 1
        if fig not in text:
            failures.append((n, fig))
print(f"   required {required}, present {required - len(failures)}, failures {len(failures)}")
for n, fig in failures:
    print(f"   FAIL chapter-{n}: {fig!r}")

# ------------------------------------------------------------- self-collision

print("=" * 70)
print("2. SELF-COLLISION CONTROLS (run before either gate)")

def _uniq_words(n):
    """n globally unique alphabetic filler tokens, no digits, no repeats."""
    letters = "abcdefghijklmnopqrstuvwxyz"
    out = []
    for i in range(n):
        s = ""
        k = i
        while True:
            s = letters[k % 26] + s
            k = k // 26 - 1
            if k < 0:
                break
        out.append(s * (1 + i // 26))
    return out


BLOCK = ("the middle row asked for another bucket and the man with the trowel "
         "said that he would not").split()      # exactly eighteen words
assert len(BLOCK) == 18, len(BLOCK)


def control(copies, n_gaps):
    """copies of one eighteen-word block separated by gaps of distinct lengths
    filled from a pool of globally unique alphabetic words larger than the sum
    of the gaps. Returns (shapes, excess) on the sliding reading and the
    whole-paragraph reading's excess."""
    gap_sizes = [i + 1 for i in range(n_gaps)]          # 1, 2, ... n_gaps
    total = sum(gap_sizes)
    filler = _uniq_words(total + 40)                    # larger than the sum
    # one leading filler token, so that no block start lands on a whole-
    # paragraph chunk boundary and the whole-paragraph reading is silent
    para, taken = [filler[0]], 1
    for i in range(copies):
        para.extend(BLOCK)
        if i < n_gaps:
            para.extend(filler[taken:taken + gap_sizes[i]])
            taken += gap_sizes[i]
    toks = normalise_words(" ".join(para))
    windows = [tuple(toks[i:i + 18]) for i in range(len(toks) - 17)]
    whole = [tuple(toks[i:i + 18]) for i in range(0, len(toks) - 17, 18)]
    def rep(seq):
        c = collections.Counter(seq)
        return (sum(1 for v in c.values() if v > 1),
                sum(v - 1 for v in c.values() if v > 1))
    s_sh, s_ex = rep(windows)
    w_sh, w_ex = rep(whole)
    return s_sh, s_ex, w_sh, w_ex


for copies, n_gaps, want_s, want_w in [(28, 27, 27, 0), (13, 12, 12, 0)]:
    s_sh, s_ex, w_sh, w_ex = control(copies, n_gaps)
    ok = (s_ex == want_s and w_ex == want_w)
    print(f"   {copies} copies / {n_gaps} gaps: sliding shapes {s_sh} excess {s_ex}, "
          f"whole-paragraph excess {w_ex}  -> {'reproduces' if ok else 'DOES NOT REPRODUCE'}")

# ------------------------------------------------------------------- gate one

print("=" * 70)
print("3. GATE ONE - prose paragraphs of thirty words or more, exact pairs")
WORD_FLOOR = 30


def gate_one(files):
    paras = []
    for f in files:
        for p in paragraphs(f):
            if len(p.split()) >= WORD_FLOOR:
                paras.append((f.name, p.strip()))
    c = collections.Counter(p for _, p in paras)
    pairs = [(k, v) for k, v in c.items() if v > 1]
    return paras, pairs


batch_paras, batch_pairs = gate_one(FILES)
print(f"   batch scope: {len(batch_paras)} paragraphs of thirty words or more, "
      f"{len(batch_pairs)} exact pairs")
for k, v in batch_pairs:
    print("     PAIR:", k[:90])

all_chapters = sorted(BATCH.parent.parent.glob("volume-1[56]/*/chapter-*.md")) + FILES
all_chapters = sorted({p.resolve() for p in all_chapters})
w_paras, w_pairs = gate_one(all_chapters)
print(f"   Volume 15 and 16 scope: {len(w_paras)} paragraphs, {len(w_pairs)} exact pairs")
names = collections.Counter()
for k, v in w_pairs:
    for n, p in batch_paras:
        if p == k:
            names[k] = n
    for f, p in w_paras:
        if p == k:
            names[k] = f
for k, v in w_pairs:
    print("     PAIR:", names.get(k, "behind"), "|", k[:80])

WS = BATCH.parent.parent.parent / "workspace"
manuscript = sorted(WS.glob("volume-*/batch-*/chapter-*.md"))
m_paras, m_pairs = gate_one(manuscript)
touching = []
for k, v in m_pairs:
    for n, p in batch_paras:
        if p == k:
            touching.append((names.get(k), k))
print(f"   whole manuscript: {len(m_paras)} paragraphs, {len(m_pairs)} exact pairs, "
      f"of which {len(touching)} touch this batch (floor {WORD_FLOOR} words)")
for n, k in touching:
    print("     TOUCHES:", n, "|", k[:80])

# -------------------------------------------------------------- second gate

print("=" * 70)
print("4. SECOND GATE - whole-paragraph chunks and sliding eighteen-word windows")


def second_gate(files, label):
    whole_units = []
    win_units = []
    for f in files:
        for p in paragraphs(f):
            toks = normalise_words(p)
            for i in range(0, len(toks) - 17, 18):
                whole_units.append(tuple(toks[i:i + 18]))
            for i in range(len(toks) - 17):
                win_units.append(tuple(toks[i:i + 18]))
    def rep(seq):
        c = collections.Counter(seq)
        return (sum(1 for v in c.values() if v > 1),
                sum(v - 1 for v in c.values() if v > 1))
    w_sh, w_ex = rep(whole_units)
    s_sh, s_ex = rep(win_units)
    print(f"   {label}: whole-paragraph {len(whole_units)} units, {w_sh} shapes, {w_ex} excess; "
          f"sliding {len(win_units)} windows, {s_sh} shapes, {s_ex} excess")
    c = collections.Counter(win_units)
    for k, v in c.items():
        if v > 1:
            print("     SHAPE x%d:" % v, " ".join(k)[:110])
    return s_sh, s_ex


second_gate(FILES, "batch scope")
second_gate(all_chapters, "Volume 15 and Volume 16 scope")

# --------------------------------------------------- exact-duplicate sweep

print("=" * 70)
print("5. EXACT-DUPLICATE SWEEP at any paragraph length, whole manuscript")
dupes = collections.defaultdict(list)
for f in manuscript:
    for p in paragraphs(f):
        s = p.strip()
        if s:
            dupes[s].append(f.name)
repeats = {k: v for k, v in dupes.items() if len(v) > 1}
batch_dupes = {k: v for k, v in repeats.items()
               if any(n in v for n in [f.name for f in FILES])}
print(f"   duplicated paragraphs anywhere in the manuscript: {len(repeats)}")
print(f"   of those involving a morning in this batch: {len(batch_dupes)}")
for k, v in batch_dupes.items():
    print("     DUP:", v, "|", k[:90])
batch_names = {f.name for f in FILES}
batch_internal = collections.Counter()
for f in FILES:
    for p in paragraphs(f):
        s = p.strip()
        if s:
            batch_internal[s] += 1
internal = {k: v for k, v in batch_internal.items() if v > 1}
print(f"   repeated inside the batch itself: {len(internal)}")
for k, v in internal.items():
    print("     INTERNAL:", v, "|", k[:90])

# --------------------------------------------------------------- apparatus

print("=" * 70)
print("6. APPARATUS")
batch_blocks = 0
for f in FILES:
    run = 0
    for line in f.read_text().splitlines():
        if line.lstrip().startswith(">"):
            run += 1
            if run == 1:
                batch_blocks += 1
        else:
            run = 0
print(f"   blocks in this batch: {batch_blocks}")
spent = 0
where = []
for f in sorted(WS.glob("volume-16/batch-*/chapter-*.md")):
    run = 0
    for line in f.read_text().splitlines():
        if line.lstrip().startswith(">"):
            run += 1
            if run == 1:
                spent += 1
                where.append(f.name)
        else:
            run = 0
print(f"   blocks spent across the whole manuscript: {spent}")
print(f"   ceiling thirty, unspent: {30 - spent}")
print("   files carrying a block in this batch:", [n for n in where if n in batch_names])
lab = []
for f in sorted(WS.glob("volume-16/batch-*/chapter-*.md")):
    t = f.read_text()
    if re.search(r"^>\s*Entered", t, re.M):
        lab.append(f.name)
print("   Entered labels in Volume 16:", lab)

# ------------------------------------------------------------ manual sweeps

print("=" * 70)
print("7. MECHANICAL SWEEPS over the ten mornings")

bodies = {}
for f in FILES:
    bodies[f.name] = "\n".join(paragraphs(f))


def sweep(name, pattern, flags=0, scope=None):
    rx = re.compile(pattern, flags)
    hits = []
    for n, t in (scope or bodies).items():
        for m in rx.finditer(t):
            line = t[:m.start()].count("\n") + 1
            hits.append((n, line, t[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    print(f"   {name}: {len(hits)}")
    for h in hits[:8]:
        print("      ", h[0], "line", h[1], "|", h[2][:100])


sweep("digits in body prose", r"\d")
sweep("non-ascii in body prose", r"[^\x00-\x7f]")
sweep("em/en dash or figure dash", r"[—–‒−]")
bare = r"\b(volume|batch|chapter|seat|fieldbook|tally|panel)\b"
sweep("the six bare words and the apparatus word", bare, re.I)
months = (r"\b(january|february|march|april|may|june|july|august|september|"
          r"october|november|december)\b")
sweep("the twelve month names", months, re.I)
sweep("anchor", r"\banchors?\b|\banchored\b|\banchoring\b", re.I)
sweep("rootmark", r"rootmarks?", re.I)
sweep("the arrangement words", r"\b(surrender|surrendered|release|released|"
      r"releases|releasing|resign|resigned|resigning|resignation)\b", re.I)
sweep("discharged", r"discharg", re.I)
sweep("apolog", r"apolog", re.I)
sweep("the six load-bearing strings",
      r"anywhere in four counties|whether it is on or off|far end of a thing|"
      r"the comfort is not standing|the father is not alive in the wood|"
      r"the day does not come back", re.I)
sweep("the attached hundredweight form", r"\d+hundredweight", re.I)
sweep("the second reckoning on a morning that prints the first",
      r"ninety-ninth|one hundredth|one hundred and first")
sweep("the wrong form of the bare round hundred in print",
      r"one thousand and four hundred hundredweight")
sweep("rung climbed", r"\brung\b|\brungs\b|\bclimb\w*\b|\bascend\w*\b", re.I)
sweep("rung climbed, narrowed", r"put a foot on|foot on it|climbed")
sweep("a figure against the door nine hundred yards off", r"sixty-six")
sweep("of this month", r"of this month", re.I)
sweep("discharged/let out of the compost line", r"nothing has been let out|"
      r"nothing has ever come out|column that would take it")

print("=" * 70)
print("8. ORDINALS OUTSIDE HEADINGS")
ORD_WORDS = ("ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth",
             "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth",
             "twentieth", "thirtieth")
ordrx = re.compile(r"\b(" + "|".join(ORD_WORDS) + r")\b", re.I)
flagged = 0
for n, t_ in bodies.items():
    for m in ordrx.finditer(t_):
        before = re.findall(r"[A-Za-z-]+", t_[:m.start()])[-2:]
        if before and (before[-1].lower() in ("and", "hundred", "thousand")):
            continue          # part of a spelled figure, not a date
        flagged += 1
        line = t_[:m.start()].count("\n") + 1
        print(f"   {n} line {line}: {m.group(0)!r} preceded by {before}")
print(f"   ordinal words standing as dates outside a heading: {flagged}")

print("=" * 70)
print("9. WORD COUNTS")
tot = 0
for f in FILES:
    w = len(f.read_text().split())
    tot += w
    print(f"   {f.name}: {w}")
print(f"   batch total: {tot}")
print("=" * 70)