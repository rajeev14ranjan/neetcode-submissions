# Gas Station
# There are n gas stations along a circular route. You are given two integer arrays gas and cost where:

# gas[i] is the amount of gas at the ith station.
# cost[i] is the amount of gas needed to travel from the ith station to the (i + 1)th station. (The last station is connected to the first station)
# You have a car that can store an unlimited amount of gas, but you begin the journey with an empty tank at one of the gas stations.

# Return the starting gas station's index such that you can travel around the circuit once in the clockwise direction. If it's impossible, then return -1.

# It's guaranteed that at most one solution exists.
# ******** calculating the difference for actual gas, then finding a point from where sum is positive till the end.


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0  # this will check if solution is feasible.
        tank = 0
        start = 0
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            tank += diff
            total += diff

            if tank < 0:  # it has became negative so this start won't work
                start = i + 1
                tank = 0

        return start if total >= 0 else -1
