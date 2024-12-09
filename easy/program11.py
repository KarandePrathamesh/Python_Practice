# Write a Python function that accepts a list and returns its reverse. 

class Reverse_List:
    def __init__(self,input_list):
        self.input_list = input_list
    
    def reverse_list(self): 
        return self.input_list[::-1]
    
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5] 
    obj = Reverse_List(my_list)
    reversed_list = obj.reverse_list() 
    print("Original list:", my_list) 
    print("Reversed list:", reversed_list)