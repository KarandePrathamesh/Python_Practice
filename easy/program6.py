# Write a program that checks if a number is even or odd using an if statement. 
class Check_Even_Odd: 
    def __init__(self, number): 
        self.number = number 
    
    def even_odd_check(self): 
        if self.number % 2 == 0: 
            return f"{self.number} is Even" 
        else: 
            return f"{self.number} is Odd" 

# Taking User Input
number = int(input("Enter a number to check even or odd: ")) 

# Driver Code
obj = Check_Even_Odd(number)
print(f'{obj.even_odd_check()}')