# Use list comprehension to create a list of squares for numbers 1 to 10.

class List_Comprehension:
    def __init__(self,range1,range2):
        self.range1 = range1
        self.range2 = range2
        
    def list_of_squares(self):
        squares = [x**2 for x in range(self.range1, self.range2+1)]
        return squares
    
# Taking User Input
print('\nEnter a range to get list :')
r1 = int(input('start from :'))
r2 = int(input('to :'))

# Driver Code
obj = List_Comprehension(r1,r2)
print(f'\nList of square is : {obj.list_of_squares()}')