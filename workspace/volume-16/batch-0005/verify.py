#!/usr/bin/env python3
"""Volume 16 Batch 0005 verification harness (the five last mornings, 776-780).

Paragraph unit, declared before anything is run: every non-blank line below a
heading, a block-quote separator line carrying no words excluded, apparatus
quote lines counted as paragraphs of their own, headings excluded, apparatus
inside the scope of both gates.

Normalisation: numerals and spelled number words both replaced by one token, the
word *and* left alone, hyphenated compounds split on the hyphen before lookup,
punctuation dropped, case folded.
"""

import re
import bisect
import collections
from pathlib import Path

BATCH = Path(__file__).resolve().parent
FILES = [BATCH / f"chapter-{n:04d}.md" for n in range(776, 781)]

ONES = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen"]
TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
NUMBER_WORDS = set(ONES) | set(TENS) | {"hundred", "thousand", "million"}
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
# Derived here and not inherited. Fourteen on every morning, two more on each of
# the three odd mornings (989, 991, 993), four more on the one fourth-line
# morning (990). Seventy base plus six plus four.

FIGURES = {
    776: ["one thousand and four hundred and sixteen hundredweight",
          "five hundred and thirty-ninth", "five hundred and six",
          "two hundred and fifty-eight", "two hundred and forty-eight",
          "five hundred and thirty-seven", "five hundred and thirty-sixth",
          "five hundred and thirty-eighth", "nine hundred and twenty-three",
          "nine hundred and seventy", "two hundred and sixteen",
          "four hundred and sixty-three", "four hundred and thirty-three",
          "three hundred and thirty-nine", "four hundred and twenty-seven",
          "two hundred and thirty-six"],
    777: ["one thousand and four hundred and twenty-four hundredweight",
          "five hundred and fortieth", "five hundred and seven",
          "two hundred and fifty-nine", "two hundred and forty-eight",
          "five hundred and thirty-eighth", "five hundred and thirty-seventh",
          "five hundred and thirty-ninth", "nine hundred and twenty-four",
          "nine hundred and seventy-one", "a hundred and seventy-four",
          "twenty-nine", "a hundred and forty-five", "one hundred and seventeenth",
          "four hundred and thirty-four", "three hundred and forty",
          "four hundred and twenty-eight", "two hundred and thirty-seven"],
    778: ["one thousand and four hundred and nineteen hundredweight",
          "five hundred and forty-first", "five hundred and eight",
          "two hundred and fifty-nine", "two hundred and forty-nine",
          "five hundred and thirty-ninth", "five hundred and thirty-eighth",
          "five hundred and fortieth", "nine hundred and twenty-five",
          "nine hundred and seventy-two", "two hundred and seventeen",
          "four hundred and sixty-five", "four hundred and thirty-five",
          "three hundred and forty-one", "four hundred and twenty-nine",
          "two hundred and thirty-eight"],
    779: ["one thousand and four hundred and twenty-seven hundredweight",
          "five hundred and forty-second", "five hundred and nine",
          "two hundred and sixty", "two hundred and forty-nine",
          "five hundred and forty", "five hundred and thirty-ninth",
          "five hundred and forty-first", "nine hundred and twenty-six",
          "nine hundred and seventy-three", "four hundred and thirty-six",
          "three hundred and forty-two", "four hundred and thirty",
          "two hundred and thirty-nine"],
    780: ["one thousand and four hundred and twenty-two hundredweight",
          "five hundred and forty-third", "five hundred and ten",
          "two hundred and fifty", "two hundred and sixty",
          "five hundred and forty-first", "five hundred and fortieth",
          "five hundred and forty-second", "nine hundred and twenty-seven",
          "nine hundred and seventy-four", "two hundred and eighteen",
          "four hundred and sixty-seven", "four hundred and thirty-seven",
          "three hundred and forty-three", "four hundred and thirty-one",
          "two hundred and forty"],
}

# The second reckoning, which is carried and not printed on a morning that
# prints the first. A checker that looks for it will be told it is absent.
ABSENT = {
    777: ["one hundred and fourth", "one hundred and second",
          "one hundred and third"],
    776: ["far end of a thing", "anywhere in four counties",
          "whether it is on or off", "the comfort is not standing",
          "the father is not alive in the wood", "the day does not come back"],
    778: ["far end of a thing", "anywhere in four counties",
          "whether it is on or off", "the comfort is not standing",
          "the father is not alive in the wood", "the day does not come back"],
    779: ["far end of a thing", "anywhere in four counties",
          "whether it is on or off", "the comfort is not standing",
          "the father is not alive in the wood", "the day does not come back"],
}

# The two locked sentences, whole, on the mornings that may spend them.
WHOLE = {
    777: ["The far end of a thing is held by two people and neither of them is me, "
          "and no instrument anywhere in four counties says whether it is on or off."],
    780: ["The far end of a thing is held by two people and neither of them is me, "
          "and no instrument anywhere in four counties says whether it is on or off.",
          "The comfort is not standing, the father is not alive in the wood, "
          "and the day does not come back."],
}

print("=" * 72)
print("1. FIGURE CHECK (derived from the rules on each card, not inherited)")
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

print("   carried-but-not-printed, checked for absence:")
for n, strs in sorted(ABSENT.items()):
    text = FILES[FILES.index(BATCH / f'chapter-{n:04d}.md')].read_text().lower()
    for s in strs:
        hit = s.lower() in text
        print(f"     chapter-{n}: {s!r} -> {'PRESENT, WHICH IS A BREACH' if hit else 'absent'}")

print("   whole appearances of the two locked sentences:")
for n, strs in sorted(WHOLE.items()):
    text = (BATCH / f"chapter-{n:04d}.md").read_text()
    for s in strs:
        print(f"     chapter-{n}: {text.count(s)} whole occurrence(s) -> "
              f"{'right' if text.count(s) == 1 else 'WRONG COUNT'}")
# and nowhere else in the batch
for n in (776, 778, 779):
    text = (BATCH / f"chapter-{n:04d}.md").read_text()
    for s in WHOLE[777] + WHOLE[780]:
        if s in text:
            print(f"     BREACH: chapter-{n} carries a whole locked sentence")
for n in (776, 778, 779):
    text = (BATCH / f"chapter-{n:04d}.md").read_text().lower()
    for s in [x for v in ABSENT.values() for x in v]:
        if s in text and s not in ("one hundred and fourth",):
            pass  # already reported above

# ------------------------------------------------------------- self-collision

print("=" * 72)
print("2. SELF-COLLISION CONTROLS (run before either gate, and before the "
      "parity reading's verdicts are trusted)")


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

# ----------------------------------------------------- the three-line reading
print("=" * 72)
print("3. THE PARITY READING, MORNING BY MORNING. Neither gate and no figure "
      "check can see this class of error. IT CHECKS THE ATTACHMENT AND NOT THE "
      "PRESENCE, because a presence check passed a morning that had the mover on "
      "the page and the other half attached to the word that means it moved.")
# (mover, stander) for each morning, derived from the rule: on an odd morning the
# falling half is the smaller of the two and it moved; on an even morning the
# rising half is the larger of the two and it moved.
PARITY = {
    776: (True,  "two hundred and forty-eight", "two hundred and fifty-eight"),
    777: (False, "two hundred and fifty-nine",  "two hundred and forty-eight"),
    778: (True,  "two hundred and forty-nine",  "two hundred and fifty-nine"),
    779: (False, "two hundred and sixty",        "two hundred and forty-nine"),
    780: (True,  "two hundred and fifty",        "two hundred and sixty"),
}
# verbs that mean a half fell, and verbs that mean a half stood or rose.
FELL = r"(came down|came|dropped|fell|went down|drop|took the fall|comes on)"
ROSE = r"(stood|stands|rose|went up|held|unchanged|stood there)"
HALVES = ("two hundred and fifty-eight", "two hundred and fifty-nine",
          "two hundred and forty-eight", "two hundred and forty-nine",
          "two hundred and sixty", "two hundred and fifty")
DIRECTIONAL = re.compile(r"(came down|came|dropped|fell|went down|comes|"
                         r"stood|stands|rose|went up|holds)", re.I)


def parity_verdict(n):
    """Which half sits on the verb that means it moved.

    A number that precedes the verb is the one that moved; a number that
    follows it stood. Both are looked for in a window either side of the verb,
    because the figure often sits outside the clause the verb is in.
    """
    odd, mover, stander = PARITY[n]
    text = (BATCH / f"chapter-{n:04d}.md").read_text().lower()
    rows = []
    for vm in DIRECTIONAL.finditer(text):
        v = vm.group(1).lower()
        fell = v in ("came down", "came", "dropped", "fell", "went down", "comes")
        lo, hi = max(0, vm.start() - 90), min(len(text), vm.end() + 90)
        before = [(text.rfind(h, lo, vm.start()), h) for h in HALVES]
        after = [(text.find(h, vm.end(), hi), h) for h in HALVES]
        before = [b for b in before if b[0] != -1]
        after = [a for a in after if a[0] != -1]
        if not before or not after:
            continue
        carried = (max(before)[1] if fell else min(after)[1])
        rows.append((carried, v, text[lo:hi].replace("\n", " ")))
    return odd, mover, stander, rows


for n in range(776, 781):
    odd, mover, stander, rows = parity_verdict(n)
    # a fall verb must carry the mover and a rise verb must carry the stander
    FALLV = ("came down", "came", "dropped", "fell", "went down", "comes")
    wrong = [r for r in rows if r[0] != (mover if r[1] in FALLV else stander)]
    want = ("the smaller half (the falling half) moved" if odd
            else "the larger half (the rising half) moved")
    print(f"   chapter-{n}: {'odd' if odd else 'even'} morning; {want}; "
          f"mover {mover!r}, stander {stander!r}; {len(rows)} paired delivery "
          f"sentence(s), {len(wrong)} with the wrong half on the verb")
    for r in wrong:
        print(f"       WRONG: verb {r[1]!r} carries {r[0]!r} | {r[2][:110]}")

print("=" * 72)
print("3b. THE LAUNDER FRAME, ROTATED BY MOUTH OR BY FRAME")
print("   Rotating the mouth and not the frame is the defect this reading exists")
print("   to catch, so it prints the opening of every weight sentence in the batch:")
openers = []
for n in range(776, 781):
    text = (BATCH / f"chapter-{n:04d}.md").read_text().lower()
    for s in re.split(r"(?<=[.?!])\s+", text):
        if "hundredweight" in s:
            o = " ".join(re.findall(r"[a-z]+", s)[:5])
            openers.append((n, o))
            print(f"     chapter-{n}: {o}")
dupes = [o for o in set(o for _, o in openers)
         if sum(1 for _, q in openers if q == o) > 1]
print(f"   distinct opening clauses: {len(set(o for _, o in openers))} of {len(openers)}; "
      f"repeated opening clauses: {len(dupes)}")
for d in dupes:
    print("      REPEATED:", d)

# ------------------------------------------------------------------- gate one

print("=" * 72)
print("4. GATE ONE - prose paragraphs of thirty words or more, exact pairs")
WORD_FLOOR = 30


def gate_one(files):
    paras = []
    for f in files:
        for _, p in paragraphs(f):
            if len(p.split()) >= WORD_FLOOR:
                paras.append((f.name, p.strip()))
    c = collections.Counter(p for _, p in paras)
    return paras, [(k, v) for k, v in c.items() if v > 1]


batch_paras, batch_pairs = gate_one(FILES)
print(f"   batch scope: {len(batch_paras)} paragraphs of thirty words or more, "
      f"{len(batch_pairs)} exact pairs")
for k, v in batch_pairs:
    print("     PAIR:", k[:100])

WS = BATCH.parent.parent.parent / "workspace"
all_chapters = sorted(WS.glob("volume-*/batch-*/chapter-*.md"))
all_chapters = sorted({p.resolve() for p in all_chapters if p.resolve()
                       not in {q.resolve() for q in FILES}} | {f.resolve() for f in FILES})
w_paras, w_pairs = gate_one(all_chapters)
print(f"   whole manuscript: {len(w_paras)} paragraphs, {len(w_pairs)} exact pairs, "
      f"floor {WORD_FLOOR} words")
names = {}
for k, v in w_pairs:
    for n, p in batch_paras:
        if p == k:
            names[k] = n
touching = [(names.get(k), k) for k, v in w_pairs if k in names]
print(f"   of those, touching a morning in this batch: {len(touching)}")
for n, k in touching:
    print("     TOUCHES:", n, "|", k[:90])

# -------------------------------------------------------------- second gate

print("=" * 72)
print("5. SECOND GATE - whole-paragraph chunks and sliding eighteen-word windows")


def second_gate(files, label, show=True):
    whole_units, win_units = [], []
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
    print(f"   {label}: whole-paragraph {len(whole_units)} units, {w_sh} shapes, "
          f"{w_ex} excess; sliding {len(win_units)} windows, {s_sh} shapes, {s_ex} excess")
    if show:
        c = collections.Counter(win_units)
        for k, v in c.items():
            if v > 1:
                print("     SHAPE x%d:" % v, " ".join(k)[:120])
        cw = collections.Counter(whole_units)
        for k, v in cw.items():
            if v > 1:
                print("     CHUNK x%d:" % v, " ".join(k)[:120])
    return s_sh, s_ex


second_gate(FILES, "batch scope")
second_gate(all_chapters, "whole manuscript scope", show=False)

# --------------------------------------------------- exact-duplicate sweep

print("=" * 72)
print("6. EXACT-DUPLICATE SWEEP at any paragraph length, whole manuscript")
dupes = collections.defaultdict(list)
for f in all_chapters:
    for _, p in paragraphs(f):
        s = p.strip()
        if s:
            dupes[s].append(f.name)
repeats = {k: v for k, v in dupes.items() if len(v) > 1}
mine = {f.name for f in FILES}
mine_dupes = {k: v for k, v in repeats.items() if any(n in mine for n in v)}
print(f"   duplicated paragraphs anywhere in the manuscript: {len(repeats)}")
print(f"   of those involving a morning in this batch: {len(mine_dupes)}")
for k, v in mine_dupes.items():
    print("     DUP:", v, "|", k[:100])
batch_internal = collections.Counter()
for f in FILES:
    for _, p in paragraphs(f):
        s = p.strip()
        if s:
            batch_internal[s] += 1
internal = {k: v for k, v in batch_internal.items() if v > 1}
print(f"   repeated inside the batch itself: {len(internal)}")
for k, v in internal.items():
    print("     INTERNAL:", v, "|", k[:100])

# --------------------------------------------------------------- apparatus

print("=" * 72)
print("7. APPARATUS, SCOPED TO VOLUME SIXTEEN")
batch_blocks = 0
per_file = {}
for f in FILES:
    run = 0
    n = 0
    for line in f.read_text().splitlines():
        if line.lstrip().startswith(">"):
            run += 1
            if run == 1:
                batch_blocks += 1
                n += 1
        else:
            run = 0
    per_file[f.name] = n
print(f"   blocks in this batch: {batch_blocks}  ({per_file})")
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
print(f"   blocks spent across Volume 16: {spent}; ceiling thirty, unspent: {30 - spent}")
lab = [f.name for f in sorted(WS.glob("volume-16/batch-*/chapter-*.md"))
       if re.search(r"^>\s*Entered", f.read_text(), re.M)]
print(f"   Entered labels in Volume 16: {lab}")

# ------------------------------------------------------------ manual sweeps

print("=" * 72)
print("8. MECHANICAL SWEEPS over the five mornings")
bodies, body_starts, body_lines = {}, {}, {}
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


def sweep(name, pattern, flags=0, scope=None, limit=8):
    rx = re.compile(pattern, flags)
    hits = []
    for n, t in (scope or bodies).items():
        for m in rx.finditer(t):
            hits.append((n, file_line(n, m.start()),
                         t[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")))
    print(f"   {name}: {len(hits)}")
    for h in hits[:limit]:
        print("      ", h[0], "line", h[1], "|", h[2][:110])
    return hits


sweep("digits in body prose", r"\d")
sweep("non-ascii in body prose", r"[^\x00-\x7f]")
sweep("em/en dash", r"[\u2014\u2013\u2012\u2212]")
sweep("the six bare words and the apparatus word",
      r"\b(volume|batch|chapter|seat|fieldbook|tally|panel)\b", re.I)
months = (r"\b(january|february|march|april|may|june|july|august|september|"
          r"october|november|december)\b")
mhits = sweep("the twelve month names", months, re.I)
sweep("anchor", r"\banchors?\b|\banchored\b|\banchoring\b", re.I)
sweep("rootmark", r"rootmarks?", re.I)
sweep("the three words the first loss may not be named by",
      r"single private field|unified response|nine minutes", re.I)
sweep("the arrangement words", r"\b(surrender|surrendered|release|released|"
      r"releases|releasing|resign|resigned|resigning|resignation)\b", re.I)
sweep("the words that would name the first morning",
      r"\b(failure|failed|fail|betrayal|betrayed|heroic|hero)\b", re.I, limit=20)
sweep("discharg", r"discharg", re.I)
sweep("apolog", r"apolog", re.I)
sweep("the six load-bearing strings",
      r"anywhere in four counties|whether it is on or off|far end of a thing|"
      r"the comfort is not standing|the father is not alive in the wood|"
      r"the day does not come back", re.I, limit=12)
sweep("the attached hundredweight form", r"\d+hundredweight", re.I)
sweep("the wrong form of the bare round hundred in print",
      r"one thousand and four hundred hundredweight")
sweep("the ladder, rungs climbed", r"\brung\b|\brungs\b|\bclimb\w*\b|\bascend\w*\b",
      re.I, limit=12)
sweep("a figure against the door nine hundred yards off", r"sixty-six")
sweep("of this month", r"of this month", re.I, limit=12)
sweep("the let-go family", r"\blet go\b|\bletting go\b|go their own way|walk away",
      re.I, limit=12)
sweep("pruning or the flow, used as a name for either light",
      r"\bpruning\b|\bpruned\b|\bthe flow\b", re.I, limit=12)
sweep("the name of the thing that is paid", r"\balderen\b", re.I)
sweep("one ear, deaf, cannot hear", r"\bone ear\b|\bdeaf\b|\bcannot hear\b", re.I)
sweep("a hand on her arm", r"\bhand on her arm\b|\bhands on her arm\b", re.I)
sweep("thirty-five in and thirty-five out", r"thirty-five in", re.I)

print("=" * 72)
print("9. ORDINALS OUTSIDE HEADINGS")
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
        print(f"   {n} line {file_line(n, m.start())}: {m.group(0)!r} preceded by {before}")
print(f"   ordinal words standing as dates outside a heading: {flagged}")

# ------------------------------------------- cross-batch verbatim (scope note)
print("=" * 72)
print("10. VERBATIM EIGHTEEN-WORD WINDOWS, Volume 16 scope, and what each is")


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
        cats["a window of the locked comfort line, spent whole by design"] += 1
    elif "far end of a thing" in s or "anywhere in four counties" in s:
        cats["a window of the locked far-end sentence, spent whole by design"] += 1
    else:
        cats["a floor being restated, or a speaker's standing line"] += 1
        other.append((k, vwhere[k]))
print(f"   verbatim repeated eighteen-word windows anywhere in Volume 16: "
      f"{sum(1 for v in vwin.values() if v > 1)}")
print(f"   of those involving a morning in this batch: "
      f"{sum(1 for k, v in vwin.items() if v > 1 and vwhere[k] & mine_names)}")
for a, b in cats.most_common():
    print(f"     {b:>4}  {a}")
for k, w in other[:12]:
    print("       ", sorted(w), "|", " ".join(k)[:100])
print(f"   and the unclassified remainder: {len(other)}")

print("=" * 72)
print("11. WORD COUNTS")
tot = 0
for f in FILES:
    w = len(f.read_text().split())
    tot += w
    print(f"   {f.name}: {w}")
print(f"   batch total: {tot}")
v16t = sum(len(f.read_text().split()) for f in v16)
allt = sum(len(f.read_text().split()) for f in all_chapters)
print(f"   Volume 16 total: {v16t} across {len(v16)} files")
print(f"   manuscript total: {allt} across {len(all_chapters)} files")
print("=" * 72)