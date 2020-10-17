# question can be found on leetcode.com/problems/desinging-hashmap/


class MyHashMap:
    def __init__(self):
        self.hashmap = [None] * 100_000

    def put(self, key: int, value: int) -> None:
        key_hash = int(hash(key))
        self.hashmap[key_hash] = value

    def get(self, key: int) -> int:
        key_hash = int(hash(key))
        if self.hashmap[key_hash] is not None:
            return self.hashmap[key_hash]
        else:
            return -1

    def remove(self, key: int) -> None:
        key_hash = int(hash(key))
        if self.hashmap[key_hash] is not None:
            self.hashmap[key_hash] = None
