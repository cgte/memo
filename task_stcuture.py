# Originally published by https://github.com/akx on https://stackoverflow.com/a/67475808/7154688


import concurrent.futures


def do_task(task_id, results, dependencies):
    # sanity check - this function could use `dependencies` and `results` too
    assert all(dep in results for dep in dependencies)
    return f"Task {task_id} completed with result {task_id * 42}"


def run_graph(task_dependencies, runner):
    # Dict for results for each task.
    results = {}
    # Set of tasks yet to be completed.
    todo = set(task_dependencies)

    with concurrent.futures.ThreadPoolExecutor() as executor:
        # While there are items in the to-do set...
        while todo:
            # ... figure out what we can immediately execute by
            # comparing the dependency set to the result keys we already have
            # (i.e. the complement of the to-do set)
            next_tasks = {
                task_id
                for (task_id, deps) in task_dependencies.items()
                if task_id in todo and set(deps) <= set(results)
            }
            # If there are no next tasks we could schedule, it means the dependency
            # graph is incorrect (or at the very least incompleteable).
            if not next_tasks:
                raise RuntimeError(
                    f"Unable to schedule tasks, bad dependencies? Todo: {todo}"
                )

            print("Scheduling", next_tasks)
            # Submit tasks for execution in parallel. `futures` will be a list of
            # 2-tuples (task_id, future).
            futures = [
                (
                    task_id,
                    executor.submit(
                        runner, task_id, results, task_dependencies[task_id]
                    ),
                )
                for task_id in next_tasks
            ]

            # Loop over the futures, waiting for their results; when a future
            # finishes, save the result value and remove that task from the
            # to-do set.
            for (task_id, future) in futures:
                results[task_id] = future.result()
                todo.remove(task_id)
    # Once the while loop finishes, we have our results.
    return results


if __name__ == "__main__":
    task_deps = {
        1: (),
        2: (1,),
        3: (1,),
        4: (1,),
        5: (2,),
        6: (3,),
        7: (4,),
        8: (5,),
        9: (6,),
        10: (7,),
        11: (8,),
        12: (9,),
        13: (10,),
        14: (11, 12),
        15: (14, 13),
    }

    result = run_graph(task_deps, do_task)
    print(result)
