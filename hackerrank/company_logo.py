import copy
# !/bin/python3

import math
import os
import random
import re
import sys
import copy


def print_this(s):
    def get_all_max(lst, num):
        lst2 = []
        for i in range(len(lst)):
            if (num == lst[i]):
                lst2.append(i)
                lst[i] = 's'
        return lst2

    word_map = {}
    str = s
    for i in range(len(str)):
        if str[i] in word_map:
            word_map[str[i]] += 1
        else:
            word_map[str[i]] = 1
    # print(word_map)
    word_key = list(word_map.keys())
    word_value = list(word_map.values())

    word_value_dummy = copy.deepcopy(word_value)
    word_value_dummy.sort()
    max_value = word_value_dummy[-1]
    max_value2 = word_value_dummy[-2]
    max_value3 = word_value_dummy[-3]
    # word_value_dummy2 = copy.deepcopy(word_value)

    lst2 = get_all_max(word_value, max_value)
    lst3 = []
    for i in range(len(lst2)):
        lst3.append(word_key[lst2[i]])
        lst3.sort()

    # print("this is lst2 {}".format(lst2))
    # print("this is max_value2 {}".format(max_value2))
    lst2 = get_all_max(word_value, max_value2)
    lst4 = []
    for i in range(len(lst2)):
        lst4.append(word_key[lst2[i]])
        lst4.sort()

    lst2 = get_all_max(word_value, max_value)
    lst5 = []
    for i in range(len(lst2)):
        lst5.append(word_key[lst2[i]])
        lst5.sort()
    lst6=[]
    lst7=[]
    # print(word_value)
    # print(lst2)
    # print("this is lst3 that is max_value {}".format(lst3))
    # print("this is lst3 that is max_value2 {}".format(lst4))
    # print("this is lst3 that is max_value3 {}".format(lst5))
    for i in range(len(lst3)):
        lst6.append(lst3[i])
        lst7.append(max_value)
    for i in range(len(lst4)):
        lst6.append(lst4[i])
        lst7.append(max_value2)
    for i in range(len(lst5)):
        lst6.append(lst5[i])
        lst7.append(max_value3)
    for i in range(3):
        print(lst6[i],lst7[i])


if __name__ == '__main__':
    s = input()
    print_this(s)