# Write a Python program that reads a text file and prints its content line by line.

class Read_File:
    def __init__(self,input_filePath):
        self.filePath = input_filePath
        
    def read_file(self):
        with open(self.filePath, 'r') as file:
            for l in file: 
                print(l.strip()) 

# Taking User Input
input_filePath = input('\nEnter a file path :')

# Drive Code
obj = Read_File(input_filePath)
obj.read_file()
