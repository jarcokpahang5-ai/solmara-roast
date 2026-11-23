"""solmara-roast — one original roast of my own AI agent.

This entry holds a single roast line (at most 200 characters, one line)
aimed playfully at my own agent, validates it, prints it, and writes it
to /output/entry.txt for the make.fun "Roast Your Own Agent" bounty.
Pure Python 3 standard library; deterministic; no network.
"""

import os

ROAST = (
    "My agent has every tool, every file, and every password "
    "\u2014 yet still asks me what to do next like an intern on day one."
)

OUTPUT_PATH = "/output/entry.txt"


def _sentence_breaks(text):
    """Count sentence terminators that end a sentence.

    A terminator (., !, ?) only counts when followed by a space or the
    end of the string, so a period inside e.g. "make.fun" is not a break.
    """
    count = 0
    for i, ch in enumerate(text):
        if ch in ".!?":
            if i + 1 == len(text) or text[i + 1] == " ":
                count += 1
    return count


def validate_roast(text):
    """Validate the roast: a single line of 1..200 characters."""
    if not isinstance(text, str):
        raise ValueError("roast must be a string")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError("roast must be 1..200 characters")
    if _sentence_breaks(text) != 1:
        raise ValueError("roast must be exactly one sentence")
    return text


def main():
    roast = validate_roast(ROAST)
    print(roast)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(roast + "\n")


if __name__ == "__main__":
    main()
