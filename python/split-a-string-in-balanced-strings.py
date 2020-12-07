class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # my way
        stack = [0]
        for char in s:
            if char == "R":
                stack.append(stack[-1] + 1)
            elif char == "L":
                stack.append(stack[-1] - 1)
        return stack.count(0) - 1

        # one could rely on only "R" and "L" will be in s
        result = counter = 0
        # here counter keeps the tab for "RL" matches
        for char in s:
            if char == "R":
                counter += 1
            else:
                counter -= 1

            if counter == 0:
                result += 1

        return result
