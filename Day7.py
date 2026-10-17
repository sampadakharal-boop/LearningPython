# Day-7 of learning 

# Loops and Sequences 


cities = [' Los Angeles', 'London', 'Tokyo']
print(cities [0])
print(cities [-1])


# Using list() Constructor - It is a used to convert an iterable into a list like this :

developer = 'Nepali'
print(list(developer)) 


# How to get the length of a list 

numbers = [1,2,3,4,5]
print(len(numbers))


# Updating list Elements

subjects = ['Computer', 'Maths', 'English', 'Science']
subjects[2] = 'Account'
print(subjects)


# Removing Elements from a list 

subjects = ['Computer', 'Maths', 'English', 'Science']
del subjects[3]
print(subjects)


# Checking If an Elements Is in a list 

continent = ['Asia','Africa','North America','South America','Antartica','Europe', 'Australia']
print('Antartica' in continent)
print('Nepal' in continent)


# Working with Nested List 

writer = ['BhanuBhakta Aachrya', 1814 , ['Ghasi','Ramayana','Kantipur Nagari']  ]
print(writer[1])
print(writer[2][0])
print(writer[0])


# Unpacking Values From a List

employee_info = ['Bob', 25, 'Software Engineer ']
name, age, job = employee_info

print(name)
print(age)
print(job)


# If you want to collect any other remaining elements from a list, you can use asterisk (*)

employee_info = ['Bob', 25, 'Software Engineer ']
name, *rest = employee_info

print(name)
print(*rest)


# Slicing Lists 

foods = ['Momo', 'Pasta', 'Keema Noodles', 'Laphing']
print(foods[1:4])


# If you want to extract a list of just even numbers, you can use the slicing operataor like below 

numbers = [1,2,3,4,5,6]
print(numbers[1::2])


# What a wonderful Dayyyyyy 
# One more bounty added to my treasure..Wohoooo !







