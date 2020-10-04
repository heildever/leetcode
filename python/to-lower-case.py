# one-liner would be string.lower(), didn't include that since
# one-liners are not always desirable


class Solution:
    def toLowerCase(self, string: str) -> str:
        final_str = ""
        for char in string:
            if char.islower():
                final_str += char
            else:
                final_str += char.lower()
        return final_str
