def parzyste(wyraz):
    for i in range(0, len(wyraz), 2):
        yield wyraz[i]

gen = parzyste("abcdefghi")
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
