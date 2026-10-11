#Day1 of Learning Python
#From Day 1 - Day 5 ( Revising all the things I known)

# Write a program to add two numbers without taking input from the user 

# a = 1
# b = 2
# c = a + b  
# print(c)


# Write a praogarm to add two number by taking input from the user 

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:"))
# c = a + b
# print(c)



# Print first and last name in reverse order with a space between them 

# first_name = (input("Enter the first name:"))
# last_name = (input("Enter the last name:"))
# print(last_name + " " + first_name)



# Write a python program to find the sum and product of two number

# a = int(input("Enter the first number:"))
# b = int(input("Enter the second number:4"))
# c = a + b
# d = a * b
# print("The addition of first number and second number is",c)
# print("The nultipication of first number and second number is",d)



# Write a python program to print the area of circle. Take radius of circle as an input from the user ( Area of circle = 2pir)

# r = int(input("Enter the radius of circle:"))
# a = 22/7 * r * r
# print(a)



# The user enters either 'A', 'B', 'C'. If 'A' is enteres, the program should display the word 'Apple', if 'B' is entered, it should display 'Banana' and when 'C' is entered it should sisplay 'Coconut'

# word = input("Enter the alphabet A , B or C: ")
# if word == 'A' or word == 'a':
#   print("Apple")
# elif word == 'B' or word == 'b':
#   print("Banana")
# elif word == 'C' or word == 'c':
#   print("Coconut")
# else:
#   print("Invalid Input. Please enter alphabet A, B or C")



# Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye"

# num = int(input("Enter the number:"))
# if (num % 5 == 0):
#     print("Hello")
# else:
#     print("Bye:")



# Write program to check wheather a person is eligible for citizenship or not (citizrnship age >= 18)

# age = int(input("Enter you age:"))
# if(age>=18):
#     print("You are eligible for citizenship")
# elif(age<=18):
#     print("You are not eligible for citizenship")
# else:
#     print("Please enter valid number")



#Write a program to check wheather a person is senoir citizenship or not, ask user for their age

# age = int(input("Enter your age"))
# if (age>=60):
#     print("You are a senoir citizenship")
# elif (age<=60):
#    print("You are not a senoir citizenship ")
# else:
#     print("Please enter valid number")



# Prompt the user to enter any number of positive and negatice integer values, then display the number of each type that were entered, sum the positive number Use break and continue concept

# positive_count = 0
# negative_count = 0
# positive_sum = 0

# while True:
#     number = int(input("Enter an integer (0 to Stop):"))

#     if number == 0:
#         break

#     if number < 0:
#         negative_count +=1
#         continue

#     positive_count += 1
#     positive_sum += number

# print("Number of positive values:",positive_count)
# print("Number of negative vlaues:",negative_count)
# print("Sum of positive values:",positive_sum)


