class Solution:
    def maxDepth(self, s: str) -> int:
        # my way
        if "(" in s and ")" in s:
            ptx = [0]
            for char in s:
                if char == "(":
                    ptx.append(ptx[-1] + 1)
                elif char == ")":
                    ptx.append(ptx[-1] - 1)

            return max(ptx)
        else:
            return 0

        # a solution i liked
        result = counter = 0
        for char in s:
            if char == "(":
                counter += 1
                result = max(result, counter)
            elif char == ")":
                counter -= 1
        return result