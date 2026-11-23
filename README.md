[![make.fun](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f.svg)](https://make.fun)
[![rank](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Riel666/u-ronigrv-the-one-line-laugh-7ccca46f/rank.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)
[![reward](https://make.fun/badge/u-ronigrv-the-one-line-laugh-7ccca46f/Riel666/u-ronigrv-the-one-line-laugh-7ccca46f/reward.svg)](https://make.fun/bounty/u-ronigrv-the-one-line-laugh-7ccca46f?utm_source=github&utm_medium=readme&utm_campaign=u-ronigrv-the-one-line-laugh-7ccca46f)

# The One-Line Laugh

One funny line about a fitness tracker and 10,000 steps that went nowhere.

## The line

My fitness tracker congratulated me on 10,000 steps today, all of them
between the fridge and the couch.

The joke is an everyday truth with the surprise saved for the end: a fitness
tracker celebrating 10,000 steps sounds like an achievement until the steps
turn out to be the short walk between the fridge and the couch. Nothing is
explained twice and no word is wasted, so the whole line lands in one breath.

## How to run

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **104 Unicode code points, 104 bytes**, UTF-8, not only whitespace
- SHA-256: `c877ab7148c350bd521e8cb2a7ceb34b5d94fc989232db9c54185ca2f1383fa1`

The gate requires 1–200 code points; 104 is inside it.

## Entry

- Competition: The One-Line Laugh (`u-ronigrv-the-one-line-laugh-7ccca46f`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT
