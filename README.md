# Mersenne Prime Generator

This repository is a GitHub Codespaces exercise in running and exploring a
Python program that searches for Mersenne primes. A Mersenne prime has the
form `2^p - 1`, where `p` is a prime exponent.

The program in [`src/hello.py`](src/hello.py) uses the Lucas-Lehmer test to
check each candidate. It requires only Python 3; no packages need to be
installed.

## Open in GitHub Codespaces

1. Open this repository on GitHub.
2. Select **Code**, choose the **Codespaces** tab, and select **Create
	codespace on main**.
3. Wait for the codespace to finish creating, then open the integrated
	terminal in VS Code.

Run the default search:

```bash
python3 src/hello.py
```

This finds the first Mersenne prime, `3`.

## Exercise

Try changing the exponent range and number of results:

```bash
python3 src/hello.py --start 127 --count 1
python3 src/hello.py --start 1000 --count 2
```

The available flags are:

| Flag | Description | Default |
| --- | --- | --- |
| `--start N` | First exponent to test | `2` |
| `--count N` | Number of Mersenne primes to find | `1` |
| `--help` | Display command-line help | - |

Start with a small exponent while experimenting. Larger exponents require
substantially more CPU time and memory, and the search prints each exponent as
it works. Press `Ctrl+C` in the terminal to stop a long-running search.

## How it works

For each exponent `p`, the program first checks that `p` is prime. It then
applies the Lucas-Lehmer recurrence:

```text
s = (s * s - 2) % (2**p - 1)
```

Starting with `s = 4`, the recurrence runs `p - 2` times. If the final value
is `0`, then `2**p - 1` is a Mersenne prime.

