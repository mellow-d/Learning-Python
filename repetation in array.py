
# trying to find first repeating number in list

#     for else
#     break and continue

print("hello world")
integer_inp = input("enter some numbers/charecter(with spaces) : ")
integers = integer_inp.split()
# print(type(integer_inp))
# print(type(integers))
lst=[integers[0]]
for i in range(1,len(integers)):
    for j in range(len(lst)):
        if (integers[i]==lst[j]):
            print(integers[i],"is the first repeating number/charecter ")
            break
    else:                                          #<-------
        continue
    break
    lst.append(integers[i])






