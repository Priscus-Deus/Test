
class Person:
    
    def __init__(self, name, job=None, pay=0) -> None:
        self.name = name
        self.job = job
        self.pay = pay

    def giveRaise(self, percent):
        self.pay = int(self.pay * ( 1 + (percent / 100)))

    def __repr__(self) -> str:
        return f'Person: {self.name}, Job: {self.job}, Pay: {self.pay}'
    

class Manager(Person):

    def __init__(self, name, pay) -> None:
        Person.__init__(self,name, 'Manager', pay)

    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)





if __name__ == '__main__':
    bob = Person('bob')
    kirill = Person('Kirill', 'dev', 20)

    print(bob)
    print(kirill)

# person2.pay *= 1.1
    kirill.giveRaise(25)
    print(kirill)
    print("____________________________")
    tom = Manager('Tom Shelby', 50)
    tom.giveRaise(10)
    print(tom.pay)
    print(tom)