class Number:
    def __init__(self ,start) -> None:
        self.data = start
    
    def __sub__(self, other):
        return Number(self.data - other)
    
# x = Number(5)
# y = x - 2
# print(y.data)

class Indexer():
    data = [i for i in range(10)]

    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

x = Indexer()



for i in range(5):
    print(x[i])