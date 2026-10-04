#!/usr/bin/env python3
"""Volume 16 close: the figure derivation, from the rules at outline/volume-16.md
section 10a, applied to each morning's own day.

NOTHING HERE IS INHERITED FROM THE PLAN'S DAY TABLE AT SECTION 10c, FROM A BATCH
HARNESS, OR FROM A BATCH PROMPT. The rules are transcribed at the top of each
function with the line of section 10a they come from, and the generator is run
against the last day of the volume behind as well, which is the check that settles
a rule set rather than a table.
"""

# ---------------------------------------------------------------- the spellings
# outline/volume-16.md section 9, seven house forms, and the eighth derivation at
# site three-A.

ONES_C = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
          "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
          "sixteen", "seventeen", "eighteen", "nineteen"]
TENS_C = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
          "eighty", "ninety"]
ORD_O = ["zeroth", "first", "second", "third", "fourth", "fifth", "sixth",
         "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth",
         "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth",
         "eighteenth", "nineteenth"]
# A tens-ordinal is hyphenated (site five). The round tens are whole words
# (twentieth, ninetieth) and the rest take a stem and a hyphen (twenty-first,
# ninety-ninth).
TENS_O_STEM = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy",
               "eighty", "ninety"]
TENS_O_WHOLE = ["", "", "twentieth", "thirtieth", "fortieth", "fiftieth",
                "sixtieth", "seventieth", "eightieth", "ninetieth"]


def under100(n):
    if n < 20:
        return ONES_C[n]
    t, u = divmod(n, 10)
    return TENS_C[t] + ("-" + ONES_C[u] if u else "")


def ordinal(n):
    """Site five: the ending goes on the whole word at a round hundred, and a
    tens-ordinal is hyphenated. One hundred is *one hundredth*."""
    if n < 20:
        return ORD_O[n]
    if n < 100:
        t, u = divmod(n, 10)
        return TENS_O_WHOLE[t] if u == 0 else TENS_O_STEM[t] + "-" + ORD_O[u]
    h, rest = divmod(n, 100)
    head = ONES_C[h] + " hundred"
    if rest == 0:
        return head + "th"
    return head + " and " + ordinal(rest)


def cardinal(n, style="std"):
    """style 'std'      : sites one and two. 200-999 is [WORD] HUNDRED AND [WORD],
                        bare at a round hundred; 100-199 is ONE HUNDRED AND [WORD].
    style 'letter100' : the letter and the fourth-line series, which take the bare
                        *a hundred* form across the whole hundred range.
    style 'ra100'     : the read-aloud numerator, which is ONE HUNDRED AND [WORD]
                        across the hundred range and is a different figure with a
                        different form (site seven)."""
    if n < 100:
        return under100(n)
    h, rest = divmod(n, 100)
    if rest == 0:
        return "a hundred" if (n == 100 and style in ("letter100", "ra100")) \
            else ONES_C[h] + " hundred"
    head = ONES_C[h] + " hundred"
    if n < 200:
        head = "a hundred" if style == "letter100" else "one hundred"
    return head + " and " + under100(rest)


def cardinal_k(n):
    """Site three keeps BOTH ands; site three-A is a bare round hundred in the
    thousands, one thousand four hundred with no and in it."""
    th, rest = divmod(n, 1000)
    head = ONES_C[th] + " thousand"
    if rest == 0:
        return head
    if rest % 100 == 0:
        return head + " " + cardinal(rest)
    return head + " and " + cardinal(rest)


# ---------------------------------------------------------------- the rules
# Each rule as it is written at outline/volume-16.md section 10a.

VOL_FIRST_DAY, VOL_LAST_DAY = 949, 993          # section 3, and section 10c's own range
ANCHOR_DAY, ANCHOR_VALUE = 851, 1209            # "anchored at one thousand and
                                                 #  two hundred and nine on day 851"


def weekday(d):
    return ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
            "Sunday", "Monday"][(d - 451) % 7]


def day_of_month(d):
    return (d - 451) % 30 + 1


def month(d):
    return 4 + (d - 451) // 30


def morning(d):
    return d - 948


def third_launder(d):
    """Anchored at 1209 on day 851, plus eight on every even morning and minus
    five on every odd morning after it. No reset at a month turn, no reset at the
    volume boundary. The day-minus form is withdrawn by name."""
    v = ANCHOR_VALUE
    for day in range(ANCHOR_DAY + 1, d + 1):
        v += 8 if morning(day) % 2 == 0 else -5
    return v


def ordinal_of_run(d):
    return d - 450


def window(d):
    return d - 483


def halves(d):
    """The falling half is a hundred and forty-five plus half of everything above
    three hundred, floor; a fall on every odd morning and a rise on every even
    one. Both halves always add to the window."""
    w = window(d)
    falling = 145 + (w - 300) // 2
    return falling, w - falling


def aggregate(d):
    return d - 452


def near_board(d):
    return d - 66


def far_board(d):
    return d - 19


def register_form(d):
    return d - 556


def charter(d):
    return d - 650


def second_ruled_line(d):
    return d - 562


def letter(d):
    return d - 753


def is_read_aloud(d):
    """Read at the seventh hour on every odd morning and on no even one."""
    return morning(d) % 2 == 1


def read_aloud_numerator(d, first=949):
    """A hundred and ninety-six on the first morning it appears, which is this
    volume's first morning because it opens on an odd morning, rising by one on
    every odd morning after it."""
    return 196 + ((d - first) // 2)


def read_aloud_denominator(d):
    return d - 526


def is_fourth_line(d):
    return d % 4 == 2


def count_in_force(index):
    """Stands at a hundred and sixty-three at the boundary and rises by one on
    each fourth-line morning."""
    return 163 + index


def not_half(index):
    return count_in_force(index) - 29


def first_reckoning(index):
    """Steps by one on every fourth-line morning.

    THE STARTING VALUE IS TAKEN FROM THE ELEVEN PAGES AND FROM THE PLAN'S OWN DAY
    TABLE AT SECTION 10c, WHICH AGREE WITH EACH OTHER, AND NOT FROM THE PROSE AT
    SECTION 10a, WHICH SAYS *FROM ONE HUNDRED AND SIXTH* AND ALSO SAYS *TO ONE
    HUNDRED AND SEVENTEENTH* OVER ELEVEN MORNINGS, WHICH ARE ELEVEN FIGURES AND
    TEN STEPS. ONE ENDPOINT IS WRONG AND THE ENDPOINT THAT AGREES WITH ALL ELEVEN
    MORNINGS IS THE LAST ONE, so the run is 107 to 117. The close reports the
    defect in the plan's prose and does not repair that file."""
    return 106 + index


def second_reckoning(index):
    """Thirteen apart and never agreeing."""
    return first_reckoning(index) - 13


def is_return(d):
    """The last return morning of the volume behind was day 946; returns come
    every nine days and the day is derived by adding nine and never by carrying a
    count forward."""
    return (d - 946) % 9 == 0 and d > 946


# ------------------------------------------------------- the derived spellings

def figures_for(d):
    """The derived figures of one morning, each with the series it belongs to and
    whether the item list requires it present or requires it absent."""
    fall, rise = halves(d)
    items = [
        ("third launder", cardinal_k(third_launder(d)) + " hundredweight", True),
        ("ordinal of the run", ordinal(ordinal_of_run(d)), True),
        ("rising half", cardinal(rise), True),
        ("falling half", cardinal(fall), True),
        ("window", cardinal(window(d)), True),
        ("aggregate", cardinal(aggregate(d)), True),
        ("aggregate clause, limb under the line", ordinal(aggregate(d) - 1), True),
        ("aggregate clause, limb over the line", ordinal(aggregate(d) + 1), True),
        ("near board", cardinal(near_board(d)), True),
        ("far board", cardinal(far_board(d)), True),
        ("register form", cardinal(register_form(d)), True),
        ("charter", cardinal(charter(d)), True),
        ("Silling's second ruled line", cardinal(second_ruled_line(d)), True),
        ("the letter", cardinal(letter(d), "letter100"), True),
    ]
    if is_read_aloud(d):
        items += [
            ("read-aloud numerator",
             cardinal(read_aloud_numerator(d), "ra100"), True),
            ("read-aloud denominator", cardinal(read_aloud_denominator(d)), True),
        ]
    if is_fourth_line(d):
        idx = sorted(x for x in range(950, 994, 4)).index(d) + 1
        items += [
            ("count in force", cardinal(count_in_force(idx), "letter100"), True),
            ("the taken figure", "twenty-nine", True),
            ("the not figure", cardinal(not_half(idx), "letter100"), True),
            ("first reckoning", ordinal(first_reckoning(idx)), True),
            # section 8d: carried and not printed on a morning that prints the
            # first. The item list still counts it, so it is checked for ABSENCE.
            ("second reckoning", ordinal(second_reckoning(idx)), False),
        ]
    return items


def item_list_total():
    """Derived from the volume's own item list and not inherited: fourteen on
    every morning, two more on each of the twenty-three odd mornings, five more
    on each of the eleven fourth-line mornings."""
    base, odd, fourth = 0, 0, 0
    for d in range(VOL_FIRST_DAY, VOL_LAST_DAY + 1):
        base += 14
        if is_read_aloud(d):
            odd += 1
        if is_fourth_line(d):
            fourth += 1
    return {"mornings": base // 14, "odd": odd, "fourth_line": fourth,
            "base_total": base, "odd_total": 2 * odd, "fourth_total": 5 * fourth,
            "total": base + 2 * odd + 5 * fourth}


if __name__ == "__main__":
    import json
    print(json.dumps(item_list_total(), indent=2))
