# Arithmetic Formatter Project
# Finish the arithmetic_arranger function that receives a list of strings which are 
# arithmetic problems, and returns the problems arranged vertically and side-by-side. The
# function should optionally take a second argument. When the second argument is set to
# True, the answers should be displayed.

# Verify the operators
def find_str(my_list, target):
    for item in my_list:
        if target in item:
            return True
    return False 

# Verify for letter or special characters
def is_num(my_list):
    for item in my_list:
        cleaned = item.replace(' ','').replace('+', '').replace('-','')
        if not cleaned.isdigit():
            return False
    return True

# Extract the numbers and operations
def extract(my_list):
    part1 = []
    part2 = []
    part3 = []    
    for item in my_list:
        parts = item.split()
        part1.append(parts[0])
        part2.append(parts[1])
        part3.append(parts[2])
    return (part1, part2, part3)

def arithmetic_arranger(problems, show_answers=False):
     
    conditions = 4

    # Limit strings input
    if len(problems) > 5:
        conditions -= 1
        error1 = 'Error: Too many problems.'
        return error1
    
    num1, operator, num2 = extract(problems)

    # Verify the operators
    if find_str(problems, '*') or find_str(problems, '/'):
        conditions -= 1
        error2 = "Error: Operator must be '+' or '-'."
        return error2

    # Verify for letter or special characters
    if is_num(problems) == False:
        conditions -= 1
        error3 = 'Error: Numbers must only contain digits.'
        return error3

    # Verify width of each operation
    for i in range(len(problems)):
        if len(num1[i]) > 4 or len(num2[i]) > 4:
            conditions -= 1
            error4 = 'Error: Numbers cannot be more than four digits.'
            return error4

    if conditions == 4:
        top = ''
        mid = ''
        bot = ''

        for i in range(len(problems)):
            num_width = max(len(num1[i]), len(num2[i])) + 2
            top += num1[i].rjust(num_width) + ' ' * 4

        for i in range(len(problems)):
            num_width = max(len(num1[i]), len(num2[i]))
            mid += operator[i] + ' ' + num2[i].rjust(num_width) + ' ' * 4
        
        for i in range(len(problems)):
            num_width = max(len(num1[i]), len(num2[i])) + 2
            bot += '-'.rjust(num_width, '-') + ' ' * 4

        if show_answers == True:
            num_width = max(len(num1[i]), len(num2[i])) + 2
            answers_list = []
            answers = ''
            answer = 0
            for i in range(len(problems)):
                x = int(num1[i])
                y = int(num2[i])
                if operator[i] == '+':
                    answer = x + y
                    answers_list.append(answer)
                elif operator[i] == '-':
                    answer = x - y
                    answers_list.append(answer)
                answers += str(answers_list[i]).rjust(num_width) + ' ' * 4
            lines = [top, mid, bot, answers]
            return '\n'.join(lines).rstrip(' ') + '\n'
        else:
            lines = [top, mid, bot]
            return '\n'.join(lines).rstrip(' ') + '\n'

print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)}')