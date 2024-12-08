# Create a program that converts a given Celsius temperature to Fahrenheit. 
# Explanation: Use the formula F = (C * 9/5) + 32, where C is Celsius, and F is Fahrenheit.
class Temperature_Converter:
    def __init__(self,celsius):
        self.celsius = celsius
    
    def celsius_to_fahrenheit(self):
        return (self.celsius * 9/5)+32

# driver code
obj = Temperature_Converter(37)
print(f'\nTemperature in celsius : {obj.celsius} and in fahrenheit : {obj.celsius_to_fahrenheit()}\n')
