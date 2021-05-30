age=int(input("enter age:"))
if age < 5:
    print("too young to go to school")
elif age == 5:
    print("go to kindergarden")
elif (age > 5) and (age <= 17):
    grade = age-5
    print("go to grade {}".format(grade))
else:
    print("go to college")
