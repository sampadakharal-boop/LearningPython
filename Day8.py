#Day-8 of learning Python 

# Welcomeee back to my seriesss hehheee
# We are continuing with Some Common Methods Used for Lists

# 1) Adding Elements with append()

festivals = ['Dashain', 'Tihar', 'Holi']
festivals.append('Teej')
print(festivals)


# 2) Adding Multiple Elements with extend()

festivals = ['Dashain', 'Tihar', 'Holi']
more_festivals = ['Teej','Loshar','Jamastami']
festivals.extend(more_festivals)
print(festivals)



# 3) Inserting Elements at a Specific Index

festivals = ['Dashain', 'Tihar', 'Holi']
festivals.insert(2,'Janmastami')
print(festivals)


# 4) Removing Elements from a List

festivals = ['Dashain', 'Tihar', 'Holi', 'Janmastami']
festivals.remove('Holi')
print(festivals)


# 5) In order to remove specific index in the list, you can use the pop()

festivals = ['Dashain', 'Tihar', 'Holi', 'Janmastami']
festivals.pop(2)
print(festivals)


# 6) Clearing the list - If you need to empty the list they use clear()

festivals = ['Dashain', 'Tihar', 'Holi', 'Janmastami']
festivals.clear()
print(festivals)


# 7) Sorting a list - It is used to sort the elements in place. Like arranging numbers in asending order

numbers = [20, 5, 6, 8, 10, 19, 90]
numbers.sort()

print(numbers)


# 8) If you want both the orginal List and the sorted list then you have another one that is sorted().You can use it like 


numbers = [20, 5, 6, 8, 10, 19, 90]
sorted_numbers = sorted(numbers)

print(numbers)
print(sorted_numbers)


# 9 ) Reversing a List 

festivals = ['Dashain', 'Tihar', 'Holi', 'Janmastami']
festivals.reverse()
print(festivals)


# 10) Finding the Index of an Element

festivals = ['Dashain', 'Tihar', 'Holi', 'Janmastami']
print(festivals.index('Tihar'))


# Ohh wowww sammpuu Youu did ittt 
# Again the bounty is yoursss 


# Next lesson we will learn more about Tupleee 










