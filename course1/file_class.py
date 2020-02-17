import os.path
import tempfile


class File():
    def __init__(self, path):
        self.path = path
        if not os.path.exists(self.path):
            with open(self.path, 'w'):
                pass
        with open(self.path, "r") as f:
            self.iterable = f.readlines()
        self.current = 0
        self.end = len(self.iterable) - 1

    def read(self):
        with open(self.path, "r") as f:
            text = f.read()
        return text

    def write(self, text):
        with open(self.path, "w") as f:
            f.write(text)

    def __str__(self):
        return self.path

    def __add__(self, other):
        tmp = File(os.path.join(tempfile.gettempdir(), "new"))
        with open(self.path, "r") as f:
            first = f.read()
        with open(other.path, "r") as f:
            second = f.read()
        to_write = first + second
        tmp.write(to_write)
        return tmp

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        result = self.iterable[self.current]
        self.current += 1
        return result

# file = File("test2.txt")
# file.write("line1,\nline 2,\n")
# for line in file:
#     print(ascii(line))