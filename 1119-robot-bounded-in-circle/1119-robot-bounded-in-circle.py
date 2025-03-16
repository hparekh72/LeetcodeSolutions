# TC: O(n)
# SC: O(1)


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos = [0, 0]
        direction = "North"
        antiClockwiseDirections = ["North", "West", "South", "East"]
        clockwiseDirections = ["North", "East", "South", "West"]

        for i in range(4):
            for char in instructions:
                if char == "G":
                    if direction == "North":
                        pos[1] += 1
                    elif direction == "South":
                        pos[1] -= 1
                    elif direction == "West":
                        pos[0] -= 1
                    else:
                        pos[0] += 1
                elif char == "L":
                    index = antiClockwiseDirections.index(direction)
                    direction = antiClockwiseDirections[(index + 1) % 4]
                else:
                    index = clockwiseDirections.index(direction)
                    direction = clockwiseDirections[(index + 1) % 4]

            if pos == [0, 0]:
                return True
        return False

        