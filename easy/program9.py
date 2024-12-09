# Create a program to count the number of characters in a string provided by the user.

class CharacterCounter: 
    def __init__(self, input_string): 
        self.input_string = input_string 
    
    def count_characters(self): 
        return len(self.input_string) 
    
# Taking User Input
myStr = input("Enter a string to count its characters: ") 

# Driver Code
obj = CharacterCounter(myStr)
count = obj.count_characters()
print(f"The number of characters in the string is: {count}")