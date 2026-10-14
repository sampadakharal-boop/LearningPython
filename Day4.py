#Day-4 of learning Python
# Let's gather all the energy to learn new things


# 1) Some Common String Methods 

# Making a Lower case to upper case

string = 'Hureyyy I Did it'

uppercase = string.upper()
print(uppercase)



# 2) Making a word Upper to Lower

string = 'Hureyyy I Did it'

uppercase = string.lower()
print(uppercase)



# 3) Lets Use strip
# strip(): Removes leading and trailing characters or whitespace from a string.
# Even if there is no whitespace, strip() works without causing an error. It simply returns the same string.

string = ' hello world '
remove_space = string.strip()
print(remove_space)


# 4) Lets Use replace (old, new)

myfile = 'welcome backk to my blog'
replace_my_message = myfile.replace('welcome backk to my blog', 'Go back guys I am not shootting')
print(replace_my_message)



# 5) split(seprator) 
# -> It Splits a string into a list using a separator. If none is given, it splits at whitespace.

# when the seperator is not specified

string = 'hello world'
changed_one = string.split()
print(changed_one)

# 6) joins()

string = ['Mr','Popular']
unpopular = ' '.join(string)
print(unpopular)


# 7) startswith(prefix) - It return a boolen indicating if a string strat with the sprecified prefix

string = 'Soo Tired'
startswith_what = string.startswith('So')
print(startswith_what) 

# 8) capitalize(): Returns a new string with the first character capitalized and the other characters lowercased.

string = 'feeling sleepy'
startswith_what = string.capitalize()
print(startswith_what) 


# 9) endswith(suffix) - It return a boolen indicating if a string ends with the sprecified prefix

string = 'Soo Tiredd'
startswith_what = string.endswith('Tiredd')
print(startswith_what)  


# 10) count(substring) - Counts how many times a substring appears in a string.

string = 'hello world'

countit = string.count('o')
print(countit)



# Hureyyyyy Samm You completed the Taskkkk
# You are awarded with a Bountyyyy . 
# Be back with more curiosity and eagerness to learn 



















