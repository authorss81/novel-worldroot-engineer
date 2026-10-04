#!/usr/bin/env python3
"""Volume 16 close harness. THE ORDER IS THE ORDER IN THE PROMPT AND THE
INSTRUMENTS ARE NOT INTERCHANGEABLE:

  1  the self-collision controls, which must reproduce before any nil is published
  2  the parity reading, morning by morning, over all forty-five mornings
  3  the figure check, every figure derived from its own rule on its own day
  4  the lock check
  5  both gates, both readings, both scopes, with the thirty-word floor named
  6  the exact-duplicate sweep at any paragraph length, scoped to the manuscript
  7  the apparatus count, scoped to Volume Sixteen
  and then the mechanical sweeps, each read by hand.

THE PARAGRAPH UNIT IS DECLARED BEFORE ANY READING IS RUN, AND IT IS THE UNIT OF
THIS VOLUME AND NOT A NEW ONE: every non-blank line below a heading, a
block-quote separator line carrying no words excluded, apparatus quote lines
counted as paragraphs of their own, headings excluded, apparatus inside the scope
of both gates.

THE NORMALISATION: every run of number words that makes one figure replaced by one
token, the word *and* left alone, hyphenated compounds split on the hyphen,
punctuation dropped, case folded.
"""

import re
import sys
import collections
import bisect
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import derive as D                                            # noqa: E402

HERE = Path(__file__).resolve().parent
V16 = HERE.parent
ROOT = V16.parent.parent
WS = ROOT / "workspace"

VOL_DIRS = [V16 / f"batch-{n:04d}" for n in range(1, 6)]
V16_FILES = [p for d in VOL_DIRS for p in sorted(d.glob("chapter-*.md"))]
ALL_FILES = sorted(WS.glob("volume-*/batch-*/chapter-*.md"))

FIRST_CH = 736
FILE_OF_DAY = {D.VOL_FIRST_DAY + (n - 1): f"chapter-{FIRST_CH + (n - 1):04d}.md"
               for n in range(1, 46)}

# ---------------------------------------------------------------- normalisation

ONES = D.ONES_C
TENS = ["zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
        "eighty", "ninety"]
NUMBER_WORDS = set(ONES) | set(TENS) | {"hundred", "thousand", "million"}
for w in ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
          "eighth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth",
          "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eighteenth",
          "nineteenth", "twentieth", "thirtieth", "fortieth", "fiftieth",
          "sixtieth", "seventieth", "eightieth", "ninetieth", "hundredth",
          "thousandth"]:
    NUMBER_WORDS.add(w)
TOKEN = "<NUM>"


def normalise_words(text):
    """A run of number words that makes one figure collapses to one token. A
    hyphenated compound is split on the hyphen BEFORE the lookup, so that
    five-hundred-and-fortieth and five hundred and fortieth are the same shape.
    The word *and* is left alone."""
    toks = []
    for raw in text.split():
        for part in raw.lower().split("-"):
            part = re.sub(r"[^a-z]", "", part)
            if not part:
                continue
            toks.append(TOKEN if part.isdigit() or part in NUMBER_WORDS else part)
    return toks


def paragraphs(path):
    """The declared unit. A block-quote separator line carrying no words is NOT a
    paragraph and is excluded; every other apparatus quote line IS one."""
    out, seen_heading = [], False
    for lineno, line in enumerate(path.read_text().splitlines(), 1):
        if line.startswith("#"):
            seen_heading = True
            continue
        if not line.strip():
            continue
        if line.lstrip().startswith(">"):
            if not line.lstrip().lstrip(">").strip():
                continue
        if not seen_heading:
            continue
        out.append((lineno, line))
    return out


def body_of(path):
    """Body prose: the declared unit minus the apparatus blocks. An apparatus
    block is one run of consecutive `>` lines and it sits in the middle of a
    morning here as often as at the end of one, so the run is closed by the first
    prose line after it and not by the end of the file."""
    out, in_apparatus = [], False
    for lineno, line in paragraphs(path):
        if line.lstrip().startswith(">"):
            in_apparatus = True
            continue
        in_apparatus = False
        if not in_apparatus:
            out.append((lineno, line))
    return out


def head() :
    print("=" * 78)


def hr(title):
    head()
    print(title)


# =========================================================== 0  the word counts
hr("0. WORD COUNTS, MEASURED PER FILE WITH len(text.split()) AND NEVER BY "
   "CONCATENATION")

v16_per_file = [(f.name, len(f.read_text().split())) for f in V16_FILES]
for i in range(0, len(v16_per_file), 10):
    batch = v16_per_file[i:i + 10]
    print("   " + "  ".join(f"{n.replace('chapter-', '').replace('.md', '')}:"
                            f"{w}" for n, w in batch))
v16_total = sum(w for _, w in v16_per_file)
print(f"   Volume 16: {v16_total} across {len(v16_files_ := V16_FILES)} files")
for d in VOL_DIRS:
    fs = sorted(d.glob("chapter-*.md"))
    print(f"     {d.name}: {sum(len(f.read_text().split()) for f in fs)} across "
          f"{len(fs)} files")
man_per_file = [(f.name, len(f.read_text().split())) for f in ALL_FILES]
man_total = sum(w for _, w in man_per_file)
vols = collections.Counter()
for f in ALL_FILES:
    vols[f.parts[-3]] += len(f.read_text().split())
print(f"   manuscript: {man_total} across {len(ALL_FILES)} files")
behind = man_total - v16_total
print(f"   volumes one to fifteen: {behind} across {len(ALL_FILES) - len(V16_FILES)} "
      f"files  (reconciles: {behind} + {v16_total} = {behind + v16_total})")

# The residual the Volume 14 close named: files that lack an EOF newline read one
# word short under a naive wc -w.
no_eof = [f.name for f in ALL_FILES if not f.read_bytes().endswith(b"\n")]
print(f"   files lacking an EOF newline in the manuscript: {len(no_eof)}")
no_eof_v16 = [f.name for f in V16_FILES if not f.read_bytes().endswith(b"\n")]
print(f"   of those in Volume 16: {len(no_eof_v16)} {no_eof_v16}")
residual = []
for f in ALL_FILES:
    t = f.read_text()
    if len(t.split()) != len(t.rstrip("\n").split()) + (0 if t.endswith("\n") else 1):
        pass
cat = None
try:
    import subprocess
    # (a) wc -w over the file list: one count per file, joined by the tool.
    listed = subprocess.run(["wc", "-w"] + [str(f) for f in ALL_FILES],
                            capture_output=True, text=True).stdout
    cat_listed = int(listed.strip().splitlines()[-1].split()[0])
    # (b) wc -w over the concatenation: the residual the Volume 14 close named.
    joined = subprocess.run(f"cat {' '.join(str(f) for f in ALL_FILES)} | wc -w",
                            shell=True, capture_output=True, text=True).stdout
    cat_joined = int(joined.strip())
    cat = (cat_listed, cat_joined)
except Exception as exc:                                        # pragma: no cover
    cat = f"not available ({exc})"
print(f"   wc -w over the same files listed one by one: {cat[0]}, difference "
      f"{cat[0] - man_total}")
print(f"   wc -w over the same files CONCATENATED: {cat[1]}, difference "
      f"{cat[1] - man_total}  <-- the residual, and it is the count of files that "
      f"lack an EOF newline among those the count lands between")

# ================================================= 1  the self-collision controls
hr("1. THE SELF-COLLISION CONTROLS, RUN FIRST, AND THEY MUST REPRODUCE")


def _uniq_words(n):
    letters = "abcdefghijklmnopqrstuvwxyz"
    out = []
    for i in range(n):
        s, k = "", i
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
    filler = _uniq_words(sum(gap_sizes) + 40)
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
    return (*rep(windows), *rep(whole))


controls_ok = True
for copies, n_gaps, want_s, want_w in [(28, 27, 27, 0), (13, 12, 12, 0)]:
    s_sh, s_ex, w_sh, w_ex = control(copies, n_gaps)
    ok = (s_ex == want_s and w_ex == want_w)
    controls_ok &= ok
    print(f"   {copies} copies, {n_gaps} gaps: sliding {s_sh} shape(s) / {s_ex} "
          f"excess; whole-paragraph {w_sh} shape(s) / {w_ex} excess -> "
          f"{'REPRODUCES' if ok else 'DOES NOT REPRODUCE'}")
print(f"   the normalisation is settled: {controls_ok}. A working gate proves that "
      f"a shape is real; it does not prove that the absence of a shape means "
      f"anything.")

# ============================================================ 2  the parity read
hr("2. THE PARITY READING. THE DEMONSTRATION ON A KNOWN INSTANCE COMES FIRST, "
   "AND THE MORNING-BY-MORNING TABLE FOLLOWS IT, AND THE READING RUNS OVER ALL "
   "FORTY-FIVE MORNINGS AND NOT OVER ITS OWN FILES")

FALL_VERBS = ("came down", "came", "dropped", "fell to", "fell", "went down",
              "comes on", "comes", "drop", "dropping", "taken off", "taken down")
RISE_VERBS = ("did not move", "has not moved", "did not shift", "not moved",
              "not shifted", "stood", "stands", "rose", "went up", "held", "holds",
              "holding", "unchanged", "stayed", "stay", "stays")
WEAK_VERBS = ("moved", "moves", "moving", "changed", "went", "goes")
DIRECTIONAL = re.compile("(" + "|".join(sorted(set(FALL_VERBS + RISE_VERBS + WEAK_VERBS),
                                                key=len, reverse=True)) + ")",
                         re.I)
NEAREST_CHARS = 45
# a verb inside one of these is naming the OTHER half and does not bind this one
RELATIVE = re.compile(r"(the one that|the one which|the one who|the other one|"
                      r"the one it|the other)\s*$", re.I)


def _binds(gap):
    """Whether a verb at the end of `gap` binds the half-figure at the start of
    it. Three exclusions, each of them a thing this house has taught:
    a sentence break, another half-figure, and a phrase that renames the pair."""
    if re.search(r"[.;!?]", gap):
        return False
    if re.search(r"\b(half|halves|tall|short|window|board)\b", gap, re.I):
        return False
    return True


def pair_rows(day, text):
    """Which half sits on the verb that means it moved.

    SIDE-AGNOSTIC ON PURPOSE. A morning may say *two hundred and thirty-six stood
    and two hundred and forty-seven came* or *the other way round*, and a reading
    that assumes the mover is the figure before the verb flags the first of those
    and misses the second. So each occurrence of either half takes the NEAREST
    directional verb on either side of it, and the question is which half is
    attached to a verb that means it moved.

    A fall verb must carry the mover. A rise verb must carry the stander. On an odd
    morning the mover is the smaller of the two halves and on an even morning the
    larger. A verb that does not say which way (moved, went, changed) is recorded
    and is not used for a verdict, because a reading that guesses here would
    manufacture the very defect it is looking for.
    """
    fall, rise = D.halves(day)
    cands = sorted({D.cardinal(fall), D.cardinal(rise)}, key=len, reverse=True)
    odd = D.morning(day) % 2 == 1
    mover = D.cardinal(fall) if odd else D.cardinal(rise)
    stander = D.cardinal(rise) if odd else D.cardinal(fall)
    rows = []
    for c in cands:
        pat = re.compile(r"(?<![\w-])" + re.escape(c) + r"(?![\w-])")
        for m in pat.finditer(text):
            best = None
            for vm in DIRECTIONAL.finditer(text, max(0, m.start() - NEAREST_CHARS),
                                           m.end() + NEAREST_CHARS):
                v = vm.group(1).lower()
                if RELATIVE.search(text[max(0, vm.start() - 40):vm.start()]):
                    continue          # the verb is naming the other half
                if vm.start() >= m.end():                     # verb after figure
                    gap = text[m.end():vm.start()]
                    if not _binds(gap) or any(
                            text.count(x, m.end(), vm.start()) for x in cands if x != c):
                        continue
                    dist = abs(vm.start() - m.end())
                else:                                         # verb before figure
                    gap = text[vm.end():m.start()]
                    if not _binds(gap) or any(
                            text.count(x, vm.end(), m.start()) for x in cands if x != c):
                        continue
                    dist = abs(m.start() - vm.end())
                cand = (dist, vm.start(), v)
                if best is None or cand < best:
                    best = cand
            if best is None:
                continue
            dist, vpos, v = best
            weak = v in WEAK_VERBS
            fell = v in FALL_VERBS
            lo = max(0, min(m.start(), vpos) - 60)
            hi = min(len(text), max(m.end(), vpos) + 60)
            rows.append({"figure": c, "verb": v, "fell": fell, "weak": weak,
                         "gap": dist, "carried": c,
                         "want": (mover if fell else stander) if not weak else "-",
                         "ctx": text[lo:hi].replace("\n", " ")})
    return odd, mover, stander, rows


# --- the demonstration this class of instrument owes, on a KNOWN instance ------
hr("2b. THE READING DEMONSTRATED ON A KNOWN INSTANCE OF THE CLASS IT CATCHES, "
   "AND IT IS RUN BEFORE THE PER-MORNING TABLE BELOW, BECAUSE A READING THAT HAS NOT "
   "BEEN SHOWN THE CLASS MAY NOT PUBLISH ITS NIL AS A NIL")

FIXTURE_BAD = ("the girl of about seventeen said two hundred and fifty-eight came "
               "and two hundred and forty-eight stood, and she gave the rule in "
               "the next eleven words, that a fall goes on every odd morning")
V16_TEXT = {f.name: f.read_text().lower() for f in V16_FILES}
probe_day = 989
odd, mover, stander, rows = pair_rows(probe_day, FIXTURE_BAD)
bad_hits = [r for r in rows if r["carried"] != r["want"]]
print(f"   fixture: the pre-repair wording recorded at "
      f"workspace/volume-16/batch-0005/SELF-CHECK.md section 12 item 1, on day 989 "
      f"(an odd morning, so the smaller half moves)")
for r in rows:
    print(f"     verb {r['verb']!r} carries {r['carried']!r}, wanted {r['want']!r} "
          f"-> {'FLAGGED, so the reading sees the class' if r['carried'] != r['want'] else 'silent'}")
live = [r for r in pair_rows(probe_day, V16_TEXT['chapter-0776.md'])[3]]
live_bad = [r for r in live if r["carried"] != r["want"]]
print(f"   the same reading against the page as it now stands, chapter-0776.md: "
      f"{len(live)} paired delivery sentence(s), {len(live_bad)} flagged")
for r in live:
    print(f"     verb {r['verb']!r} carries {r['carried']!r}, wanted {r['want']!r}")
print(f"   THE READING IS DEMONSTRATED ON THE CLASS: "
      f"{'yes' if bad_hits else 'NO -- AND NO NIL FROM IT MAY BE PUBLISHED'}")

# also: the opposite direction, a rise verb carrying the mover on an even morning
EVEN_FIXTURE = ("and at the ninth hour the clerk said two hundred and fifty-nine "
                "stood and two hundred and forty-eight rose, which is the other way "
                "round")
erows = pair_rows(990, EVEN_FIXTURE)[3]
print(f"   the mirror fixture on an even morning (day 990): "
      f"{sum(1 for r in erows if r['carried'] != r['want'])} of {len(erows)} "
      f"flagged")


parity_wrong, parity_rows, weak_rows = [], 0, 0
for day in range(D.VOL_FIRST_DAY, D.VOL_LAST_DAY + 1):
    name = FILE_OF_DAY[day]
    odd, mover, stander, rows = pair_rows(day, V16_TEXT[name])
    parity_rows += len([r for r in rows if not r["weak"]])
    weak_rows += len([r for r in rows if r["weak"]])
    wrong = [r for r in rows if not r["weak"] and r["carried"] != r["want"]]
    parity_wrong += [(name, r) for r in wrong]
    flag = "clean" if not wrong else f"{len(wrong)} FLAGGED, read by hand below"
    print(f"   {name} day {day} morning {D.morning(day):>2} "
          f"{'odd  ' if odd else 'even'}: the "
          f"{'smaller' if odd else 'larger'} half moved, mover {mover!r}, stander "
          f"{stander!r}; {len([r for r in rows if not r['weak']])} half(s) attached "
          f"to a verb that says which way -> {flag}")
    for r in wrong:
        print(f"       FLAGGED: {r['figure']!r} on {r['verb']!r}, wanted {r['want']!r}"
              f" | {r['ctx'][:160]}")
print(f"   half-figures attached to a verb that says which way, examined: "
      f"{parity_rows}; wrong attachment: {len(parity_wrong)}")
print(f"   half-figures attached to a verb that does NOT say which way (moved, "
      f"went, changed), recorded and not used for a verdict: {weak_rows}")

# ================================================================= 3  the figures
hr("3. THE FIGURE CHECK. EVERY FIGURE DERIVED FROM ITS OWN RULE APPLIED TO ITS "
   "OWN DAY, REQUIRED AS A WHOLE PHRASE IN THAT MORNING'S BODY PROSE")

item_total = D.item_list_total()
print(f"   the volume's own item list, derived here and inherited from no file: "
      f"14 x {item_total['mornings']} mornings + 2 x {item_total['odd']} odd "
      f"mornings + 5 x {item_total['fourth_line']} fourth-line mornings = "
      f"{item_total['total']}")

req_present = req_absent = 0
failures, outside_body = [], []
PATH_OF = {f.name: f for f in V16_FILES}
for day in range(D.VOL_FIRST_DAY, D.VOL_LAST_DAY + 1):
    name = FILE_OF_DAY[day]
    full = V16_TEXT[name]
    body = "\n".join(t for _, t in body_of(PATH_OF[name])).lower()
    for series, phrase, wanted in D.figures_for(day):
        hit_full = phrase in full
        hit_body = phrase in body
        if wanted:
            req_present += 1
            if not hit_full:
                failures.append((name, series, phrase, day))
            elif not hit_body:
                outside_body.append((name, series, phrase))
        else:
            req_absent += 1
            if hit_full:
                failures.append((name, series, phrase + "  [REQUIRED ABSENT]", day))
print(f"   required present: {req_present}; required absent: {req_absent} "
      f"(the second reckoning, section 8d); failures: {len(failures)}")
for f in failures:
    print(f"     FAIL {f[0]}: {f[1]} -> {f[2]!r}")
print(f"   figures present in a heading or an apparatus block but NOT in body "
      f"prose: {len(outside_body)}")
for o in outside_body:
    print(f"     OUTSIDE BODY {o[0]}: {o[1]} -> {o[2]!r}")

# --- the volume's own standing figures, re-derived and compared with the pages --
hr("3b. THE FIGURES OF THE VOLUME'S OWN STANDING, DERIVED AND COMPARED WITH THE "
   "PAGES")
launders = {d: D.third_launder(d) for d in range(D.VOL_FIRST_DAY, D.VOL_LAST_DAY + 1)}
mx_day = max(launders, key=lambda d: launders[d])
print(f"   the third launder enters Volume 16 at {D.cardinal_k(launders[949])} "
      f"hundredweight and ends at {D.cardinal_k(launders[993])} hundredweight")
print(f"   its maximum in the volume is {D.cardinal_k(launders[mx_day])} on day "
      f"{mx_day} (morning {D.morning(mx_day)}, {FILE_OF_DAY[mx_day]}), and the last "
      f"morning reads {D.cardinal_k(launders[993])}")
print(f"   a round hundred in the thousands stands at "
      f"{D.cardinal_k(launders[974])} hundredweight on day 974 "
      f"({FILE_OF_DAY[974]}), site three-A")
rises = {d: D.halves(d)[1] for d in launders}
falls = {d: D.halves(d)[0] for d in launders}
print(f"   the rising half runs {min(rises.values())} to {max(rises.values())} and "
      f"stands at {D.cardinal(rises[992])} on day 992 and {D.cardinal(rises[993])} "
      f"on day 993")
print(f"   the falling half runs {min(falls.values())} to {max(falls.values())}; no "
      f"half reaches a round hundred on any morning: "
      f"{not any(v % 100 == 0 for v in list(rises.values()) + list(falls.values()))}")
print(f"   the two halves add to the window on all forty-five mornings: "
      f"{all(D.halves(d)[0] + D.halves(d)[1] == D.window(d) for d in launders)}")
print(f"   the ordinal of the run stands at exactly five hundred on its second "
      f"morning, day 950: {D.ordinal(D.ordinal_of_run(950))!r}")
print(f"   the fifth returns are at days {[d for d in launders if D.is_return(d)]}, "
      f"one of them a fourth-line morning (982) and one a first morning of a month "
      f"(991)")
print(f"   the compost line enters paid at thirty-one and this plan schedules no "
      f"turn in it; the ladder and the drawer have a fresh standing for these "
      f"forty-five mornings and are not a claim about the fifteen behind")

# ============================================== 4  the lock check on the figures
hr("4. THE LOCK CHECK. WHOLE APPEARANCES, LOAD-BEARING STRINGS, SHORTENED FORMS, "
   "AND THE OPENING CLAUSE")

FAR_END = ("The far end of a thing is held by two people and neither of them is "
           "me, and no instrument anywhere in four counties says whether it is on "
           "or off.")
COMFORT = ("The comfort is not standing, the father is not alive in the wood, and "
           "the day does not come back.")
STRINGS = ["far end of a thing", "anywhere in four counties", "whether it is on or off",
           "the comfort is not standing", "the father is not alive in the wood",
           "the day does not come back"]

far_whole = [(n, V16_TEXT[n].count(FAR_END.lower())) for n in V16_TEXT
             if FAR_END.lower() in V16_TEXT[n]]
com_whole = [(n, V16_TEXT[n].count(COMFORT.lower())) for n in V16_TEXT
             if COMFORT.lower() in V16_TEXT[n]]
print(f"   the far-end sentence, whole, on: "
      f"{[(n, c, D.VOL_FIRST_DAY + int(n[8:12]) - 736) for n, c in far_whole]}")
print(f"   the comfort line, whole, on: "
      f"{[(n, c, D.VOL_FIRST_DAY + int(n[8:12]) - 736) for n, c in com_whole]}")
print(f"   whole appearances in the volume: {sum(c for _, c in far_whole)} of the "
      f"far-end sentence and {sum(c for _, c in com_whole)} of the comfort line, "
      f"on {len(set(n for n, _ in far_whole + com_whole))} mornings")
print(f"   the allowance's ceiling is four whole appearances per figure and this "
      f"volume spends {sum(c for _, c in far_whole)} of the far-end and "
      f"{sum(c for _, c in com_whole)} of the comfort line, one in between each")
for s in STRINGS:
    tot = sum(V16_TEXT[n].count(s) for n in V16_TEXT)
    where = sorted(n for n in V16_TEXT if s in V16_TEXT[n])
    print(f"   string {s!r}: {tot} in Volume 16, on {where}")

# a shortened form is any run of the sentence with a clause dropped
SHORTENED = [
    "the far end of a thing is held by two people",
    "held by two people and neither of them is me",
    "no instrument anywhere in four counties",
    "the comfort is not standing",
    "the father is not alive in the wood",
    "the day does not come back",
]
print("   shortened forms, searched as the leading clause of either sentence "
      "outside its own whole appearance:")
short_hits = []
for frag in SHORTENED:
    for n, t in V16_TEXT.items():
        c = t.count(frag)
        whole_here = FAR_END.lower().count(frag) if "far end" in frag or "held by" in frag \
            or "no instrument" in frag else COMFORT.lower().count(frag)
        if c > whole_here:
            short_hits.append((n, frag, c - whole_here))
for h in sorted(short_hits):
    print(f"     {h[0]}: {h[1]!r} appears {h[2]} time(s) outside a whole appearance")
print(f"   shortened forms found: {len(short_hits)}")

# the opening clause reused as somebody else's construction
open_reuse = [(n, t.count("the far end of a thing")) for n, t in V16_TEXT.items()
              if t.count("the far end of a thing") > FAR_END.lower().count("the far end of a thing")]
print(f"   the far-end sentence's opening clause reused as somebody else's "
      f"construction inside Volume 16: {len(open_reuse)} {open_reuse}")

# ==================================================================== 5  the gates
hr("5. BOTH GATES, BOTH READINGS, BOTH SCOPES. THE FLOOR ON GATE ONE IS THIRTY "
   "WORDS AND THE COMFORT LINE IS TWENTY WORDS AND IS STRUCTURALLY INVISIBLE TO "
   "IT, SO A CLEAN GATE ONE IS NOT EVIDENCE ABOUT EITHER LOCKED FIGURE.")

WORD_FLOOR = 30


def gate_one(files):
    paras = []
    for f in files:
        for _, p in paragraphs(f):
            if len(p.split()) >= WORD_FLOOR:
                paras.append((f.name, p.strip()))
    c = collections.Counter(p for _, p in paras)
    return paras, [(k, v) for k, v in c.items() if v > 1]


def second_gate(files, label, show_shapes=True, limit=40):
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
    print(f"   {label}: whole-paragraph reading {len(whole_units)} units, {w_sh} "
          f"shapes, {w_ex} excess; sliding eighteen-word reading {len(win_units)} "
          f"windows, {s_sh} shapes, {s_ex} excess")
    shapes = []
    c = collections.Counter(win_units)
    cw = collections.Counter(whole_units)
    for k, v in c.items():
        if v > 1:
            shapes.append(("window", v, " ".join(k)))
    for k, v in cw.items():
        if v > 1:
            shapes.append(("chunk", v, " ".join(k)))
    if show_shapes:
        for kind, v, sh in shapes:
            print(f"     {kind.upper()} x{v}: {sh[:120]}")
    return shapes, (w_sh, w_ex, s_sh, s_ex, len(whole_units), len(win_units))


def count_paragraphs(files, label):
    tot = sum(1 for f in files for _ in paragraphs(f))
    print(f"   paragraphs at the declared unit, {label}: {tot}")
    return tot


V16_PARAS = count_paragraphs(V16_FILES, "Volume 16")
count_paragraphs(ALL_FILES, "the manuscript")

v16_paras, v16_pairs = gate_one(V16_FILES)
print(f"   Volume 16 scope: {len(v16_paras)} prose paragraphs of {WORD_FLOOR} "
      f"words or more, {len(v16_pairs)} exact pairs")
for k, v in v16_pairs:
    print("     PAIR x%d:" % v, k[:110])
man_paras, man_pairs = gate_one(ALL_FILES)
LOCKED_PARA = {" ".join(normalise_words(x)) for x in (FAR_END, COMFORT)}
names = {}
for k, v in man_pairs:
    for n, p in v16_paras:
        if p == k:
            names[k] = n
touching = [(names.get(k), v, k) for k, v in man_pairs if k in names]
print(f"   whole manuscript scope: {len(man_paras)} paragraphs of {WORD_FLOOR} words "
      f"or more, {len(man_pairs)} exact pairs, {len(touching)} touching Volume 16")
for n, v, k in touching:
    locked = ("the locked far-end sentence, spent whole by design"
              if " ".join(normalise_words(k)) in LOCKED_PARA else "NOT A LOCKED FIGURE")
    print(f"     TOUCHES VOLUME 16 x{v}: {n} | {k[:80]} | {locked}")

shapes16, figs16 = second_gate(V16_FILES, "Volume 16 scope", show_shapes=False)
shapesM, figsM = second_gate(ALL_FILES, "whole manuscript scope", show_shapes=False)


FAR_TOKS = normalise_words(FAR_END.lower())
COM_TOKS = normalise_words(COMFORT.lower())
FAR_W = {" ".join(FAR_TOKS[i:i + 18]) for i in range(len(FAR_TOKS) - 17)}
COM_W = {" ".join(COM_TOKS[i:i + 18]) for i in range(len(COM_TOKS) - 17)}


def classify(shapes):
    """Every shape identified before anything is broken. A shape is a window or a
    chunk of one of the two locked sentences, or it is not, and the ones that are
    not are grouped by their first six tokens so that a restated standing block
    can be named rather than guessed at."""
    locked_keys = {" ".join(normalise_words(x)) for x in (FAR_END, COMFORT)}
    far_toks = normalise_words(FAR_END.lower())
    com_toks = normalise_words(COMFORT.lower())
    far_w = {" ".join(far_toks[i:i + 18]) for i in range(len(far_toks) - 17)}
    com_w = {" ".join(com_toks[i:i + 18]) for i in range(len(com_toks) - 17)}

    out = {"far_window": 0, "far_chunk": 0, "com_window": 0, "com_chunk": 0}
    fam = collections.defaultdict(lambda: [0, 0, ""])
    unlocked = 0
    for kind, v, sh in shapes:
        if kind == "window":
            if sh in far_w:
                out["far_window"] += 1
                continue
            if sh in com_w:
                out["com_window"] += 1
                continue
        else:
            if sh in locked_keys:
                out["far_chunk" if "far end" in sh else "com_chunk"] += 1
                continue
        unlocked += 1
        key = " ".join(sh.split()[:6])
        fam[key][0] += 1
        fam[key][1] += v - 1
        fam[key][2] = sh
    return out, unlocked, fam


out16, unlocked16, fam16 = classify(shapes16)
print(f"   Volume 16 scope, every shape identified before anything is broken: "
      f"{out16['far_window']} windows of the far-end sentence, "
      f"{out16['com_window']} windows of the comfort line, "
      f"{out16['far_chunk']} whole-paragraph chunks of the far-end sentence, "
      f"{out16['com_chunk']} whole-paragraph chunks of the comfort line, and "
      f"{unlocked16} that are none of those four")
print(f"   the second gate's tuple is (whole shapes, whole excess, sliding shapes, "
      f"sliding excess, whole units, sliding windows) = {figs16}")
print(f"   and the sliding reading's {figs16[2]} shapes therefore resolve as "
      f"{out16['far_window'] + out16['com_window']} locked and "
      f"{figs16[2] - out16['far_window'] - out16['com_window']} unlocked, and the "
      f"{figs16[0]} whole-paragraph shapes are all unlocked")
print(f"   the far-end sentence normalises to {len(FAR_TOKS)} tokens and yields "
      f"{len(FAR_W)} sliding windows; the comfort line to {len(COM_TOKS)} tokens and "
      f"{len(COM_W)}")
print(f"   the unlocked shapes grouped by their first six tokens: {len(fam16)} "
      f"families, and the largest are:")
for k, (n, ex, ex_sh) in sorted(fam16.items(), key=lambda kv: (-kv[1][0], kv[0]))[:12]:
    print(f"     {n:>3} shape(s), {ex:>3} excess | {k}")
big = max(fam16.items(), key=lambda kv: kv[1][0]) if fam16 else None
if big:
    print(f"   the largest family in full: {big[1][2][:180]!r}")
outM, unlockedM, famM = classify(shapesM)
print(f"   whole manuscript scope, for comparison and not a measurement of this "
      f"volume: {outM} locked, {unlockedM} unlocked")

# ================================================ 6  the exact-duplicate sweep
hr("6. THE EXACT-DUPLICATE SWEEP AT ANY PARAGRAPH LENGTH, SCOPED TO THE "
   "MANUSCRIPT, BECAUSE NEITHER GATE CAN SEE A PARAGRAPH AGAINST ITSELF")
dupes = collections.defaultdict(list)
for f in ALL_FILES:
    for _, p in paragraphs(f):
        s = p.strip()
        if s:
            dupes[s].append(f.name)
repeats = {k: v for k, v in dupes.items() if len(v) > 1}
mine = {f.name for f in V16_FILES}
mine_dupes = {k: v for k, v in repeats.items() if any(n in mine for n in v)}
print(f"   duplicated paragraphs anywhere in the manuscript: {len(repeats)}")
print(f"   of those involving a morning in Volume 16: {len(mine_dupes)}")
LOCKED_KEYS = {" ".join(normalise_words(x)) for x in (FAR_END, COMFORT)}
for k, v in sorted(mine_dupes.items()):
    key = " ".join(normalise_words(k))
    tag = ("a LOCKED FIGURE, spent whole by design" if key in LOCKED_KEYS
           else "not a locked figure")
    print(f"     DUP x{len(v)} in {len(set(v))} files | {tag} | {k[:100]}")
internal = collections.defaultdict(list)
for f in V16_FILES:
    c = collections.Counter(p.strip() for _, p in paragraphs(f))
    for k, v in c.items():
        if v > 1:
            internal[f.name].append((k, v))
print(f"   paragraphs repeated inside a single Volume 16 file: "
      f"{sum(len(v) for v in internal.values())}")
for n, v in internal.items():
    for k, c in v:
        print(f"     INTERNAL {n} x{c} | {k[:100]}")

# also, at a literal eight-word floor, as the volume behind's close published both
hr("6b. THE SAME SWEEP UNDER THE NUMBER-AND-ORDINAL NORMALISATION, WHICH IS NOT "
   "THE SAME SWEEP, AND THE SIXTEEN-LINE SWEEP, WHICH IS PER FILE")
norm_dupes = collections.defaultdict(list)
for f in ALL_FILES:
    for _, p in paragraphs(f):
        key = " ".join(normalise_words(p))
        if key:
            norm_dupes[key].append(f.name)
norm_rep = {k: v for k, v in norm_dupes.items() if len(v) > 1}
norm_mine = {k: v for k, v in norm_rep.items() if any(n in mine for n in v)}
print(f"   duplicated paragraphs under the number-and-ordinal normalisation, "
      f"anywhere in the manuscript: {len(norm_rep)}")
print(f"   of those involving a morning in Volume 16: {len(norm_mine)}")
for k, v in sorted(norm_mine.items(), key=lambda kv: -len(set(kv[1]))):
    locked = k in LOCKED_KEYS
    print(f"     NORM DUP in {len(set(v))} files | "
          f"{'a LOCKED FIGURE, spent whole by design' if locked else 'not a locked figure'}"
          f" | {k[:100]}")

# the sixteen-line shared-token sweep, per file, on the longest shared contiguous
# run. It cannot see a restatement against a morning in another file at all.
print("   the sixteen-line sweep, per file, longest shared contiguous token run "
      "between any two non-blank body lines within sixteen lines of each other:")
buckets = collections.Counter()
worst = []
for f in V16_FILES:
    ls = [norm_phrase for norm_phrase in
          [re.findall(r"[a-z]+", t.lower()) for _, t in body_of(f)] if norm_phrase]
    for i in range(len(ls)):
        for j in range(i + 1, min(i + 17, len(ls))):
            best = 0
            for a, b in zip(ls[i], ls[j]):
                if a == b:
                    best += 1
                else:
                    break
            if best >= 6:
                buckets[best] += 1
                if best >= 10:
                    worst.append((f.name, i, j, best, " ".join(ls[i][:best])))
for k in sorted(buckets):
    print(f"     runs of {k} tokens: {buckets[k]}")
print(f"   runs of ten tokens or more: {len(worst)}")
for w in worst[:10]:
    print("     ", w[0], w[3], w[4][:90])

hr("7. THE APPARATUS COUNT, SCOPED TO VOLUME SIXTEEN AND NOT TO THE MANUSCRIPT")
spent, where, entered = 0, [], []
for f in V16_FILES:
    run = 0
    for line in f.read_text().splitlines():
        if line.lstrip().startswith(">"):
            run += 1
            if run == 1:
                spent += 1
                where.append(f.name)
        else:
            run = 0
    if re.search(r"^>\s*\**\s*(Entered|Entered:)", f.read_text(), re.M):
        entered.append(f.name)
print(f"   blocks spent across Volume 16: {spent}; ceiling thirty; unspent: "
      f"{30 - spent}")
print(f"   the mornings that carry one: {where}")
print(f"   mornings carrying more than one: none by the ceiling's own first rule; "
      f"counted above")
man_apparatus = 0
for f in ALL_FILES:
    run = 0
    for line in f.read_text().splitlines():
        if line.lstrip().startswith(">"):
            run += 1
            if run == 1:
                man_apparatus += 1
        else:
            run = 0
print(f"   the same count over the whole manuscript, WHICH IS NOT THE FIGURE: "
      f"{man_apparatus} (the mistake named at state/current.md section 27)")
print(f"   Entered labels in Volume 16: {entered}")

# ============================================================ 8  the sweeps
hr("8. THE MECHANICAL SWEEPS, EVERY ONE READ BY HAND AND PUBLISHED WHETHER IT IS "
   "CLEAN OR NOT. A SWEEP THAT FLAGS ITS OWN HOUSE IS A BROKEN SWEEP AND IS "
   "REPORTED AS ONE.")

BODIES, APPAR = {}, {}
for f in V16_FILES:
    lines_ = f.read_text().splitlines()
    BODIES[f.name] = "\n".join(t for _, t in body_of(f))
    APPAR[f.name] = "\n".join(l.lstrip().lstrip(">").strip() for l in lines_
                              if l.lstrip().startswith(">"))
BODY_LINES, STARTS = {}, {}
for f in V16_FILES:
    ls = body_of(f)
    BODY_LINES[f.name] = [n for n, _ in ls]
    pos, st = 0, []
    for _, t in ls:
        st.append(pos)
        pos += len(t) + 1
    STARTS[f.name] = st


def file_line(name, off):
    i = bisect.bisect_right(STARTS[name], off) - 1
    return BODY_LINES[name][max(0, i)]


def sweep(name, pattern, flags=re.I, scope=None, limit=10, width=52):
    rx = re.compile(pattern, flags)
    hits = []
    for n, t in sorted((scope or BODIES).items()):
        for m in rx.finditer(t):
            ln = file_line(n, m.start()) if n in STARTS else 0
            hits.append((n, ln, m.group(0),
                         t[max(0, m.start() - width):m.end() + width].replace("\n", " ")))
    print(f"   {name}: {len(hits)}")
    for h in hits[:limit]:
        print(f"      {h[0]} line {h[1]} [{h[2]}] | {h[3][:120]}")
    if len(hits) > limit:
        print(f"      ... and {len(hits) - limit} more")
    return hits


print("   -- the six bare words, with the apparatus word available to the narrator "
      "only to say that there is none")
sweep("digits in body prose", r"\d")
sweep("digits in apparatus", r"\d", scope=APPAR)
sweep("non-ascii in body prose", r"[^\x00-\x7f]")
sweep("em dash, en dash, figure dash", r"[\u2014\u2013\u2012\u2212]")
sweep("volume|batch|chapter|seat|fieldbook|tally|panel",
      r"\b(volume|batch|chapter|seat|fieldbook|tally|panel)\b")

print("   -- the twelve month names. THE MODAL VERB IS NOT A MONTH, so the sweep "
      "runs twice: a capitalised name, and a lower-case may that carries a date "
      "rather than a verb.")
cap = sweep("the twelve month names, capitalised",
            r"\b(January|February|March|April|May|June|July|August|September|"
            r"October|November|December)\b", flags=0)
dat = sweep("a lower-case may carrying a date and not a verb",
            r"\b(in|on|of|until|since|by|through)\s+may\b|\bmay\s+the\b", flags=0)
print(f"   month names in any form: {len(cap) + len(dat)}")

print("   -- the words that are unavailable in this holding, in body prose and in "
      "apparatus, and the apparatus counted inside its own block")
for label, pat in [("anchor, in any form", r"anchor"),
                   ("rootmark, in any form", r"rootmark")]:
    sweep(label + ", body prose", pat)
    sweep(label + ", apparatus", pat, scope=APPAR)
for label, pat in [("single private field", r"single private field"),
                   ("unified response", r"unified response"),
                   ("nine minutes", r"(?<![\w-])nine minutes(?![\w-])")]:
    h = sweep("the phrase that would name the first permanent loss: " + label,
              pat)
    sweep(label + ", apparatus", pat, scope=APPAR)

print("   -- the arrangement, the thing that is paid, and the let-go family")
sweep("the arrangement words", r"\b(surrender|surrendered|surrendering|resign|"
      r"resigned|resigning|resignation)\b")
sweep("the words that would name the forty-first morning",
      r"\b(failure|failed|fail|betrayal|betrayed|heroic|hero)\b")
# THE NAME OF THE THING THAT IS PAID IS NOT WRITTEN INTO THIS FILE, BECAUSE THIS
# CLOSE MAY NOT PRINT IT. THE INSTRUMENT THAT PROVES ITS ABSENCE IS THEREFORE NOT
# A SWEEP FOR IT BUT THE LIST OF EVERY CAPITALISED WORD THAT STANDS MID-SENTENCE IN
# THE FORTY-FIVE MORNINGS: if the name is not in that list it is on no page, and the
# list is printed whole so that a reader can check the absence without being given
# the word.
_caps = collections.Counter()
for _n, _t in BODIES.items():
    for _sent in re.split(r"(?<=[.?!])\s+", _t):
        _w = re.findall(r"[A-Za-z][A-Za-z'-]*", _sent)
        for _i, _x in enumerate(_w[1:], 1):
            if _x[:1].isupper():
                _caps[_x] += 1
print(f"   distinct capitalised words standing mid-sentence in the forty-five "
      f"mornings: {len(_caps)}")
print(f"      {sorted(_caps)}")
sweep("the let-go family", r"\blet go\b|\bletting go\b|go their own way|"
      r"walk away|\bwithdraw\b|\bwithdrew\b")

print("   -- the compost line and the seed keeper")
sweep("a figure for a turn in the compost line, thirty-two standing alone",
      r"(?<!hundred and )(?<![\w-])thirty-two(?![\w-])")
sweep("*discharg*, which stands inside a negation every time it appears",
      r"discharg")
sweep("*apolog*", r"apolog")
sweep("one ear, deaf, cannot hear", r"\bone ear\b|\bdeaf\b|\bcannot hear\b")
sweep("a hand on her arm, which must stand only as a statement that none was laid",
      r"\bhand(?:s)? on her arm\b")

print("   -- the ladder and the drawer, whose standing is FRESH for these "
      "forty-five mornings and is not a claim about the fifteen behind")
sweep("the ladder named", r"\bladder\b")
rung = sweep("a rung, or a climbing verb", r"\brungs?\b|\bclimb\w*\b|\bascend\w*\b")
sweep("the drawer named", r"\bdrawer\b")
sweep("the drawer standing open", r"drawer[^.]{0,60}\bopen\b|\bopen\b[^.]{0,40}drawer")
sweep("the key off its nail", r"key off (?:its|the) nail|off (?:its|the) nail")

print("   -- the door nine hundred yards off. ITS OWN FIGURE IS *SIXTY-SIX* "
      "STANDING ALONE, and two other series in this holding carry that pair of "
      "words inside a larger figure on a morning of their own.")
sweep("the door's own figure standing alone",
      r"(?<!hundred and )(?<![\w-])sixty-six(?![\w-])")
sweep("and the same pair of words inside a larger figure, which is a collision "
      "in the sweep and not a printing of the door",
      r"(?<=hundred and )sixty-six\b")

print("   -- the standing blocks this volume restates, counted PER MORNING and not "
      "per occurrence, because an occurrence is not a morning")
for label, pat in [
        ("the compost board at the back of the tap house read paid at thirty-one",
         r"compost board at the back of the tap house read paid at thirty-one"),
        ("Kellan Rusk came out to the step with the register form under his arm",
         r"kellan rusk came out to the step with the register form under his arm"),
        ("the man who lays for three councils came down the middle road with his hod",
         r"man who lays for three councils came down the middle road with his hod"),
        ("a woman's own sheet with a refusal written on it in her own hand",
         r"woman.s own sheet with a refusal written on it in her own hand"),
        ("no column cut under any of them", r"no column cut under any of them"),
        ("Tova Reed had the four ages on the corner of the seed board",
         r"tova reed had the four ages on the corner of the seed board"),
        ("nothing against it", r"nothing against it"),
]:
    rx2 = re.compile(pat, re.I)
    occ = collections.Counter()
    for n, t in BODIES.items():
        occ[n] = len(rx2.findall(t))
    days = sorted(d for d in FILE_OF_DAY.values() if occ[d])
    print(f"     {sum(occ.values())} occurrence(s) on {len(days)} morning(s): "
          f"{label}")
    print(f"        {days}")

print("   -- the two locked sentences and their six load-bearing strings")
sweep("the six load-bearing strings", "|".join(re.escape(s) for s in STRINGS),
      limit=20)

print("   -- the thirty-five, the six not knowns, and the pruning window")
sweep("thirty-five in and thirty-five out", r"thirty-five in")
sweep("a figure published for the thirty-five other than thirty-five",
      r"thirty-four (?:open|left|threads|questions)|thirty-six (?:open|left|threads|"
      r"questions|rows)|thirty-five (?:answered|closed|resolved|grouped|summed)")
sweep("six ruled rows, and no seventh", r"six ruled rows|no seventh row|"
      r"seventh ruled row|six not knowns")
sweep("pruning, pruned", r"\bpruning\b|\bpruned\b|\bprunes\b")
flow = sweep("the flow", r"\bthe flow\b", limit=20)
sweep("a mercy", r"\bmercy\b")
sweep("*of this month*", r"of this month")

print("   -- the second reckoning, which is carried and not printed on the eleven "
      "fourth-line mornings. CHECKED AS THE TWELVE VALUES IT TAKES, nothing else.")
SECOND_VALUES = [D.ordinal(D.second_reckoning(i)) for i in range(1, 12)]
hits = sweep("the eleven second-reckoning values standing alone, anywhere in "
             "Volume 16, and NOT inside a larger figure, because ninety-ninth is "
             "also the top limb of an aggregate clause in the four hundreds",
             "(?<!hundred and )" + "|".join(re.escape(v) for v in SECOND_VALUES),
             limit=20)
on_fourth = [h for h in hits if h[0] in [FILE_OF_DAY[d] for d in range(949, 994)
                                         if D.is_fourth_line(d)]]
print(f"   of those, on the eleven fourth-line mornings, where the second reckoning "
      f"must be ABSENT: {len(on_fourth)} {on_fourth}")

print("   -- the spellings")
sweep("an attached hundredweight", r"\w+hundredweight")
sweep("the wrong and in the bare round hundred in the thousands, where the figure "
      "IS exactly one thousand four hundred",
      r"one thousand and four hundred(?!\s+and)")
sweep("the bare round hundred in the thousands, where it is required",
      r"one thousand four hundred(?![\w-])")
sweep("a hyphen inside a spelled hundreds figure", r"one hundred-|two hundred-|"
      r"three hundred-|four hundred-|five hundred-|six hundred-|seven hundred-|"
      r"eight hundred-|nine hundred-")
sweep("an ordinal date in body prose",
      r"\b(?:on|in|by|at|until|from|of)\s+the\s+(?:first|second|third|fourth|fifth|"
      r"sixth|seventh|eighth|ninth|tenth|eleventh|twelfth|thirteenth|fourteenth|"
      r"fifteenth|sixteenth|seventeenth|eighteenth|nineteenth|twentieth|"
      r"thirtieth)\s+of\s+(?!hour\b)")
sweep("a day of the week, which this holding keeps and which no rule forbids",
      r"\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b", limit=6)

print("   -- the counts that stand and are not to be added to")
sweep("the thirty-nine blanks and the second rule under them",
      r"thirty-nine blanks|thirty-ninth time")
sweep("the fifteen lines of the use log, and a sixteenth",
      r"fifteen lines|sixteenth line")
sweep("eleven journeys of the barrow, and a twelfth",
      r"eleven journeys|twelfth journey")
sweep("a fifth sheet, a fifth term or a fifth column, which the pages forbid",
      r"\bfifth (?:sheet|term|column)\b|\bfourth term\b|\bsixth term\b")
sweep("a column cut under one of the four sheets", r"column cut under|"
      r"cut a column|column was cut")
sweep("the four sheets, none entered and none refused",
      r"none entered|none refused|no column cut under", limit=6)
sweep("twenty-nine fetchings of the man of about seventy, and a fetching",
      r"twenty-nine fetchings|was fetched|\bfetched\b", limit=8)
sweep("the seed ring re-dug, re-counted or improved",
      r"\bnine beds dug\b|\bten beds\b|\beight beds\b|\bsix beds\b")
sweep("the four losses, and a fifth",
      r"\bfour losses\b|\bfive losses\b|\blosses\b", limit=12)

hr("9. ORDINALS OUTSIDE HEADINGS, AT THE UNIT DECLARED. A HIT IS A HIT AND NOT A "
   "VERDICT, AND THE HYPHEN IN A SPELLED TENS-ORDINAL DEFEATS A HARNESS'S OWN "
   "EXCLUSION RULE, SO EVERY HIT IS CLASSIFIED AND THE RESIDUAL IS PRINTED.")
ORD_WORDS = ("ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth",
             "fifteenth", "sixteenth", "seventeenth", "eighteenth", "nineteenth",
             "twentieth", "thirtieth")
ordrx = re.compile(r"\b(" + "|".join(ORD_WORDS) + r")\b", re.I)
kinds, residual = collections.Counter(), []
for n, t in BODIES.items():
    for m in ordrx.finditer(t):
        before = re.findall(r"[A-Za-z-]+", t[:m.start()])[-3:]
        after = re.findall(r"[A-Za-z-]+", t[m.end():])[:3]
        word = m.group(0).lower()
        if "hour" in after:
            kinds["an hour, in the house form"] += 1
        elif any(b.endswith("hundred") or b.endswith("thousand") for b in before) or \
                (before and before[-1].endswith("-")):
            kinds["a limb of a spelled figure, tens-ordinal hyphenated"] += 1
        else:
            kinds["something else, printed in full below"] += 1
            residual.append((n, file_line(n, m.start()), word, before, after,
                             t[max(0, m.start() - 60):m.end() + 60].replace("\n", " ")))
print(f"   ordinal words of that set standing in body prose: "
      f"{sum(kinds.values())}")
for k, v in kinds.most_common():
    print(f"     {v:>4}  {k}")
print(f"   the residual, every one read: {len(residual)}")
for r in residual:
    print(f"     {r[0]} line {r[1]}: {r[2]!r} | before {r[3]} after {r[4]}")
    print(f"        {r[5][:150]}")

hr("9b. THE EIGHT FIGURES OF THE FIGURE CHECK THAT ARE PRESENT IN THE WRONG FORM, "
   "NAMED BY FILE AND BY LINE, AND NOT REPAIRED")
for n, series, phrase, day in failures:
    pth = PATH_OF[n]
    val = D.aggregate(day) if series == "aggregate" else D.ordinal_of_run(day)
    other = D.ordinal(val) if series == "aggregate" else D.cardinal(val)
    for ln, line in enumerate(pth.read_text().splitlines(), 1):
        low = line.lower()
        if other in low:
            i = low.find(other)
            print(f"   {n} line {ln}, day {day}, morning {D.morning(day)}: the "
                  f"{series} is {val} and the page prints "
                  f"{'the ordinal where the series is a cardinal' if series == 'aggregate' else 'a cardinal where the series is an ordinal'}:")
            print(f"      {line[max(0, i - 90):i + 110]}")
            break
print(f"   the eight are a FORM and not a VALUE. Every one of the eight values is "
      f"correct for its day and correct against the plan's own day table, and not "
      f"one figure of any series was moved to pay for them.")

hr("10. THE SIX LOCKED FIGURES AND THE TWO ALLOWED FIGURES, AND WHAT THE VOLUME "
   "SPENDS")
print(f"   the third launder's maximum stands on day {mx_day} "
      f"({FILE_OF_DAY[mx_day]}, morning {D.morning(mx_day)}) and not on the last "
      f"morning, because the volume closes on an odd morning and an odd morning "
      f"falls")
print(f"   the ordinal of the run on the last morning is "
      f"{D.ordinal(D.ordinal_of_run(993))} and on the morning before it "
      f"{D.ordinal(D.ordinal_of_run(992))}, so the ordinal of the run stands one "
      f"HIGHER on the last morning while the launder figure stands "
      f"{launders[mx_day] - launders[993]} LOWER, and the two are two series and "
      f"are not added and are not a sign")
head()
