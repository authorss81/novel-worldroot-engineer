#!/usr/bin/env python3
"""Volume 16 Batch 0004 verification harness.

Paragraph unit: every non-blank line below a heading, a block-quote separator
line carrying no words excluded, apparatus quote lines counted as paragraphs of
their own, headings excluded, apparatus inside the scope of both gates.

Normalisation for both readings: numerals and spelled number words both replaced
by one token, the word *and* left alone, every hyphenated compound split on the
hyphen before lookup, punctuation dropped, case folded.
"""

import re
import bisect
import collections
from pathlib import Path

BATCH = Path(__file__).resolve().parent
FILES = [BATCH / f"chapter-{n:04d}.md" for n in range(766, 776)]

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
    out = []
    seen_heading = False
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
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
        out.append((lineno, line))
    return out


# ---------------------------------------------------------------- figure check
# Derived here and not inherited: fourteen on every morning, two more on each of
# the five odd mornings, four more on each of the two fourth-line mornings.

FIGURES = {
    766: ["one thousand and four hundred and one hundredweight",
          "five hundred and twenty-ninth", "four hundred and ninety-six",
          "two hundred and fifty-three", "two hundred and forty-three",
          "five hundred and twenty-seventh", "five hundred and twenty-sixth",
          "five hundred and twenty-eighth", "nine hundred and thirteen",
          "nine hundred and sixty", "two hundred and eleven",
          "four hundred and fifty-three", "four hundred and twenty-three",
          "three hundred and twenty-nine", "four hundred and seventeen",
          "two hundred and twenty-six"],
    767: ["one thousand and four hundred and nine hundredweight",
          "five hundred and thirtieth", "four hundred and ninety-seven",
          "two hundred and fifty-four", "two hundred and forty-three",
          "five hundred and twenty-eighth", "five hundred and twenty-seventh",
          "five hundred and twenty-ninth", "nine hundred and fourteen",
          "nine hundred and sixty-one", "four hundred and twenty-four",
          "three hundred and thirty", "four hundred and eighteen",
          "two hundred and twenty-seven"],
    768: ["one thousand and four hundred and four hundredweight",
          "five hundred and thirty-first", "four hundred and ninety-eight",
          "two hundred and fifty-four", "two hundred and forty-four",
          "five hundred and twenty-ninth", "five hundred and twenty-eighth",
          "five hundred and thirtieth", "nine hundred and fifteen",
          "nine hundred and sixty-two", "two hundred and twelve",
          "four hundred and fifty-five", "four hundred and twenty-five",
          "three hundred and thirty-one", "four hundred and nineteen",
          "two hundred and twenty-eight"],
    769: ["one thousand and four hundred and twelve hundredweight",
          "five hundred and thirty-second", "four hundred and ninety-nine",
          "two hundred and fifty-five", "two hundred and forty-four",
          "five hundred and thirty", "five hundred and twenty-ninth",
          "five hundred and thirty-first", "nine hundred and sixteen",
          "nine hundred and sixty-three", "a hundred and seventy-two",
          "twenty-nine", "a hundred and forty-three",
          "one hundred and fifteenth", "four hundred and twenty-six",
          "three hundred and thirty-two", "four hundred and twenty",
          "two hundred and twenty-nine"],
    770: ["one thousand and four hundred and seven hundredweight",
          "five hundred and thirty-third", "five hundred",
          "two hundred and fifty-five", "two hundred and forty-five",
          "five hundred and thirty-first", "five hundred and thirtieth",
          "five hundred and thirty-second", "nine hundred and seventeen",
          "nine hundred and sixty-four", "two hundred and thirteen",
          "four hundred and fifty-seven", "four hundred and twenty-seven",
          "three hundred and thirty-three", "four hundred and twenty-one",
          "two hundred and thirty"],
    771: ["one thousand and four hundred and fifteen hundredweight",
          "five hundred and thirty-fourth", "five hundred and one",
          "two hundred and fifty-six", "two hundred and forty-five",
          "five hundred and thirty-second", "five hundred and thirty-first",
          "five hundred and thirty-third", "nine hundred and eighteen",
          "nine hundred and sixty-five", "four hundred and twenty-eight",
          "three hundred and thirty-four", "four hundred and twenty-two",
          "two hundred and thirty-one"],
    772: ["one thousand and four hundred and ten hundredweight",
          "five hundred and thirty-fifth", "five hundred and two",
          "two hundred and fifty-six", "two hundred and forty-six",
          "five hundred and thirty-third", "five hundred and thirty-second",
          "five hundred and thirty-fourth", "nine hundred and nineteen",
          "nine hundred and sixty-six", "two hundred and fourteen",
          "four hundred and fifty-nine", "four hundred and twenty-nine",
          "three hundred and thirty-five", "four hundred and twenty-three",
          "two hundred and thirty-two"],
    773: ["one thousand and four hundred and eighteen hundredweight",
          "five hundred and thirty-sixth", "five hundred and three",
          "two hundred and fifty-seven", "two hundred and forty-six",
          "five hundred and thirty-fourth", "five hundred and thirty-third",
          "five hundred and thirty-fifth", "nine hundred and twenty",
          "nine hundred and sixty-seven", "a hundred and seventy-three",
          "twenty-nine", "a hundred and forty-four",
          "one hundred and sixteenth", "four hundred and thirty",
          "three hundred and thirty-six", "four hundred and twenty-four",
          "two hundred and thirty-three"],
    774: ["one thousand and four hundred and thirteen hundredweight",
          "five hundred and thirty-seventh", "five hundred and four",
          "two hundred and fifty-seven", "two hundred and forty-seven",
          "five hundred and thirty-fifth", "five hundred and thirty-fourth",
          "five hundred and thirty-sixth", "nine hundred and twenty-one",
          "nine hundred and sixty-eight", "two hundred and fifteen",
          "four hundred and sixty-one", "four hundred and thirty-one",
          "three hundred and thirty-seven", "four hundred and twenty-five",
          "two hundred and thirty-four"],
    775: ["one thousand and four hundred and twenty-one hundredweight",
          "five hundred and thirty-eighth", "five hundred and five",
          "two hundred and fifty-eight", "two hundred and forty-seven",
          "five hundred and thirty-sixth", "five hundred and thirty-fifth",
          "five hundred and thirty-seventh", "nine hundred and twenty-two",
          "nine hundred and sixty-nine", "four hundred and thirty-two",
          "three hundred and thirty-eight", "four hundred and twenty-six",
          "two hundred and thirty-five"],
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
         "said that he would not").split()
assert len(BLOCK) == 18, len(BLOCK)


def control(copies, n_gaps):
    gap_sizes = [i + 1 for i in range(n_gaps)]
    total = sum(gap_sizes)
    filler = _uniq_words(total + 40)
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
        for _, p in paragraphs(f):
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
        for _, p in paragraphs(f):
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
    for _, p in paragraphs(f):
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
    for _, p in paragraphs(f):
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
print(f"   blocks spent across Volume 16: {spent}")
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
body_starts = {}
body_lines = {}
for f in FILES:
    lines = paragraphs(f)
    bodies[f.name] = "\n".join(t for _, t in lines)
    starts, pos = [], 0
    for _, t in lines:
        starts.append(pos)
        pos += len(t) + 1
    body_starts[f.name] = starts
    body_lines[f.name] = [n for n, _ in lines]


def file_line(name, offset):
    i = bisect.bisect_right(body_starts[name], offset) - 1
    if i < 0:
        return body_lines[name][0]
    return body_lines[name][i]


def sweep(name, pattern, flags=0, scope=None):
    rx = re.compile(pattern, flags)
    hits = []
    for n, t in (scope or bodies).items():
        for m in rx.finditer(t):
            line = file_line(n, m.start())
            hits.append((n, line, t[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    print(f"   {name}: {len(hits)}")
    for h in hits[:8]:
        print("      ", h[0], "line", h[1], "|", h[2][:100])
    return hits


sweep("digits in body prose", r"\d")
sweep("non-ascii in body prose", r"[^\x00-\x7f]")
sweep("em/en dash or figure dash", r"[\u2014\u2013\u2012\u2212]")
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
      r"one hundred and second|one hundred and third")
sweep("the wrong form of the bare round hundred in print",
      r"one thousand and four hundred hundredweight")
sweep("rung climbed", r"\brung\b|\brungs\b|\bclimb\w*\b|\bascend\w*\b", re.I)
sweep("a figure against the door nine hundred yards off", r"sixty-six")
sweep("of this month", r"of this month", re.I)
sweep("the let-go family", r"\blet go\b|\bletting go\b|go their own way|walk away",
      re.I)

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
            continue
        flagged += 1
        line = file_line(n, m.start())
        print(f"   {n} line {line}: {m.group(0)!r} preceded by {before}")
print(f"   ordinal words standing as dates outside a heading: {flagged}")


# ------------------------------------------- cross-batch verbatim (scope note)
# Published as a figure, so it needs an implementation on disk like every other.

print("=" * 70)
print("10. CROSS-BATCH VERBATIM WINDOWS, Volume 16 scope, and what each is")


def raw_tokens(p):
    return tuple(w for w in re.sub(r"[^A-Za-z0-9' -]", " ", p).lower().split() if w)


v16 = sorted(WS.glob("volume-16/batch-*/chapter-*.md"))
vwin = collections.Counter()
vwhere = collections.defaultdict(set)
for f in v16:
    for _, p in paragraphs(f):
        t = raw_tokens(p)
        for i in range(len(t) - 17):
            k = tuple(t[i:i + 18])
            vwin[k] += 1
            vwhere[k].add(f.name)
mine_names = {f.name for f in FILES}
cats = collections.Counter()
other = []
for k, v in vwin.items():
    if v < 2 or not (vwhere[k] & mine_names):
        continue
    s = " ".join(k)
    if "father is not alive in the wood" in s:
        cats["the locked comfort line, spent once and verbatim by design"] += 1
    elif "thirteen from the other one" in s:
        cats["Sera Quill's thirteen-apart line, her standing tic"] += 1
    elif "out of the gate at her own pace" in s:
        cats["Iona Vey's exit, deliberately identical to her first walk out"] += 1
    else:
        cats["a floor being restated, or a speaker's standing line"] += 1
        other.append((k, vwhere[k]))
print(f"   verbatim repeated eighteen-word windows in Volume 16: "
      f"{sum(1 for v in vwin.values() if v > 1)}")
print(f"   of those involving a morning in this batch: "
      f"{sum(1 for k, v in vwin.items() if v > 1 and vwhere[k] & mine_names)}")
for a, b in cats.most_common():
    print(f"     {b:>4}  {a}")
print("   NONE of these is a pair of prose paragraphs, and the exact-duplicate")
print("   sweep at any paragraph length returns nil for this batch at both")
print("   scopes. BATCH SCOPE IS THE GOVERNING READING AND IT IS NIL ON BOTH.")

print("=" * 70)
print("9. WORD COUNTS")
tot = 0
for f in FILES:
    w = len(f.read_text().split())
    tot += w
    print(f"   {f.name}: {w}")
print(f"   batch total: {tot}")
print("=" * 70)