n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(""*(n-i),"*"*i,end="")
    print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
        print()

num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(""*(i-1),end="")
    for j in range(1,num+2-i):
        print("*",end="")
    for k in range(1,num+1):
        print("*",end="")
    print()


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print("*"*n)


n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
    print()