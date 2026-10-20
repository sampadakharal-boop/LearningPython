# Day 11 of learning Python


#LOOP 


# Loop are used to repeat a block of code

# Using for Loop - Use a for loop when you want to go through a sequence, such as a list, string, or range of numbers.

programming_languages = ['Rust', 'Java', 'Python', 'C++']

for language in programming_languages:
 print(language)


# Nesting for Loop - When you need a loop inside another loop
categories = ['Fruit','Vegetable']
foods = ['Apple','Mango','Banana']


for category in categories:
  for food in foods:
    print(category,  food)


# Using while loop - When you repeat until a condition changes

secret_number = 3
guess = 0

while guess != secret_number:
    guess = int(input('Guess the number (1-5): '))
    if guess != secret_number:
        print('Wrong! Try again.')



# Loop with break - It helps to stop the loop immediately 

for i in range(10):
    if i == 5:
        break
    print(i)



# Loop with continue - Skips the current iteration and moves to the next one.

for i in range(5):
    if i == 2:
        continue
    print(i)


# Loop with else - Python allows an else block after a loop. It runs when the loop finishes normally, without being stopped by break.

for i in range(3):
    print(i)
else:
    print("Loop completed!")


#  Loop through a list using enumerate() - Useful when you need both the index and the value.

fruits = ["Apple", "Mango", "Banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)


# You have complete todays taskkk
# Goodnightt