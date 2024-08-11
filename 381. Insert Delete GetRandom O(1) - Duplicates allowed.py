import collections, random


class RandomizedCollection:

    def __init__(self):
        self.mapping = collections.defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        self.mapping[val].add(len(self.list))
        self.list.append(val)
        return len(self.mapping[val]) == 1

    def remove(self, val: int) -> bool:
        if self.mapping[val]:
            idx = self.mapping[val].pop()
            last = self.list[-1]
            last_idx = len(self.list) - 1
            self.list[idx] = last
            self.mapping[last].add(idx)
            self.mapping[last].discard(last_idx)
            self.list.pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()