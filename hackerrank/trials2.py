
s = 'atring same in ring is the ringer'
s1 = 'ring'
m = len(s1)
n=0
count=0
for i in range(len(s)):
    if s[n:n+m] == s1:
        count+=1
        n+=1
    else:
        n+=1
print(count)

