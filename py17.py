'''a=int(input("enter value:"))
b=int(input("enter another value:"))
a=a+b
b=a-b
a=a-b
print("the value of a:",a)
print("the value of b:",b)'''

'''val=int(input("enter value:"))
if val==0:
    exit()
else:
    print("print the entered value:",val)'''


'''val=int(input("enter an integer value:"))
flt=eval(input("enter any float value:"))
str=input("enter any string:")
if val==0:
    exit()
else:
    print("here the value enter by u")
    print("interger value",val)
    print("float value",flt)
    print("string",str)'''


'''print("enter 2 numbers from user:")
val1=eval(input())
val2=eval(input())
if val1==0:
    exit()
else:

    sum=val1+val2
    print("sum is=",sum)'''

'''ch=input("enter any character:")
if(ch>='a' and ch<='z') or (ch>='A' and ch <='Z'):
    print(ch, "is an alphabet")
else:
    print(ch,"is not an alphabet")'''

'''def convert(s):
    s1=''
    for i in s:
        if ord(i)>=97 and ord(i)<=122:
            s1=s1+chr(ord(i)-32)
        elif ord(i)>=65 and ord(i)<=90:
            s1=s1+chr(ord(i)+32)
        else:
            s1=s1+i
    return s1
s="I am learning python"
print(convert(s))'''

'''for i in range(5):
    if i ==3:
        continue
    print(i)'''


'''n=int(input("enter no of element to be inserted"))
a=[]
for i in range(0,n):
    b=int(input("enter element"))
    a.append(b)
avg =sum(a)/n
print("avg:",avg)'''


'''
'''class father:
    tech='java'
    def designation(self):
        print('manager')

class son:
    tech="python"
    def designation(self):
        print('clerk')
f1=father()
print(f1.tech)
f1.designation()
s1=son()
print(s1.tech)
s1.designation()'''

overloading

'''class student
    def add(self,m1=none,m2=none,m3=none):''''''


class A:
    __pin = 1234

    def __feture1(self):
        print(A.__pin)

    def A_pin(self):
        self.__feture1()


a = A()
a.A_pin()







