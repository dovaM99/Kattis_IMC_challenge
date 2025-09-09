# Kattis IMC Challenge

![IMC Challenge](https://www.huawei.com/minisite/imc-challenge/en/img/banner.jpg)

Repository of my code for the [Huawei IMC Challenge](https://www.huawei.com/minisite/imc-challenge/en/).
The challenge invites developers to analyse signals and deliver efficient
algorithms across multiple problem statements.

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

The script in `problem_A/proposed_solution_pb_A.py` reads the waveform
data set and reports statistics such as average amplitude and number of
zero crossings.  These features form the basis for a classifier or
scoring function as described in the problem PDF.

## Problem B

The script in `problem_B/proposed_solution_pb_B.py` summarises each
slice of numeric data.  It computes the sum and mean for every slice to
serve as a lightweight yet effective representation for downstream
modelling.
