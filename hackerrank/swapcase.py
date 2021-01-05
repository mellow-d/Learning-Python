def swap_case(s):
    string = ""

    for i in s:

        if 65 <= ord(i) <= 90:
            charr = chr(ord(i) + 32)
            string += charr

        elif 97 <= ord(i) <= 122:
            charr = chr(ord(i) - 32)
            string += charr

        else:
            string += i

    return string


if __name__ == '__main__':
    s = input("enter the string")
    result = swap_case(s)
    print(result)
# hello world