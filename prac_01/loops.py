for i in range(1, 21, 2):
    print(i, end=' ')
print()
for i in range(0, 101, 10):
    print(i, end=' ')
print()
for i in range(20, 0, -1):
    print(i, end=' ')
print()
stars_number = int(input("stars number: "))
for i in range(stars_number):
    print('*', end=' ')
print()
for i in range(1, stars_number + 1):
    print('*' * i)
print()