rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("-------------------------------------")

rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("-------------------------------------")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(i, end="")
    print()

print("-------------------------------------")

rows = 5
for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end="")
    print()

print("-------------------------------------")

rows = 5
num = 1
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(num, end=" ")
        num += 1
    print()

print("-------------------------------------")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("--------------------------------------")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("---------------------------------------")

rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()

print("----------------------------------------")

