class Student:
    interest = 0.05
    def __init__(self,first,last,budget):
        self.first = first
        self.last = last
        self.budget = budget
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def money(self):
        return (self.budget * self.interest) + self.budget

student1 = Student("Mongkol","EK",1500)
print(  student1.money())