class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        self.index +=2
        if self.index >= len(self.data):
            raise StopIteration
        return self.data[self.index]


elo=Parzyste("Hej")
witaj=iter(elo)
print(next(witaj))
print(next(witaj))
print(next(witaj))