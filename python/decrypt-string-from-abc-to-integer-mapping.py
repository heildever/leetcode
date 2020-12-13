def freqAlphabets(self, s: str) -> str:
    abc = "#abcdefghijklmnopqrstuvwxyz"
    result, idx = "", 0
    length = len(s)
    while length > idx:
        if length > idx + 2 and s[idx + 2] == "#":
            result += abc[int(s[idx:idx + 2])]
            idx += 3
        else:
            result += abc[int(s[idx])]
            idx += 1

    return result
