# T3XT

A small command line tool that rewrites text in leetspeak, swapping letters for
number lookalikes. By default it only replaces some of the letters at random, so
you get the uneven look of something like:

```
WH4T S74ND5 IN THE W4Y BECOME5 7H3 W4Y
```

## Usage

Pass the string you want to convert as an argument:

```
python3 leetspeak.py "What stands in the way becomes the way"
```

Each run varies because letters are replaced with a probability rather than
every time. If you want the classic all-caps look, add `-u`:

```
python3 leetspeak.py -u "What stands in the way becomes the way"
```

## Options

- `-p`, `--prob` sets the chance (0 to 1) that a convertible letter is replaced.
  The default is 0.6. Lower it for a subtler effect, raise it for heavier
  substitution.
- `-a`, `--all` replaces every convertible letter. Same as `--prob 1`.
- `-u`, `--upper` uppercases the text before converting.
- `-s`, `--seed` fixes the random seed so you get the same output every time.
  Useful when you want a result you can reproduce.

## Letter mapping

The following letters are swapped for digits: a becomes 4, e becomes 3, i
becomes 1, o becomes 0, s becomes 5, t becomes 7, b becomes 8, and g becomes 9.
Letters without a number lookalike are left alone.

## Examples

```
$ python3 leetspeak.py -u -a "What stands in the way becomes the way"
WH47 574ND5 1N 7H3 W4Y 83C0M35 7H3 W4Y

$ python3 leetspeak.py -u -s 42 "What stands in the way becomes the way"
WHA7 57ANDS IN 7H3 W4Y 83C0M3S 7H3 W4Y
```
