n = int(input("enter a number "))
m = (n-1)*2

def print_one_line(n,i):
    num = n
    str = ""
    while(num>=1):
        str += (chr(num+96+i)+"-")
        num -= 1
    num += 2
    while(num<=n):
        str += (chr(num+96+i)+"-")
        num += 1
    return str[(2*i):-(2*i)-1]
#
# str = print_one_line(n,1)
# print(str.rjust(10,"-"))
for i in range(n-1,0,-1):
    string = print_one_line(n,i)
    string = string.rjust(2*m-2*i+1,"-")
    string = string.ljust(2*m+1,"-")
    print(string)
for i in range(n):
    string = print_one_line(n,i)
    string = string.rjust(2*m-2*i+1,"-")
    string = string.ljust(2*m+1,"-")
    print(string)


# the submissions of ALPHABET_RANGOLI
def print_rangoli(size):
    alp = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(size - 1, -size, -1):
        temp = '-'.join(alp[size - 1:abs(i):-1] + alp[abs(i):size])
        print(temp.center(4 * size - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

