import tempfile
import os
import uuid


class File:
    def __init__(self, file_name):
        self.file_name = file_name
        self.current = 0
        self.end = 0

        if not os.path.exists(file_name):
            with open(file_name, 'w'):
                pass

    def read(self):
        with open(self.file_name, 'r') as f:
            return f.read()

    def write(self, data):
        print(len(data))
        with open(self.file_name, 'w') as f:
            f.write(data)

    def __add__(self, obj):
        data = self.read() + obj.read()
        file_name = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()))
        f = File(file_name)
        f.write(data)
        return f

    def __str__(self):
        return self.file_name

    def __iter__(self):
        self.end = len(self.read())
        return self

    def __next__(self):
        if self.current >= self.end:
            self.current = 0
            raise StopIteration

        with open(self.file_name, 'r') as f:
            f.seek(self.current)
            line = f.readline()
            self.current = f.tell()
            return line
