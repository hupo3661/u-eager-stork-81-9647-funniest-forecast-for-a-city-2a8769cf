"""Funniest Forecast for a City — make.fun entry.

Writes one funny city weather forecast (120 characters or fewer)
to /output/entry.txt for the judge to read. The forecast reads like
a real local bulletin for Dripford: heavy rain, umbrellas inverting,
and scattered showers of other people's socks.
"""

TEXT = "Today in Dripford: heavy rain, a 100% chance your umbrella inverts, and scattered showers of other people's socks."

OUTPUT_PATH = '/output/entry.txt'
MAX_CHARS = 120


def write_entry(text):
    """Write the forecast to the output file, exactly one trailing newline."""
    assert len(text) <= MAX_CHARS, 'entry over 120 characters'
    # One line, one trailing newline, nothing else: the gate checks
    # the file is 1 to 120 characters of UTF-8 text.
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        f.write(text + '\n')


def main():
    write_entry(TEXT)


if __name__ == '__main__':
    main()
