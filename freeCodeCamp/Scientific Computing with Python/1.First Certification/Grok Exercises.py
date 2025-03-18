# Grok Exercises

# 1. Palindrome Checker
# Task: Write a function that takes a string and returns True if it’s a palindrome 
# (reads the same forward and backward, ignoring spaces and case), False otherwise.
# ETA 30 min - Took 28 min

def palindrome_check(text):
    clean_text = text.lower().replace(' ', '')
    list_text = []
    invert_text = []
    for char in clean_text:
        list_text.append(char)
        invert_text.insert(0, list_text[-1])
    if invert_text == list_text:
        return print(True)
    else:
        return print(False)

print('\n1. Palindrome Checker')
print('-'*100)
palindrome_check("A man a plan a canal Panama")
print('='*100)

# 2. Number Guessing Game
# Task: Create a game where the computer picks a random number between 1 and 100, and the user guesses it. 
# Provide hints (“too high” or “too low”) until they get it. Use random.randint().
# ETA 45 min - Took 13 min

import random as rd

num = rd.randint(1, 1)
guessed = False
count = 0

print('\n2. Number Guessing Game')
print('-'*100)

while guessed == False:
    guess = int(input("Guess:"))
    if guess == num:
        print('You got it!')
        break
    elif guess < num:
        count += 1
        print('Too low')
    elif guess > num:
        count += 1
        print('Too high')
    if count % 5 == 0:
        giveup = input('Give up (y/n)? ')
        if giveup.lower() == 'y':
            print('Loser')
            break

print('='*100)

# 3. Simple Calculator
# Task: Create a function that takes two numbers and an operator (+, -, *, /) and returns the result. Handle division by zero.
# ETA 20 min - Took 38 min

# Remove spaces
def no_spaces(my_list):
    no_spaces = []
    for item in my_list:
        cleaned = item.replace(' ','')
        no_spaces.append(cleaned)
    return no_spaces

# Split problems into numbers and operators
def extract(my_list):
    part1 = []  # First numbers
    part2 = []  # Operators
    part3 = []  # Second numbers
    formated = []   # Formated list
    cleaned = no_spaces(my_list) # List with no spaces

    for item in cleaned:
        if '**' in item:
            formated = item.replace('**', ' ** ')
        elif '^' in item:
            formated = item.replace('^', ' ^ ')
        else:
            formated = item.replace('+', ' + ').replace('-', ' - ').replace('*', ' * ').replace('/', ' / ')
        
        parts = formated.split()
        if len(parts) != 3:  # Check if input has 3 parts
            return None
        part1.append(parts[0])
        part2.append(parts[1])
        part3.append(parts[2])
    return (part1, part2, part3)

def calculator(operation):
    
    indeterminate = 'indeterminate'

    operation = no_spaces(operation)
    result = extract(operation)
    if result is None:  # Invalid input
        return "Error: Invalid operation format"

    num1, operator, num2 = result
    try:
        x = float(num1[0])
        y = float(num2[0])
    except ValueError:
        return "Error: Numbers must be valid"

    if operator[0] == '+':
        answer = x + y
    elif operator[0] == '-':
        answer = x - y
    elif operator[0] == '*':
        answer = x * y
    elif operator[0] == '/':
        if y == 0:
            return indeterminate
        else:
            answer = x / y
    elif operator[0] == '**' or operator[0] == '^':
        answer = x ** y
    return answer

operation = []
exit = False

print('\n3. Simple Calculator')
print('-'*100)

while exit == False:
    operation = [str(input('Input: '))]  # Reset list with new input
    if operation[0].lower() in ('exit', 'end'):  # Check exit first
        break
    result = calculator(operation)
    print(result)

print('='*100)