money = input("enter how much u want to invest:")
interest_rate = input("interest_rate")
money = float(money)
interest_rate = float(interest_rate)*0.01
for i in range(10):
    money = money + (money * interest_rate)

print("investment after 10 years = ${:.2f}".format(money))
