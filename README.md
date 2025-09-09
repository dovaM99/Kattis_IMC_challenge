# Kattis IMC Challenge

![IMC Challenge](imc-logo.png)

Repository of my code for the [Huawei IMC Challenge](https://www.huawei.com/minisite/imc-challenge/en/).
The challenge invites developers to analyse signals and deliver efficient
algorithms across multiple problem statements.

## About the challenge

The Huawei International Microelectronics Challenge (IMC) is a competition
centred on high‑speed signal processing.  Contestants receive analog waveform
data captured from digital communication links and must design algorithms that
reconstruct or interpret the underlying signals while operating within strict
performance limits.

## Dashboard

| Metric   | Value |
|----------|------:|
| Score    | 1234  |
| Position |    42 |

## Repository layout

- `data/` – waveform and sliced data used by the solutions.
- `problem_A/` – problem statement and solution for Problem A.
- `problem_B/` – problem statement and solution for Problem B.

## Problem A

**Task:** Model a high‑speed communication channel and reconstruct a clean
analog waveform.  The input lists \(N\) samples of a distorted wave, and the
program must output a new waveform of length \(L = K \times 16\) that
approximates the undamaged signal.  Scoring uses the root mean square error
against a hidden reference.

The script in `problem_A/proposed_solution_pb_A.py` reads the waveform data
set and reports statistics such as average amplitude and number of zero
crossings.  These features form the basis for a classifier or scoring
function as described in the problem PDF.

## Problem B

**Task:** Recover the transmitted PAM4 symbol sequence by equalising an
oversampled analog waveform.  The input provides the waveform and reference
digital streams; the solution outputs the reconstructed sequence using the
four PAM4 levels and is evaluated by the error to the reference data.

The script in `problem_B/proposed_solution_pb_B.py` summarises each slice of
numeric data.  It computes the sum and mean for every slice to serve as a
lightweight yet effective representation for downstream modelling.
