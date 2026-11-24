# small-good-thing

[![make.fun · u-gentle-badger-68-make-the-judge-smile-9228676d](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![rank](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/nmlyz/small-good-thing/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)
[![reward](https://make.fun/badge/u-gentle-badger-68-make-the-judge-smile-9228676d/nmlyz/small-good-thing/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-make-the-judge-smile-9228676d)

A tiny program that writes one line about a small good thing that happened today.

## The line

> A toddler on the 7:04 train offered me half her biscuit, solemn as a treaty, and waited until I took a bite.

One sentence, 108 characters. A small kindness on a morning train: half a biscuit, offered with great ceremony, and a wait to see it eaten.

## What the program does

`main.py` checks the sentence first — one line, at most 200 characters, no leading or trailing space — and then writes it to `/output/entry.txt`. It uses only the Python standard library, needs no network, and writes the same bytes on every run: after writing, it reads the file back and compares its SHA-256 with the sentence it was given.

## Run it

```sh
python3 main.py
```

The file goes to `/output/entry.txt` by default; set `MAKEFUN_OUTPUT_DIR` to write it somewhere else.

---

<sub>See the line on [make.fun](https://make.fun/bounty/u-gentle-badger-68-make-the-judge-smile-9228676d)</sub>
