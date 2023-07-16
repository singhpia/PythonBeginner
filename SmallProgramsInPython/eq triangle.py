print("enter number of rows")
n=int(input())
for i in range(n):
    for j in range(n):
        print(end=' ')
    n=n-1
    for j in range(0,i):
        print("* ",end="")
    print("\r")
