class CyclicIterator:
    def __init__(self, obj):
        self.obj = obj
        self.cursor = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.cursor == len(self.obj) - 1:
            self.cursor = -1
        self.cursor += 1
        return self.obj[self.cursor]


gen = CyclicIterator(['a', 'b', 'c'])
for i in gen:
    print(i)
