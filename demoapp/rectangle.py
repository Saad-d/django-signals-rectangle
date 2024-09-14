# rectangle.py

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        self._index = 0
        return self

    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length': self.length}
        elif self._index == 1:
            self._index += 1
            return {'width': self.width}
        else:
            raise StopIteration

# Usage example
if __name__ == "__main__":
    rectangle = Rectangle(length=10, width=5)
    for dimension in rectangle:
        print(dimension)
