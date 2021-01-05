if __name__ == '__main__':
    s = input("enter a string: ")
    n_alpha = False
    n_digit = False
    n_lower = False
    n_upper = False
    for i in s:
        if n_alpha == False:
            if i.isalpha() == True:
                n_alpha = True
        if n_digit == False:
            if i.isdigit() == True:
                n_digit = True
        if n_lower == False:
            if i.islower() == True:
                n_lower = True
        if n_upper == False:
            if i.isupper() == True:
                n_upper = True

    print(n_alpha or n_digit)
    print(n_alpha)
    print(n_digit)
    print(n_lower)
    print(n_upper)

