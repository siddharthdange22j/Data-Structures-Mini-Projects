# Job Scheduling Using Graphs

## 1. Introduction
In many projects, some jobs must be completed before other jobs can begin. For example, testing an application must happen after the application has been developed.

This project represents jobs and their dependencies using a directed graph, then finds a valid job order using topological sorting.

## 2. Problem Statement
Develop a program that schedules jobs according to their dependencies. A job must not be scheduled before its prerequisite jobs. The program must also detect a cycle, because cyclic dependencies make a valid schedule impossible.

## 3. Aim
To implement job scheduling using a directed graph and topological sorting.

## 4. Objectives
- Represent jobs as vertices (nodes).
- Represent dependencies as directed edges.
- Store the graph using an adjacency list.
- Calculate each job's in-degree.
- Use Kahn's algorithm to find a valid schedule.
- Detect cycles in the dependency graph.

## 5. Graph Concepts Used

### Vertex (Node)
A vertex represents one job, such as `A - Collect requirements`.

### Directed Edge
An edge `A -> B` means job A must be completed before job B can begin.

### In-degree
The in-degree of a job is the number of prerequisite jobs that must be completed before it can be scheduled.

### Topological Sorting
Topological sorting produces an order of vertices in a directed acyclic graph (DAG) such that every prerequisite appears before the job that depends on it.

### Kahn's Algorithm
Kahn's algorithm repeatedly schedules jobs whose in-degree is zero. When a job is scheduled, it reduces the in-degree of the jobs that depend on it.

## 6. Example Dependency Graph
```text
           A
          / \
         B   C
          \ /
           D
           |
           E
```
- A: Collect requirements
- B: Design the system (depends on A)
- C: Prepare the database (depends on A)
- D: Develop the application (depends on B and C)
- E: Test the application (depends on D)

One valid schedule is `A, B, C, D, E`. B and C may be scheduled in either order.

## 7. Algorithm
1. Create a list of jobs.
2. Create an adjacency list for the directed graph.
3. For every dependency `A -> B`, add B to A's outgoing-neighbor list and increase B's in-degree by one.
4. Put all jobs with in-degree zero into a queue.
5. Remove a job from the queue and append it to the schedule.
6. For each job that depends on the removed job, reduce its in-degree by one.
7. If a dependent job's in-degree becomes zero, add it to the queue.
8. Repeat until the queue is empty.
9. If every job is scheduled, display the schedule.
10. If some jobs remain unscheduled, report a cycle and explain that no valid schedule exists.

## 8. Pseudocode
```text
CALCULATE in-degree for every job
ADD every zero-in-degree job to queue
schedule = empty list

WHILE queue is not empty:
    job = REMOVE front of queue
    ADD job to schedule

    FOR each dependent job:
        DECREASE dependent job's in-degree
        IF its in-degree is zero:
            ADD it to queue

IF schedule contains every job:
    DISPLAY schedule
ELSE:
    DISPLAY cycle error
```

## 9. Example
Jobs:
- A: Collect requirements
- B: Design the system
- C: Prepare the database
- D: Develop the application
- E: Test the application

Dependencies:
- A must be completed before B.
- A must be completed before C.
- B must be completed before D.
- C must be completed before D.
- D must be completed before E.

A valid result:
```text
A -> B -> C -> D -> E
```
The order of B and C can be swapped and still be valid.

## 10. Complexity Analysis
Let `V` be the number of jobs (vertices) and `E` be the number of dependencies (edges).
- **Time Complexity:** `O(V + E)` using an adjacency list and Kahn's algorithm.
- **Space Complexity:** `O(V + E)` to store the graph, in-degrees, queue, and schedule.

## 11. Applications
- Planning software development tasks.
- Scheduling steps in a project workflow.
- Ordering build tasks in software systems.
- Course planning when prerequisites exist.
- Organizing manufacturing or data-processing steps.

## 12. Advantages
- Ensures prerequisites appear before dependent jobs.
- Detects impossible schedules caused by cycles.
- Supports independent jobs that can appear in either order.
- Efficient for sparse dependency graphs.

## 13. Limitations
- The project determines a valid order; it does not estimate job durations or optimize staff and resource allocation.
- The dependencies must be supplied correctly.
- A valid topological order exists only when the graph has no directed cycle.

## 14. How to Run
Make sure Python 3.8 or newer is installed. In a terminal, run:
```bash
python job_scheduling.py
```
If your system uses `python3`, run:
```bash
python3 job_scheduling.py
```

## 15. Conclusion
This project demonstrates how graphs represent dependencies and how topological sorting creates a valid order for jobs. Cycle detection prevents the program from presenting an invalid schedule.
