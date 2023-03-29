# Creating a list
fruits = ['apple', 'banana', 'cherry', 'orange']

# Accessing elements by index
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Appending an element to the list
fruits.append('grape')
print("Fruits after appending:", fruits)

# Extending a list with another list
more_fruits = ['mango', 'kiwi']
fruits.extend(more_fruits)
print("Fruits after extending:", fruits)

# Slicing a list
first_three_fruits = fruits[:3]
print("First three fruits:", first_three_fruits)

# Searching for an element in the list
search_fruit = 'cherry'
if search_fruit in fruits:
    print(f"{search_fruit} is in the list.")
else:
    print(f"{search_fruit} is not in the list.")

# Sorting the list
fruits.sort()
print("Sorted fruits:", fruits)

# Reverse sorting the list
fruits.sort(reverse=True)
print("Reverse sorted fruits:", fruits)

# Using list comprehension to create a new list
short_fruits = [fruit for fruit in fruits if len(fruit) <= 5]
print("Short-named fruits:", short_fruits)
