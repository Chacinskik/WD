def fibonacci():
    a=0
    b=1
    while True:
        yield b
        temp=a+b
        a=b
        b=temp

fib=fibonacci()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))