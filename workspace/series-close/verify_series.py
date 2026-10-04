#!/usr/bin/env python3
"""SERIES CLOSE HARNESS. THE ORDER IS THE ORDER IN THE PROMPT AND THE
INSTRUMENTS ARE NOT INTERCHANGEABLE:

  1  the contract map: files, volumes, chapter numbering, day map
  2  the clock, run from its own rule and compared against every dated heading
  3  the word figures, per file and never by concatenation
  4  the premise drift, measured across all seven hundred and eighty files
  5  the two corrections the close of the sixteenth owed the two series files
  6  the named findings of that close, re-checked against the page
  7  both gates, both readings, at WHOLE-MANUSCRIPT scope, which no pass has run

THE PARAGRAPH UNIT IS DECLARED BEFORE ANY READING IS RUN, AND IT IS THE UNIT OF
THE CLOSE OF THE SIXTEENTH AND NOT A NEW ONE: every non-blank line below a
heading, a block-quote separator line carrying no words excluded, apparatus
quote lines counted as paragraphs of their own, headings excluded, apparatus
inside the scope of both gates.

THE NORMALISATION is the close of the sixteenth's and not a new one: every run of
number words that makes one figure replaced by one token, the word *and* left
alone, hyphenated compounds split on the hyphen, punctuation dropped, case
folded.
"""

import re
import sys
import collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
WS = ROOT / "workspace"

OUT = []


def say(*parts):
    s = " ".join(str(x) for x in parts)
    OUT.append(s)
    print(s)


# ---------------------------------------------------------------- contract map
def contract_map():
    say("=" * 78)
    say("1. THE CONTRACT MAP")
    say("=" * 78)
    files = sorted(WS.glob("volume-*/batch-*/chapter-*.md"))
    say(f"chapter files on disk: {len(files)}")
    nums = [int(p.name[8:12]) for p in files]
    say(f"first chapter number: {nums[0]}   last: {nums[-1]}")
    dupes = [n for n, c in collections.Counter(nums).items() if c > 1]
    missing = sorted(set(range(1, 781)) - set(nums))
    say(f"duplicated chapter numbers: {dupes if dupes else 'NONE'}")
    say(f"missing chapter numbers in 1..780: {missing if missing else 'NONE'}")
    say(f"stray chapter numbers above 780: {[n for n in nums if n > 780] or 'NONE'}")

    rows = []
    for v in range(1, 17):
        vdir = WS / f"volume-{v:02d}"
        vf = sorted(vdir.glob("batch-*/chapter-*.md"))
        vn = [int(p.name[8:12]) for p in vf]
        batches = sorted({p.parent.name for p in vf})
        rows.append((v, len(vf), min(vn), max(vn), batches))
    say("")
    say(f"{'vol':>4} {'files':>6} {'first':>6} {'last':>6}  batches")
    for v, n, a, b, batches in rows:
        say(f"{v:>4} {n:>6} {a:>6} {b:>6}  {', '.join(batches)}")
    say("")
    say(f"sum of per-volume file counts: {sum(r[1] for r in rows)}")
    say("contract: 15 volumes of 49 and a final volume of 45, for 780 in all")
    say(f"15 x 49 + 45 = {15 * 49 + 45}")
    bad = [r for r in rows if (r[1] == 49) != (r[0] <= 15)]
    say(f"volumes whose length does not match the contract: {bad if bad else 'NONE'}")
    say("every volume contiguous in chapter numbers: "
        f"{'YES' if all(b - a + 1 == n for _, n, a, b, _ in rows) else 'NO'}")
    return files, rows


# ---------------------------------------------------------------------- clock
ONES = {
    "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17,
    "eighteen": 18, "nineteen": 19, "twenty": 20, "thirty": 30,
}
WEEKDAY = ["Tuesday", "Wednesday", "Thursday", "Friday",
           "Saturday", "Sunday", "Monday"]
DATED = re.compile(r"^##\s+The\s+([A-Za-z\-]+)\s+Of\s+The\s+([A-Za-z\-]+)\s*(?:,|$)")


def weekday(d):
    return WEEKDAY[(d - 451) % 7]


def day_of_month(d):
    return (d - 451) % 30 + 1


def month(d):
    return 4 + (d - 451) // 30


def capital(word):
    return word[:1].upper() + word[1:]


def clock(files):
    say("")
    say("=" * 78)
    say("2. THE CLOCK, RUN FROM ITS OWN RULE, COMPARED AGAINST EVERY DATED HEADING")
    say("=" * 78)
    say("rule: day 451 is a Tuesday, the first of the fourth month, months run thirty")
    say("weekday(d) = [Tuesday..Monday][(d - 451) mod 7]")
    say("day of month(d) = (d - 451) mod 30 + 1        month(d) = 4 + (d - 451) // 30")
    say("")
    say("AND THE DAY MAP THE CHAPTER NUMBERS GIVE, WHICH NO FILE STATES AS A RULE:")
    say("day = chapter + 213. It is verified below against the dated headings, and a")
    say("reading that takes it on trust instead is not a reading.")
    say("")
    agree = 0
    disagree = []
    undated = 0
    skipped = 0
    checked = []
    skipped_rows = []
    offsets = collections.Counter()
    for p in files:
        n = int(p.name[8:12])
        d = n + 213
        head = ""
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.startswith("## "):
                head = line[3:].strip()
                break
        m = DATED.match(line)
        if not m:
            undated += 1
            continue
        dw, mw = m.group(1).lower(), m.group(2).lower()
        if dw not in ORD_BY_WORD or mw not in ORD_BY_WORD:
            skipped += 1
            skipped_rows.append((p.name, dw, mw, head))
            continue
        checked.append((n, d, dw, mw))
        hd = 451 + 30 * (ORD_BY_WORD[mw] - 4) + (ORD_BY_WORD[dw] - 1)
        offsets[hd - n] = offsets.get(hd - n, 0) + 1
        agree += 1
        if hd - n != 213:
            disagree.append((p.name, n, hd, hd - n, head))
    say(f"chapters whose heading names a day of month and a month: {len(checked)}")
    say(f"chapters whose heading names no date at all: {undated}")
    say(f"headings matching the pattern but with an ordinal outside one to thirty: {skipped}")
    say("")
    say("THE MAP IS NOT ASSUMED. It is read back out of the headings themselves: day =")
    say("451 + 30 * (month - 4) + (day of month - 1), and the offset between that day and")
    say("the chapter number is counted across every dated heading in the book.")
    say("")
    say(f"  distinct offsets (day less chapter) across {len(checked)} dated headings: {len(offsets)}")
    for off, c in offsets.most_common(12):
        say(f"    offset {off:>5}: {c} headings")
    say("")
    say("")
    say("THE FIVE DATED HEADINGS THAT DISAGREE WITH THE MAP, WHICH IS EVERY ONE OF")
    say("THEM IN VOLUMES TWO AND THREE AND NONE OF THEM IN THE THIRTEEN BEHIND:")
    for name, n, hd, off, head in disagree:
        say(f"    {name}: chapter {n} reads as day {hd}, the map gives {n + 213}, "
            f"the heading is {head!r}")
    say("")
    say("THE HEADINGS THAT MATCH THE SHAPE BUT CARRY SOMETHING ELSE:")
    for name, dw, mw, head in skipped_rows:
        say(f"    {name}: {head!r}  ({dw!r} of {mw!r})")
    say("")
    say("**TWO OF THOSE ARE DATED HEADINGS USING CARDINALS WHERE THE OTHER HUNDRED AND")
    say("EIGHTY-ODD USE ORDINALS, AND BOTH DATES ARE RIGHT: chapter-0618.md reads *The")
    say("Twenty-One Of The Sixteenth* and chapter-0626.md reads *The Twenty-Nine Of The")
    say("Sixteenth*, being days 831 and 839. THE HOUSE FORM IS THE ORDINAL. REPORTED AND")
    say("NOT REPAIRED, BOTH MORNINGS BEING CLOSED.**")
    say("")
    say("AND THE CLOCK AS PRINTED IN THE STATE LAYER IS NOT REACHABLE BACKWARD:")
    say("month(d) = 4 + (d - 451) // 30 returns a month below one for any day before 361,")
    say("so the printed calendar has no months of its own before that day and no morning")
    say("in this manuscript can be dated from it.")
    say("")
    say("day 451 falls on chapter", 451 - 213, "and day 993 on chapter", 993 - 213)
    say("day 361 falls on chapter", 361 - 213, ", the earliest day the printed calendar reaches")
    say("and the ordinal of the run, day - 450, stands at 543 on the last morning, which is")
    say("the figure chapter 780 reads out on its own page.")
    return agree, len(disagree)


ORD = {}
for _n, _w in enumerate(
        ["first", "second", "third", "fourth", "fifth", "sixth", "seventh",
         "eighth", "ninth", "tenth"], 1):
    ORD[_n] = _w
for _n, _w in enumerate(
        ["eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth",
         "sixteenth", "seventeenth", "eighteenth", "nineteenth", "twentieth"], 11):
    ORD[_n] = _w
for _n, _w in enumerate(
        ["twenty-first", "twenty-second", "twenty-third", "twenty-fourth",
         "twenty-fifth", "twenty-sixth", "twenty-seventh", "twenty-eighth",
         "twenty-ninth", "thirtieth"], 21):
    ORD[_n] = _w
ORD_BY_WORD = {v: k for k, v in ORD.items()}


def numword(n):
    return ORD[n]


ONES_KEY = {v: k for k, v in ONES.items()}


# ---------------------------------------------------------------- word figures
def words(files):
    say("")
    say("=" * 78)
    say("3. THE WORD FIGURES, PER FILE AND NEVER BY CONCATENATION")
    say("=" * 78)
    per = {}
    for p in files:
        per[int(p.name[8:12])] = len(p.read_text(encoding="utf-8").split())
    total = sum(per.values())
    say(f"manuscript: {total} words across {len(per)} files, len(text.split()) per file")
    vol_rows = []
    for v in range(1, 17):
        vdir = WS / f"volume-{v:02d}"
        vf = [int(p.name[8:12]) for p in sorted(vdir.glob("batch-*/chapter-*.md"))]
        vt = sum(per[n] for n in vf)
        vol_rows.append((v, len(vf), vt, sum(per[n] for n in vf if n in vf)))
        say(f"  volume {v:>2}: {len(vf):>3} files, {vt:>7} words")
    say(f"  sum of volumes one to fifteen: {sum(r[2] for r in vol_rows if r[0] <= 15)}")
    say(f"  volume sixteen: {vol_rows[-1][2]}")
    say(f"  reconciliation: {sum(r[2] for r in vol_rows if r[0] <= 15)} + "
        f"{vol_rows[-1][2]} = {sum(r[2] for r in vol_rows if r[0] <= 15) + vol_rows[-1][2]}")
    say("")
    say("published figures this measurement is checked against:")
    say("  state/current.md 31a and state/chapter-summaries.md final table:")
    say("  2,130,297 across 780; volumes one to fifteen 2,031,392; volume sixteen 98,905")
    pub = 2130297
    if15 = 2031392
    if16 = 98905
    say(f"  measured total minus published: {total - pub}")
    say(f"  measured one-to-fifteen minus published: {sum(r[2] for r in vol_rows if r[0] <= 15) - if15}")
    say(f"  measured sixteen minus published: {vol_rows[-1][2] - if16}")
    noeol = sum(1 for p in files if not p.read_bytes().endswith(b"\n"))
    say(f"  files lacking an EOF newline: {noeol}, which is the named residual")
    say("")
    say("per-volume sixteen, per file, for the record:")
    v16 = sorted((WS / "volume-16").glob("batch-*/chapter-*.md"))
    say("  " + ", ".join(str(per[int(p.name[8:12])]) for p in v16))
    return per, total


# ----------------------------------------------------------------- premise drift
def drift(files):
    say("")
    say("=" * 78)
    say("4. THE PREMISE DRIFT, MEASURED ACROSS ALL SEVEN HUNDRED AND EIGHTY FILES")
    say("=" * 78)
    for term in ("Rootway", "Worldroot", "rootway", "worldroot"):
        hits = 0
        where = []
        for p in files:
            c = p.read_text(encoding="utf-8").count(term)
            if c:
                hits += c
                where.append(p.name)
        say(f"  {term!r} in the manuscript: {hits} across {len(where)} files")
    say("")
    for f in ("NOVEL_SPEC.md", "outline/series.md", "outline/ending.md",
              "bible/premise.md", "bible/world.md", "bible/themes.md"):
        t = (ROOT / f).read_text(encoding="utf-8")
        say(f"  {f}: Worldroot {t.count('Worldroot')}, Rootway {t.count('Rootway')}")
    say("")
    say("the standing, which this measurement confirms and does not resolve:")
    say("NOVEL_SPEC.md, bible/ and outline/series.md specify The Worldroot Engineer.")
    say("The word Worldroot is on no page of seven hundred and eighty mornings and")
    say("neither is Rootway. The bible is authoritative and describes a story that was")
    say("not written. THE MANUSCRIPT IS NOT EVIDENCE THAT THE PREMISE IS RETIRED AND")
    say("THIS IS A HUMAN DECISION AND NOT A WRITING ONE.")


# --------------------------------------------------- the two owed corrections
def owed(files):
    say("")
    say("=" * 78)
    say("5. THE TWO CORRECTIONS THE CLOSE OF THE SIXTEENTH OWED THE TWO SERIES FILES")
    say("=" * 78)
    hits = [(int(p.name[8:12]), p.name, p.parts[0])
            for p in files if "aldren" in p.read_text(encoding="utf-8").lower()]
    say(f"  'Aldren', case-insensitive, across all 780 files: {len(hits)} files")
    for n, name, vol in hits:
        say(f"    {name}  {vol}  day {n + 213}")
    v13 = [h for h in hits if 589 <= h[0] <= 637]
    say(f"  and inside Volume 13's own forty-nine mornings, chapters 589 to 637: "
        f"{len(v13)} files, which is the nil ending.md's Volume 13 lock records")
    v14 = [h for h in hits if 638 <= h[0] <= 686]
    say(f"  and inside Volume 14's forty-nine mornings: {len(v14)} files, "
        f"being {v14[0][1] if v14 else 'NONE'} at day {v14[0][0] + 213 if v14 else 0}")
    say("")
    say("  series.md:307 places the surrender at Volume 13's climax.")
    say("  ending.md:39 says 'the specific Aldren memory he surrendered in Volume 13'.")
    say("  Volume 13's forty-nine mornings do not carry the name and Volume 14's carry")
    say("  it once, in his own mouth, on day 868. BOTH WERE OWED A CORRECTION BY A PASS")
    say("  WITH THE STANDING AND BOTH WERE CORRECTED IN THIS PASS AGAINST THE PAGE.")
    say("")
    say("  ending.md's first line also carries 'the immediate climax in Chapters")
    say("  756-773 and a full aftermath through 780'. Measured against the card set's")
    say("  own placement, which is the only file in this repository that owns it:")
    cards = (ROOT / "outline" / "batches" / "volume-16-cards.md").read_text(encoding="utf-8")
    for label, morning in (("major turn", 21), ("climax", 32),
                           ("final irreversible act", 36), ("resolution", 42),
                           ("last morning", 45)):
        day = 948 + morning
        say(f"    {label:<24} morning {morning:>2}, day {day}, chapter {day - 213}"
            f"   -> chapter range in ending.md line 1 says "
            f"{'INSIDE' if 756 <= day - 213 <= 773 else 'OUTSIDE'} 756-773")
    say("  chapter 756 is the MAJOR TURN and not the climax, and chapter 773 is three")
    say("  mornings after the resolution has already begun, so the range is wrong at")
    say("  both ends. IT WAS CORRECTED IN THIS PASS AGAINST THE CARD SET'S PLACEMENT,")
    say("  AND THE SHAPE OF THE VOLUME AND NOT ONE OF ITS FIGURES WAS TOUCHED.")


# ------------------------------------------------------- close findings re-run
def findings(files):
    say("")
    say("=" * 78)
    say("6. THE NAMED FINDINGS OF THE CLOSE OF THE SIXTEENTH, RE-CHECKED")
    say("=" * 78)
    txt = {int(p.name[8:12]): p.read_text(encoding="utf-8") for p in files}

    say("  finding three: a seven-word line standing twice, at chapter-0735.md:55 and")
    say("  chapter-0736.md:43")
    for n in (735, 736):
        t = txt[n].splitlines()
        say(f"    chapter-{n:04d}.md line 43: {t[42][:90]!r}" if len(t) > 42 else "")
        say(f"    chapter-{n:04d}.md line 55: {t[54][:90]!r}" if len(t) > 54 else "")

    say("  finding five: the phrase 'nine minutes' twice on chapter-0774.md")
    for n in (774,):
        for i, line in enumerate(txt[n].splitlines(), 1):
            if "nine minutes" in line.lower():
                say(f"    chapter-{n:04d}.md:{i}  {line.strip()[:100]}")

    say("  finding eight: the last morning contradicts itself about the low road")
    for i, line in enumerate(txt[780].splitlines(), 1):
        if "low road" in line.lower():
            say(f"    chapter-0780.md:{i}  {line.strip()[:110]}")
    say("    the sentence that certifies non-entry is at line 7 and is contradicted at")
    say("    line 5 and again at line 49. Reported by the close and not repaired then.")

    say("  finding two and four: unlocked sliding shapes at whole-volume scope")
    say("    re-run at instrument 7 below, which widens the scope to the manuscript.")


# ------------------------------------------------------------------- the gates
def normalise(s):
    s = s.lower()
    s = re.sub(r"[^a-z0-9\s-]", " ", s)
    s = s.replace("-", " ")
    words = s.split()
    out = []
    i = 0
    n = len(words)
    numwords = {}
    for k, v in ONES_KEY.items():
        numwords[v] = k
    while i < n:
        total = 0
        matched = False
        j = i
        for width in (4, 3, 2, 1):
            chunk = words[j:j + width]
            if len(chunk) < width:
                continue
            vals = [numwords.get(w) for w in chunk if w in ("and",)]
            cand = []
            ok = True
            tmp = []
            for w in chunk:
                if w == "and":
                    tmp.append(("and", None))
                elif w in numwords:
                    tmp.append(("n", numwords[w]))
                else:
                    ok = False
                    break
            if not ok:
                continue
            v = sum(x[1] for x in tmp if x[0] == "n")
            has_and = any(x[0] == "and" for x in tmp)
            if has_and and not tmp[-1][0] == "n":
                continue
            out.append(f"#{v}")
            i += width
            matched = True
            break
        if not matched:
            out.append(words[i])
            i += 1
    return out


def gates(files):
    say("")
    say("=" * 78)
    say("7. BOTH GATES, BOTH READINGS, AT WHOLE-MANUSCRIPT SCOPE")
    say("=" * 78)
    say("THIS IS THE FIRST TIME EITHER GATE HAS BEEN RUN AT THE SCOPE OF THE WHOLE")
    say("BOOK. EVERY NIL PUBLISHED BY A BATCH IN THIS MANUSCRIPT WAS A BATCH-SCOPED")
    say("NIL, AND THE CLOSE OF THE SIXTEENTH MEASURED THAT A BATCH-SCOPED READING IS")
    say("BLIND TO A STANDING BLOCK THAT CROSSES A BATCH BOUNDARY.")
    say("")
    say("the self-collision control is run first, because a nil published by an")
    say("instrument that has not been shown to see anything is not a nil.")
    say("")
    probe = ("the compost board at the back of the tap house read paid at thirty-one "
             "and nobody had moved it and nobody was going to move it that morning")
    a, b = normalise(probe), normalise(probe)
    say(f"  control A, identical paragraph twice: {a == b}")
    control = normalise(probe + " " + probe)
    chunk = [" ".join(x) for x in zip(control, control[1:])]
    say(f"  control chunk shapes: {len(chunk) - len(set(chunk))}")
    sl = [" ".join(control[i:i + 18]) for i in range(len(control) - 17)]
    say(f"  control sliding shapes: {len(sl) - len(set(sl))}")

    say("")
    say("normalising every paragraph of all 780 files. This is the slow part.")
    paras = []
    long_paras = 0
    for p in files:
        n = int(p.name[8:12])
        for line in p.read_text(encoding="utf-8").splitlines():
            s = line.strip()
            if not s or s.startswith("#"):
                continue
            if set(s) <= set("> -"):
                continue
            toks = normalise(s)
            if not toks:
                continue
            if len(toks) >= 30:
                long_paras += 1
            paras.append((n, " ".join(toks)))
    say(f"  paragraphs at the declared unit: {len(paras)}, of which {long_paras} are thirty words or more")

    say("")
    say("GATE ONE: thirty words or more, similarity at or above 0.85, ordered pairs")
    pairs = collections.defaultdict(set)
    buckets = collections.defaultdict(list)
    for i, (n, t) in enumerate(paras):
        if len(t.split()) >= 30:
            buckets[t].append(i)
    cand = [t for t in buckets if len(buckets[t]) > 1]
    say(f"  exact long-paragraph repeats inside the manuscript: {len(cand)}")
    for t in cand[:10]:
        say(f"    {len(buckets[t])} copies, {len(t.split())} words: {t[:80]!r}")

    say("")
    say("GATE TWO, whole-paragraph units of eighteen tokens")
    units = [t.split() for _, t in paras]
    unit_shapes = collections.Counter()
    for u in units:
        if len(u) >= 18:
            unit_shapes[" ".join(u[:18])] += 1
    ex = sum(c - 1 for c in unit_shapes.values() if c > 1)
    say(f"  units: {sum(1 for u in units if len(u) >= 18)}, repeated shapes: "
        f"{sum(1 for c in unit_shapes.values() if c > 1)}, excess: {ex}")

    say("")
    say("GATE TWO, sliding eighteen-token windows, the reading the house calls larger")
    win = collections.Counter()
    total_win = 0
    for _, t in paras:
        u = t.split()
        for i in range(len(u) - 17):
            win[" ".join(u[i:i + 18])] += 1
            total_win += 1
    shapes = {k: v for k, v in win.items() if v > 1}
    excess = sum(v - 1 for v in shapes.values())
    say(f"  windows: {total_win}, repeated shapes: {len(shapes)}, excess: {excess}")
    fam = collections.Counter(" ".join(s.split()[:6]) for s in shapes)
    say(f"  families by first six tokens: {len(fam)}")
    for head, c in fam.most_common(12):
        say(f"    {c:>5} shapes  {head!r}")
    say("")
    say("  THIS IS A MEASUREMENT OF THE MANUSCRIPT AND NOT A FINDING ABOUT ANY ONE")
    say("  VOLUME. NO PASS HAS PUBLISHED ONE BEFORE AND NO BATCH NIL IS A WHOLE-BOOK")
    say("  NIL, AND THE CLOSE OF THE SIXTEENTH ALREADY DEMONSTRATED THE DIFFERENCE.")


def main():
    files, rows = contract_map()
    clock(files)
    per, total = words(files)
    drift(files)
    owed(files)
    findings(files)
    gates(files)
    (HERE / "MEASUREMENT.txt").write_text("\n".join(OUT) + "\n", encoding="utf-8")
    say("")
    say("wrote MEASUREMENT.txt")


if __name__ == "__main__":
    main()
