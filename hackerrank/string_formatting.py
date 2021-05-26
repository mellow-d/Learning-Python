def print_formatted(number):
    def binary(num):
        return bin(num).replace('0b', '')

    def hexadecimal(num):
        a = hex(num).replace('0x', '')
        return a.upper()

    def octal(num):
        return oct(num).replace('0o', '')

    def formatting(num):
        lst = []
        lst.append(str(num))
        lst.append(octal(num))
        lst.append(hexadecimal(num))
        lst.append(binary(num))
        str_ing = ""
        str_ing = str_ing + str(lst[0]).rjust(7)
        str_ing = str_ing + str(lst[1]).rjust(7)
        str_ing = str_ing + str(lst[2]).rjust(7)
        str_ing = str_ing + str(lst[3]).rjust(7)


        return str_ing

    for i in range(1, number + 1):
        string = formatting(i)
        print(string)


    # print(string[:len(string) - 1])
    # your code goes here
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)