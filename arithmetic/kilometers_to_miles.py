#Convert Kilometers to Miles
kilometer =  float(input("Enter the distance in kilometers: "))

# Conversion factor: 1 kilometer = 0.621371 miles
factor = 0.621371
miles = kilometer * factor

print(f"{kilometer} kilometers is equivalent to {miles} miles")