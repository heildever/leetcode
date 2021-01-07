# question can be found on leetcode.com/problems/desinging-hashset/


class HashSet:
    def __init__(self):
        self.hashset = [None] * 100_000

    def add(self, key: int) -> None:
        hashed_key = hash(key)
        if not self.hashset[hashed_key]:
            self.hashset[hashed_key] = key

    def remove(self, key: int) -> None:
        hashed_key = hash(key)
        if self.hashset[hashed_key]:
            self.hashset[hashed_key] = None

    def contains(self, key: int) -> None:
        hashed_key = hash(key)
        return self.hashset[hashed_key] is not None
