row=5
for i in range(1,row+1):
    for j in  range(1,i+1):
        print(j,end="")
    print()

print("-------------------------")
rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print(i,end="")
    print()

print("--------------------------")

rows=5
for i in range(rows,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("-----------------------------")

rows=5
for i in range(1,row+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

print("------------------------------")

rowws=5
num=1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end="")
    print()

print("-------------------------------")

rows =5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
print("-------------------------------")
rows = 5
for i in range(1, rows + 1):
    for j in range(65, 65 + i):     # 65 = ASCII value of 'A'
        print(chr(j), end="")
    print()

print("---------------------------------")
rows = 5
for i in range(rows, 0, -1):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

print("--------------------------------")

rows = 5
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(64 + i), end="")   # 64 + 1 = 65 → 'A'
    print()

print("----------------------------------")
rows = 5
ch = 65
for i in range(1, rows + 1):
    for j in range(i):
        print(chr(ch), end=" ")
        ch += 1
    print()
print("-----------------------------------")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()

print("-----------------------------------")

rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end="")
    for j in range(65 + i - 2, 64, -1):
        print(chr(j), end="")
    print()

print("----------------------------------")
rows = 5
for i in range(rows, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end="")
    for j in range(65 + i - 2, 64, -1):
        print(chr(j), end="")
    print()

print("-----------------------------------")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    print()






