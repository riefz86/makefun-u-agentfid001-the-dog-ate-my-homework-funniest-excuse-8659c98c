# Drafting notes — The Dog Ate My Homework: Funniest Excuse

## The line

> I only ate the answers page. The questions are all still there, so technically I turned your homework into a pop quiz. You're welcome.

134 characters, one line, no trailing newline.

## Why this line

The judge's brief ranks its criteria in order, so the line was built
to clear them top to bottom:

1. **Dog's own voice, caught in the act.** First person, present
   tense, answering for the eaten homework directly. No narrator, no
   human apologising on the dog's behalf.
2. **A twist of dog logic.** Eating only the answers page is not
   destruction in the dog's accounting — it is a curriculum change.
   "Technically" is the dog lawyering; "You're welcome" is the dog
   expecting gratitude for the damage.
3. **A real dog's priorities.** The dog is not embarrassed and not
   sorry. It reports what it did the way a dog reports a good deed:
   proudly, and slightly confused about why anyone is upset.
4. **Stands alone.** No setup, no second line, no reference to
   anything outside the sentence. A stranger reading only this line
   gets the whole joke.
5. **Fresh.** The stock excuses the brief warns against are the cat,
   the taste of paper, and the good-boy plea. This line uses none of
   them. The homework is not food here at all — it is a test, and the
   dog has helpfully removed the easy part.

## Lines considered and dropped

- "It was blank on the inside and crunchy on the outside" — a taste
  joke, too close to the stock "taste of paper" line the brief warns
  against.
- "The homework smelled like sandwiches, so legally this is your
  fault" — the dog-blames-the-owner angle is funny, but "legally"
  invites a human argument; "You're welcome" lands the same
  shamelessness in two words.
- "I reclaimed my spot on the couch, one page at a time" — a
  territory joke, but it explains the eating instead of excusing it,
  and it needs the couch as setup.

## How the entry works

`main.py` writes the line, unchanged, to `/output/entry.txt`. It is
deterministic: the same line on every run, no randomness, no network,
no input. The gate needs 1–200 UTF-8 characters, not only
whitespace; the line is 134.
