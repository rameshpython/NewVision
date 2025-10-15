for i in range(1,4):
    for j in range(1,4):
        print(i,j)
print("--------------------------------------------")
for i in range(1, 4): # Outer loop (rows)
    for j in range(i): # Inner loop (columns)
        print("*", end="")
    print()

print("--------------------------------------------")
rows = 5
for i in range(1, rows+1):
    for j in range(i):
        print("*", end="")
    print()

print("---------------------------------------------")

rows=5
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end="")
    print()
print("----------------------------------------------")
rows=5
for i in range(rows,1,-1):
    for j in range(i):
        print("*",end="")
    print()
print("-----------------------------------------------")
rows=5
for i  in range(2,rows+1):
    for j in range(i):
        print("*",end="")
    print()

print("------------------------------------------------")

rows=5
for i  in range(3,rows+1):
    for j in range(i):
        print("*",end="")
    print()
print("-------------------------------------------------")
rows = 5
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print("-------------------------------------------------")

rows=5
for i in range(rows,0,-1):
    print(""*(rows-i)+"*"*(2*i-1))

print("--------------------------------------------------")

rows = 5
# Upper part
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
# Lower part
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))