# Data Structures Mini Projects

This repository contains two Python mini-projects that demonstrate core Data Structures concepts.

## Projects

### 1. Palindrome Checker Using Stacks and Queues
Checks whether a word or sentence reads the same forward and backward. It uses a manually implemented stack (LIFO) and queue (FIFO), rather than relying on Python's built-in reverse operation.

**Folder:** `Palindrome-Checker-Stacks-Queues/`

### 2. Job Scheduling Using Graphs
Creates a valid order for jobs based on their dependencies. It represents dependencies as a directed graph and uses Kahn's topological sorting algorithm. It also detects cycles, where no valid schedule exists.

**Folder:** `Job-Scheduling-Graphs/`

## Requirements
- Python 3.8 or newer
- No external libraries are required

## How to Run

Open a terminal in the repository folder and run:

```bash
python Palindrome-Checker-Stacks-Queues/palindrome_checker.py
python Job-Scheduling-Graphs/job_scheduling.py
```

On some systems, use `python3` instead of `python`.

## Concepts Demonstrated
- Stack and queue operations
- Strings and input processing
- Directed graphs and adjacency lists
- In-degree calculation
- Kahn's topological sorting algorithm
- Cycle detection
- Time and space complexity analysis

## Repository Structure

```text
Data-Structures-Mini-Projects/
├── README.md
├── Palindrome-Checker-Stacks-Queues/
│   ├── README.md
│   ├── palindrome_checker.py
│   └── output.txt
└── Job-Scheduling-Graphs/
    ├── README.md
    ├── job_scheduling.py
    └── output.txt
```

## Learning Purpose
These projects are intended for educational use and can be extended with a graphical interface, saved data, or additional test cases.
