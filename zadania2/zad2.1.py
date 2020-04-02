counter = 0
zdanie = input("Wpisz zdanie")
for litera in zdanie:
    if litera == " ":
        counter = counter + 1
print(counter)
