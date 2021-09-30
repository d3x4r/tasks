class Open():
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.fp = open(self.file, self.mode)
        return self.fp

    def __exit__(self, exp_type, exp_value, traceback):
        self.fp.close()


with Open('test.txt', 'w') as fp:
    fp.write('text')