# Task Scheduler
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# ***** Greedy approach *******

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cooldown = {}  # task as key and (delay, count) as value

        for task in tasks:
            if task in cooldown:
                val = cooldown[task]
                cooldown[task] = (val[0], val[1] + 1)
            else:
                cooldown[task] = (0, 1)

        cycle = 0

        while True:
            cycle += 1
            # pick the valid tasks
            task = None
            maxc = 0
            for k, v in cooldown.items():
                if cycle > v[0] and v[1] > maxc:
                    maxc = v[1]
                    task = k

            # if there is a valid task, choose it
            if task is not None:
                val = cooldown[task]
                if val[1] == 1:
                    del cooldown[task]
                else:
                    cooldown[task] = (cycle + n, val[1] - 1)

            if not len(cooldown):
                break

        return cycle