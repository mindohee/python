a = int(input())
b = a
c = 0
for i in range(a+1):
    b -= 1
    c += 1
    print(" "*c,"*"*(b+1))
