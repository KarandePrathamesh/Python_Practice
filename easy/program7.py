# Create a Python function to find the maximum of three numbers. 

class Max:
    def __init__(self,n1,n2,n3):
        self.a = n1
        self.b = n2
        self.c = n3
        
    def find_maximum(self): 
        return max(self.a,self.b,self.c) 

# Taking User Input
num1 = float(input("Enter the first number : ")) 
num2 = float(input("Enter the second number : ")) 
num3 = float(input("Enter the third number : ")) 

# Driver Code
obj = Max(num1, num2, num3)
print(f"The maximum number is : {obj.find_maximum()}")