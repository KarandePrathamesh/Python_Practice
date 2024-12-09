# Write a Python script to declare and access values in a list.
class List_Operations:
    def __init__(self,input_list):
        self.list_name = input_list

    def create_list(self):
        # self.list_name = []
        self.list_name = list()
    
    def insert_list_elements(self,elements):
        self.list_name.append(elements)
    
    def print_list(self):
        for i in self.list_name:
            print(i)

# Taking User input
input_list = str(input("\nEnter a name for list :"))

# Driver Calling 
obj = List_Operations(input_list)
obj.create_list()
obj.insert_list_elements(45)
obj.insert_list_elements(92.2)
obj.insert_list_elements("Prathamesh")
obj.insert_list_elements('a')
obj.print_list()
    