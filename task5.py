class Numbers:
    multiplier = 10
    def __init__(self , x , y):
        self.x = x
        self.y = y
    
    def addNum(self):
        return self.x + self.y
    
    def multiply(self , a):
        self.a = a
        return self.a * self.multiplier

    def subs(self , b , c):
        self.b = b
        self.c = c
        return self.b - self.c

number1 = Numbers( 20 , 30)
print(number1.addNum())
print(number1.multiply(10))
print(number1.subs(10 , 29))