'''
n = input()
count = 0
for i in n:
    if i in "aeiouAEIOU":
        count+=1
print(count)
'''
'''
#ข้อ3
n = str(input())
data = []
count = 0
while True:
    h = str(input())
    if(h == "0"):
        break
    data.append(h)
for x in n:
    if(x in data):
        count += 1
print("{}/{}".format(count,len(n)))
'''
'''
#3
n = input()
b = []
for i in n:
    if not (i in "aeiouAEIOU"):
        print(i, end='')
'''
'''
num = int(input())
i = 1
k = 1
m = (num*2)-1
while i <= num:
    print('|',end = '')
    print("{:^{o}s}".format('*'*k, o=m),end='')
    print('|')
    k+=2
    i += 1
'''
'''
#05
s = input()
cheak = input()
num = 0
for i in s:
    if i in cheak:
        num += 1
if len(s)==2:
    print('0\n{:.2f}'.format((len(s)-2)*100))
elif len(s)>2:
    print('{}\n{:.2f}'.format(num, (num/(len(s)-2))*100))
'''
def look(a):
    if a in "aeiou":
        return True
def cheak(x):
    if len(x) < 3:
        return x
    elif look(x[0]) and x[1] == 'p' and x[2] == x[0]:
        return x[0] + cheak(x[3:])
    else:
        return x[0] + cheak(x[1:])
word = input()
print(cheak(word))