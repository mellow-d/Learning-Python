file = open(r'D:\file handle\file handling.csv','r')
file1 = ''
for each in file:
    file1 += each.replace("," ," // ")
file.close()

file = open(r'D:\file handing successful.txt','w')
file.write(file1)
file.close()


gamer = []
file = open(r'D:\file handing successful.txt','r')
for each in file:
    gamer.append(each.split('//')[0])
gamer="\n".join(gamer)
file.close()

file = open(r'D:\file handing successful2.txt','w')
file.write(gamer)
file.close()


