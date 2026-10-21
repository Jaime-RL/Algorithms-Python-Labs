# Algorithms in Python — Labs

Algorithm analysis labs in Python: **divide & conquer**, **recursion → iteration transformation**, **stack-based linear algorithms** and **empirical complexity analysis** with timing plots, plus unit tests with **pytest**.

## Contents

| File | Technique | Description |
|---|---|---|
| `sum_of_distances.py` | Monotonic stack, O(n) | For each element, distance to the next greater element; measures best/worst-case running time for n = 10⁴…10⁶ and plots it |
| `majority_element.py` | Divide & conquer, O(n) | Finds the majority element (> n/2 occurrences) by pairing reduction + verification, with timing plots |
| `majority_candidate.py` | Recursive vs iterative | Same candidate search written recursively and transformed into an equivalent iterative version |
| `frog_puzzle.py` | Recursion → iteration | Solves the "frogs" puzzle (swap two groups of pieces across a gap) recursively and iteratively, rendering the board with ANSI colours |
| `test_*.py` | pytest | Parametrised tests for both majority-element implementations |

## Running

```bash
pip install -r requirements.txt

python sum_of_distances.py      # timing plots
python frog_puzzle.py           # step-by-step board in the terminal
python -m pytest -v             # run the test suite
```

## Tech

Python 3 · pytest · Matplotlib
