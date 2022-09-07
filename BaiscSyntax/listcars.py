"""
Built in methods to help manipulating a list
"""

cars= ["bmw", "honda", "audi"]

length = len(cars)
print(cars)
print(length)

cars.append("benz")
print(cars)

cars.insert(4, "jaguar")
print(cars)

x= cars.index("audi")
print(x)

y=cars.pop()
print(y)
print(cars)

cars.remove("bmw")
print(cars)

slicing = cars [0:2]
print(slicing)


