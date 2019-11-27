class FileReader():
    def __init__(self, path):
        self.path = path

    def read(self):
        try:
            f = open(self.path, "r")
        except IOError:
            return ""
        else:
            return f.read()
