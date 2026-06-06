# Car Fleet
# There are n cars traveling to the same destination on a one-lane highway.

# You are given two arrays of integers position and speed, both of length n.

# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.

# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.

# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.

# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.

# Return the number of different car fleets that will arrive at the destination.
# ********* [Non Intuitive] *********

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Pair up cars and sort by position, closest to the target first.
        cars = sorted(zip(position, speed), reverse=True) # key=lambda x: x[0]

        fleets = 0
        lead_time = 0.0  # arrival time of the fleet currently in front

        for pos, spd in cars:
            time = (target - pos) / spd
            if time > lead_time:
                # This car can't catch the fleet ahead -> it's a new fleet.
                fleets += 1
                lead_time = time
            # else: it catches up (or meets at the target) -> joins the fleet ahead.

        return fleets
                


