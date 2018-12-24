list1=[10,8,-1,100,35,200]
max=0
for i in range(0,6):
    if max<list1[i]:
        max=list1[i]
print(max)

'''
sum=0
for i in range(1,9):
    n=int(input('输入第%d个数:'%i))
    sum=sum+n
avg=sum/8
avg=round(avg,2)
print(avg)
'''

a=[1,4,3,2,6]
a1=[]
for i in a:
    a1.append(i)
b=sorted(a)
print(b)
print(b[-2])
print(b[len(b)-2])
print(a1.index(b[-2]))
print(a1)


a='dkagifglah;'

print(a[1:])
print(a[-4:-1])
print(a[3:7])  #都是包头不包尾