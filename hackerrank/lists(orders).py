
def func(*input):
    input=list(input)
    print(input,type(input))
func(20,30,10)
marks=[20,30,10,23]
marks.insert(1,56)
marks.append(80)
print(marks)

if __name__ == '__main__':
    N = int(input("N : "))
    lst = []


    def task(inp,lst):
        if inp[0] == 'print':
            print(lst)
        elif inp[0] == 'reverse':
            lst = lst.reverse()
        elif inp[0] == 'insert':
            lst = lst.insert(int(inp[1]), int(inp[2]))
        elif inp[0] == 'remove':
            lst = lst.remove(int(inp[1]))
        elif inp[0] == 'sort':
            lst.sort()
        elif inp[0] == 'pop':
            lst.pop()
        elif inp[0] == 'append':
            lst.append(int(inp[1]))

    for i in range(N):
        inp1 = input("input : ")
        inp = inp1.split()
        task(inp,lst)


mark=[89,7,89,90]
mark.remove(7)
print(mark)