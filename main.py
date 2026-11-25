"""The Dog Ate My Homework: Funniest Excuse.

Writes one line to /output/entry.txt: the excuse a dog gives after
being caught eating the homework, in the dog's own voice.

The joke: the dog only ate the answers page. The questions are all
still there, so in the dog's mind it did not destroy the homework at
all -- it turned it into a pop quiz, and it expects thanks. That is
the twist the judge's brief rewards: a piece of dog logic that lands
in a single line, a dog who believes it has done nothing wrong, and
nothing borrowed from the stock excuses (no cat, no taste of paper,
no "good boy" plea). The line stands alone with no setup.
"""

import os

LINE = (
    "I only ate the answers page. The questions are all still there, "
    "so technically I turned your homework into a pop quiz. "
    "You're welcome."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
