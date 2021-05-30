'''a=int(input("take no:"))
if a>0:
    print("positive")
elif a==0:
    print("not postive not negative")
else:
    print("negative")'''



s1=eval(input("enter student1 marks:"))
s2=eval(input("enter student2 marks:"))
s3=eval(input("enter student3 marks:"))
s4=eval(input("enter student4 marks:"))
s5=eval(input("enter student5 marks:"))
grade=(s1+s2+s3+s4+s5)/5
print("grade:",grade)
if grade>90:
    print("outstanding")
elif grade>80 and grade<=90:
    print("excelect")
elif grade>70 and grade<=80:
    print("good")
elif grade>60 and grade<=70:
    print("average")
else:
    print("rest r satisfactory")

