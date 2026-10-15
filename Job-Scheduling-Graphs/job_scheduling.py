"""Job scheduling using a directed graph and Kahn's topological sort."""

from collections import deque


def schedule_jobs(jobs, dependencies):
    """
    Return (schedule, has_cycle).

    Each dependency is a pair (prerequisite, dependent), meaning the
    prerequisite job must be completed before the dependent job.
    """
    graph = {job: [] for job in jobs}
    in_degree = {job: 0 for job in jobs}

    for prerequisite, dependent in dependencies:
        if prerequisite not in graph or dependent not in graph:
            raise ValueError(
                f"Unknown job in dependency: {prerequisite} -> {dependent}"
            )
        graph[prerequisite].append(dependent)
        in_degree[dependent] += 1

    ready = deque(job for job in jobs if in_degree[job] == 0)
    schedule = []

    while ready:
        current_job = ready.popleft()
        schedule.append(current_job)

        for dependent in graph[current_job]:
            in_degree[dependent] -= 1
            if in_degree[dependent] == 0:
                ready.append(dependent)

    has_cycle = len(schedule) != len(jobs)
    return schedule, has_cycle


def display_schedule(jobs, descriptions, dependencies):
    print("\nJobs:")
    for job in jobs:
        print(f"  {job} - {descriptions[job]}")

    print("\nDependencies:")
    if dependencies:
        for prerequisite, dependent in dependencies:
            print(f"  {prerequisite} must finish before {dependent}")
    else:
        print("  No dependencies")

    schedule, has_cycle = schedule_jobs(jobs, dependencies)

    print("\nGenerated Job Schedule:")
    if has_cycle:
        print("A valid schedule cannot be generated.")
        print("Reason: A cycle exists in the job dependencies.")
        scheduled = set(schedule)
        blocked = [job for job in jobs if job not in scheduled]
        print("Jobs blocked by the cycle:", ", ".join(blocked))
    else:
        for number, job in enumerate(schedule, start=1):
            print(f"{number}. {job} - {descriptions[job]}")
        print("\nAll jobs can be scheduled successfully.")


def main():
    print("=" * 48)
    print("          JOB SCHEDULING SYSTEM")
    print("       Using Graphs and Topological Sort")
    print("=" * 48)

    # Example jobs for a college software project.
    jobs = ["A", "B", "C", "D", "E"]
    descriptions = {
        "A": "Collect requirements",
        "B": "Design the system",
        "C": "Prepare the database",
        "D": "Develop the application",
        "E": "Test the application",
    }
    # (prerequisite, dependent)
    dependencies = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("C", "D"),
        ("D", "E"),
    ]

    while True:
        print("\n1. Generate sample job schedule")
        print("2. Demonstrate cycle detection")
        print("3. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_schedule(jobs, descriptions, dependencies)
        elif choice == "2":
            print("\nCycle demonstration: A -> B -> C -> A")
            cycle_jobs = ["A", "B", "C"]
            cycle_descriptions = {
                "A": "Job A",
                "B": "Job B",
                "C": "Job C",
            }
            cycle_dependencies = [
                ("A", "B"),
                ("B", "C"),
                ("C", "A"),
            ]
            display_schedule(
                cycle_jobs, cycle_descriptions, cycle_dependencies
            )
        elif choice == "3":
            print("Thank you for using the Job Scheduling System!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()
