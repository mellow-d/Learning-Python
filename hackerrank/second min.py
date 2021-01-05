print('Will print you the second minimum of number of participants')

if __name__ == '__main__':
    records = []
    for _ in range(int(input('enter number of participants: '))):
        name = input('name: ')
        score = float(input('score: '))
        j = [name, score]
        records.append(j)

    lst = []
    for i in range(len(records)):
        lst.append(records[i][1])


    def second_min(lst):
        x = lst.count(min(lst))
        for i in range(x):
            lst.remove(min(lst))
        return min(lst)


    var = second_min(lst)
    print(r"People with second minimum scores(i.e.{marks}) : ".format(marks=var))
    for i in range(len(records) - 1, -1, -1):
        if records[i][1] == var:
            print(records[i][0])
#bETTER way to know second Min or Max
print(set(lst))
lst2 =list(set(lst))
lst2.sort()
print('second min',lst2[1])