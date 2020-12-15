# question can be found at leetcode.com/problems/leetcode.com/problems/goal-parser-interpretation/


class Solution:
    def interpret(self, command: str) -> str:
        result, idx = "", 0
        while len(command) > idx:
            if command[idx] == "G":
                result += "G"
                idx += 1
            else:
                if command[idx + 1] == "a":
                    result += "al"
                    idx += 4
                else:
                    result += "o"
                    idx += 2

        return result
