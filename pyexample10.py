import random
rand_num = random.randrange(1, 51)
print("random generated no is:", rand_num)
i = 1
while i != rand_num:
    print("inner :", i)
    i += 1
print("the last value of i =", i)
