# Define a simple class in Python and create an object of that class.

class Self_Intro:
    def __init__(self,name,age,address): 
        self.name = name
        self.age = age
        self.address = address


# Taking User Input
name = input('\nEnter your name    :')
age = input('Enter your age      :')
address = input('Enter your address :')

if __name__ == '__main__':
    obj = Self_Intro(name,age,address)
    print(obj.name)
    print(obj.age)
    print(obj.address)