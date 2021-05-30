class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def __add__(self,others):
        p=self.m1+others.m1
        q=self.m2+others.m2
        return(p+q)
    def __truediv__(self, others):
        p=self.m1+others.m1
        q=self.m2+others.m2
        return(p/q)
s=student(12,2)
s1=student(14,6)
print(s/s1)''''''
