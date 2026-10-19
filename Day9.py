# Day-8 (Learning Python)

# Tuplee

# Exampel of Tuple
grocery_items = ('onion','Apple','Juice', 'rice')

# Tuples are the similars to the lists, but while lists are a mutable data type , tuples are immutable. 
# Point to be noted: We cannot change the elements in a tuple 

# For example : If you try to upadte any item you will get a TypeError

grocery_items = ('onion','Apple','Juice', 'rice')
grocery_items[0] = 'Noodles' # TypeError


# 1) Accesing Tuple Elements

grocery_items = ('Potato','Apple','Juice', 'rice')
print(grocery_items[1])


# 2) Checking if a element is in tuple

grocery_items = ('Potato','Apple','Juice', 'rice')
'Potato' in grocery_items


# 3) Use of Slicing - Note ( Same as List)

grocery_items = ('Potato','Apple','Juice', 'rice')
print(grocery_items[1:3])


# 4) Removing elements from the tuple. You will see type error because Tuples are immutable 

grocery_items = ('Potato','Apple','Juice', 'rice')
del grocery_items[1]  # TypeErrorrr


# 5) Using count() Method

grocery_items = ('Potato','Apple','Juice', 'rice')
print(grocery_items.count('Potato'))


# 6) Index() Method

grocery_items = ('Potato','Apple','Juice', 'rice')
print(grocery_items.index('Apple'))


# 7) Using Sorted - In order to arrange this is assending order

even_numbers = (2,10,8,64,6,54,60)
print(sorted(even_numbers))


# In next lesson we will be learning about how the loop works 
# Congratulations on you another bounty Sampadaa












