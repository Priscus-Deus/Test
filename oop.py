from calendar import firstweekday


class FirstClass:
    def setdata(self, value):
        self.data = value
    
    def display(self):
        print(self.data)


x = FirstClass()
y = FirstClass()

x.setdata('kirill')
y.setdata(3.1415926)


x.display()
y.display()

x.data = 'new data'
x.display()

class SecondClass(FirstClass):
    def display(self):
        print(f'Current value = {self.data}')


z = SecondClass()
z.setdata(42)
z.display()



class ThirdClass(SecondClass):

    def __init__(self, value) -> None:
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)
    
    def __str__(self) -> str:
        return f"ThirdClass: {self.data}"
    
    def mul(self, other):
        self.data *= other
print("___________________________")
a = ThirdClass('kirill')
a.display()
print(a)
b = a + " kyznetsov"
b.display()
print(b)
a.mul(3)
print(a)