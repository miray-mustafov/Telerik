def list_of_size(size):
    return [None] * size


# does not handle collisions
class HashTable():
    FILL_FACTOR = 0.75

    def __init__(self):
        self._buckets = list_of_size(3)
        self._count = 0

    def add(self, item):
        if self._count / len(self._buckets) > HashTable.FILL_FACTOR:
            self._resize()

        index = hash(item) % len(self._buckets)

        self._buckets[index] = item
        self._count += 1

    def has(self, item):
        index = hash(item) % len(self._buckets)
        target = self._buckets[index]

        return target is not None and target == item

    def get_items(self):
        return [item for item in self._buckets if item is not None]

    def _resize(self):
        new_buckets = list_of_size(len(self._buckets) * 2)
        for item in self._buckets:
            if item is not None:
                index = hash(item) % len(new_buckets)
                new_buckets[index] = item

        self._buckets = new_buckets

    # used by the len() function
    def __len__(self):
        return self._count


ht = HashTable()
ht.add('hello')
ht.add('test')
ht.add('me')
ht.add('please')
ht.add('mr')
ht.add('hash')
ht.add('table')
ht.add('san')
ht.add('all')
ht.add('right')
ht.add('all right')
ht.add('all riiiiight')

print(ht.get_items())
print(ht.has('hello'))

print(len(ht))
