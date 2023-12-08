# Swap values
a = input("Enter the first value: ")
b = input("Enter the second value: ")

print(f"Original Values: a = {a}, b = {b}")

#temp value holder
temp = a 
a = b
b = temp

print(f"New Values : a = {a}, b = {b}")