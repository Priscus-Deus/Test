class Test:
    def __init__(self, value) -> None:
        self.data = value

    
    def __repr__(self) -> str:
        return "Наша строка для разработчика"
    

    def __str__(self) -> str:
        return "Наша строка для пользователя"
    


x = Test(40)
print(x)