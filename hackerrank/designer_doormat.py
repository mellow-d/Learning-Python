inp = input().split()
n1 = int(inp[0])
n2 = int(inp[1])
n = int((n1 - 3) / 2)
m = int((n2 - 1) / 2)
img = ".|."

# this is the upper pattern
for i in range(1,n+2):
    for j in range(1, m - 3 * (i-1)):
        print("-", end="")
    for k in range(2 * i - 1):
        print(img, end="")
    for l in range(1,m - 3 * (i-1)):
        print("-", end="")
    print()

# this is the welcome line
for i in range(m-3):
    print("-",end="")
print("WELCOME",end="")
for i in range(m-3):
    print("-",end="")

print()

# this is the lower pattern
for i in range(n+1,0,-1):
    for j in range(1, m - 3 * (i-1)):
        print("-", end="")
    for k in range(2 * i - 1):
        print(img, end="")
    for l in range(1,m - 3 * (i-1)):
        print("-", end="")
    print()