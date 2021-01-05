def solve(s):
    flag= False
    string=''
    for i in s:
        if flag==False and 96<ord(i)<123  :
           j=ord(i)-32
           string+=chr(j)
           flag=True
        elif ord(i)==32:
            flag=False
            string+=i
        elif ord(i)!=32:
            flag=True
            string+=i
    return string
string=input("enter a string:\n")
cap_string = solve(string)
print(cap_string)