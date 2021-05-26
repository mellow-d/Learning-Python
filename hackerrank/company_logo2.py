str = input("enter string ")
word_map = {}
for i in range(len(str)):
    if str[i] in word_map:
        word_map[str[i]] += 1
    else:
        word_map[str[i]] = 1
# print(word_map)
word_key = list(word_map.keys())
word_value = list(word_map.values())
print(word_map)
print(word_value)
print(word_key)
max_lst=[]
def get_max_out(word_value,word_key,max_lst): #to get maximum out of list of word_value
    lst1=[]
    var = max(word_value)
    for i in range(len(word_value)):
        if word_value[i] == var:
            lst1.append(word_key[i])
            word_value[i] = -1
            max_lst.append(var)
    lst1.sort()
    return lst1
lst = get_max_out(word_value,word_key,max_lst)
lst2 =get_max_out(word_value,word_key,max_lst)
for i in range(len(lst2)):
    lst.append(lst2[i])
lst3 = get_max_out(word_value,word_key,max_lst)
for i in range(len(lst3)):
    lst.append(lst3[i])
for i in range(3):
    print(lst[i],max_lst[i])


#discussions
from collections import Counter

chars = Counter(input()).items()
print(chars)

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)

