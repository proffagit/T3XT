#!/usr/bin/env python3
"""Convert a string to leetspeak by replacing some letters with numbers.

Example:
    $ python3 leetspeak.py "What stands in the way becomes the way"
    WH4T 5T4ND5 IN THE W4Y B3COM35 THE W4Y
"""

import argparse
import random

# Letters that have a common number lookalike.
LEET_MAP = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5",
    "t": "7",
    "b": "8",
    "g": "9",
}


def leetify(text, prob=0.6, seed=None):
    """Return text with each mappable letter replaced by a digit with `prob` chance."""
    rng = random.Random(seed)
    out = []
    for ch in text:
        repl = LEET_MAP.get(ch.lower())
        if repl is not None and rng.random() < prob:
            out.append(repl)
        else:
            out.append(ch)
    return "".join(out)


def main():
    parser = argparse.ArgumentParser(description="Convert a string to leetspeak.")
    parser.add_argument("text", help="the string to convert")
    parser.add_argument(
        "-p",
        "--prob",
        type=float,
        default=0.6,
        help="probability (0-1) that a mappable letter is replaced (default: 0.6)",
    )
    parser.add_argument(
        "-a",
        "--all",
        action="store_true",
        help="replace every mappable letter (same as --prob 1)",
    )
    parser.add_argument(
        "-u",
        "--upper",
        action="store_true",
        help="uppercase the output first",
    )
    parser.add_argument(
        "-s",
        "--seed",
        type=int,
        default=None,
        help="random seed for reproducible output",
    )
    args = parser.parse_args()

    text = args.text.upper() if args.upper else args.text
    prob = 1.0 if args.all else args.prob
    print(leetify(text, prob=prob, seed=args.seed))


if __name__ == "__main__":
    main()
