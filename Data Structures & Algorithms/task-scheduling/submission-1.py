# Task Scheduler
# You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.
# Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.
# The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.
# Return the minimum number of CPU cycles required to complete all tasks.

# ***** Math approach *******

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count how often each task appears. A dict only stores tasks that
        # actually occur, instead of a fixed 26-slot list for every letter.
        count = {}
        for task in tasks:
            count[task] = count.get(task, 0) + 1

        # The most frequent task is the bottleneck: it forces the layout.
        # If A appears maxf times with cooldown n, we are forced into:
        #     A _ _ _ | A _ _ _ | A
        # i.e. (maxf - 1) frames, each (n + 1) wide (the task + n cooldown
        # slots), followed by a final A.
        maxf = max(count.values())

        # How many tasks tie for that max frequency. They all share the LAST
        # frame, so the tail is maxCount wide, not 1. E.g. A and B both x3:
        #     A B _ | A B _ | A B   -> last column holds both A and B.
        maxCount = sum(1 for c in count.values() if c == maxf)

        # (maxf - 1) complete frames of width (n + 1), plus the final partial
        # frame holding every max-frequency task.
        time = (maxf - 1) * (n + 1) + maxCount

        # If there are many distinct tasks, the gaps get filled by real work
        # and no idling is needed. In that case the answer is simply the total
        # number of tasks, which can exceed the formula above.
        return max(len(tasks), time)