def list_of_size(size):
    return [None] * size


class HashTable:
    FILL_FACTOR = 0.75

    def __init__(self):
        self._buckets = list_of_size(3)
        self._count = 0

    def add(self, item):
        if self._count / len(self._buckets) > HashTable.FILL_FACTOR:
            self._resize()

        index = hash(item) % len(self._buckets)

        if self._buckets[index] is None:
            self._buckets[index] = []
        self._buckets[index].append(item)
        self._count += 1

    def has(self, item):
        index = hash(item) % len(self._buckets)
        bucket = self._buckets[index]
        if bucket is not None:
            for value in bucket:
                if value == item:
                    return True
        return False

    def get_items(self):
        items = []
        for bucket in self._buckets:
            if bucket is not None:
                items.extend(bucket)
        return items

    def _resize(self):
        new_buckets = list_of_size(len(self._buckets) * 2)
        for bucket in self._buckets:
            if bucket is not None:
                for item in bucket:
                    index = hash(item) % len(new_buckets)
                    if new_buckets[index] is None:
                        new_buckets[index] = []
                    new_buckets[index].append(item)
        self._buckets = new_buckets

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
