fruits = ["banana", "apple", "mango"]
veges = ["potato", "brinjal", "onion"]

# using Extend method
fruits.extend(veges)
print(fruits)

# using append
for x in veges:
    fruits.append(x)

print(fruits)

# using + operator
mylist = fruits + veges
print(mylist)
