'''class student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no
        print(name,roll_no)
s1=student('avi',5)
s2=student('ranga',6)
s3=student('moni',8)'''

'''class car:
    wheel=4
    def __init__(self,brand,milage):
        self.brand=brand
        self.milage=milage
        print( brand,milage,car.wheel)
car.wheel=8
c1=car('alto',12)
c2=car('bmw',89)
c3=car('sss',9)'''


class Car:
    name = 'Python garage'
    wheel = 4  # class variable/ global variable

    def __init__(self, brand, milage):
        self.brand = brand  # instance variable
        self.milage = milage  # instance variable
        print(brand, milage, Car.wheel)

    def gear(self, shift):  # instance method
        print(shift)
        print(self.brand, self.milage, Car.wheel)

    @staticmethod
    def info():  # local method
        a = 114  # local variable
        print(a)

    @classmethod
    def about(cls):  # class method
        print(cls.name)
        print(cls.wheel)


c1 = Car('audi', 14)
c2 = Car('BMW', 10)
c3 = Car('ALTO', 24)
print('*' * 10)
c1.gear('auto')
print('*' * 10)
# Car.wheel = 5
c2.gear('manual')
print('+' * 15)
Car.info()

Car.about()



