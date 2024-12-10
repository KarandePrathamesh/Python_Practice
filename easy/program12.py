# Use a for loop to print the first 10 Fibonacci numbers.
n = 10
a, b = 0, 1
result = [] 
for i in range(n): 
    result.append(a) 
    a, b = b, a + b 
print(result)