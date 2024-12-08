# Write a python program to demonstrate the use of basic arithmetic operators ( +, -, *, /).
class Arithmetic_Operator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    
    def addition(self):
        return self.a + self.b
    
    def subtraction(self):
        return self.a - self.b
    
    def multiplication(self):
        return self.a * self.b
    
    def division(self):
        return self.a / self.b
    

# Taking  User Input in float
n1  = float(input('Enter first number  :'))
n2  = float(input('Enter second number :'))

# Driver Code OR calling objects
obj = Arithmetic_Operator(n1,n2)
print(f'\nAddition is       :{obj.addition()}')
print(f'Subtraction is    :{obj.subtraction()}')
print(f'multiplication is :{obj.multiplication()}')
print(f'Division is       :{obj.division()}')


