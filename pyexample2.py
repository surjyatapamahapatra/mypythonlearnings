num_1, num_2= input("enter 2 numbers:").split()
num_1=int(num_1)
num_2=int(num_2)
sum_1=num_1 + num_2
difference=num_1 - num_2
product= num_1 * num_2
quotient= num_1 / num_2
remainder= num_1 % num_2

print("{}+{}= {}".format(num_1, num_2, sum_1))
print("{} -{}= {}".format(num_1,num_2,difference))
print("{} * {}= {}".format(num_1, num_2, product))
print("{} /{}= {}".format(num_1, num_2, quotient))
print("{} % {}= {}".format(num_1, num_2, remainder))

