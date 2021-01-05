def print_formatted(number):
    def binary(num):
        return bin(num).replace('0b', '')

    def hexadecimal(num):
        return hex(num).replace('0x', '')

    def octal(num):
        return oct(num).replace('0o', '')

    def formatting(num):
        lst = []
        lst.append(str(num))
        lst.append(octal(num))
        lst.append(hexadecimal(num))
        lst.append(binary(num))
        string = '  '.join(lst)
        return string

    string = ''
    for i in range(1, number + 1):
        string += str(formatting(i)) + '\n'

    print(string[:len(string) - 1])

    # your code goes here


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)