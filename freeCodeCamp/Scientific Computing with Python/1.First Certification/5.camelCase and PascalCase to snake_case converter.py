# camelCase/PascalCase to snake_case converter
# In this project, you are going to build a program that takes a camelCase or PascalCase formatted 
# string as input and converts that to a snake_case formatted string using two approaches. First, 
# you'll use a for loop and then list comprehension to achieve the same results. You'll see how list comprehension can make your code more concise.

# In Python, a list comprehension is a construct that allows you to generate 
# a new list by applying an expression to each item in an existing iterable
# and optionally filtering items with a condition. Apart from being briefer, 
# list comprehensions often run faster.

text = input('Text: ')

def convert_to_snake_case(pascal_or_camel_cased_string):
   # snake_cased_char_list = []
    # for char in pascal_or_camel_cased_string:
    #     if char.isupper():
    #         converted_character = '_' + char.lower()
    #         snake_cased_char_list.append(converted_character)
    #     else:
    #         snake_cased_char_list.append(char)
    # snake_cased_string = ''.join(snake_cased_char_list)
    # clean_snake_cased_string = snake_cased_string.strip('_')

    # return clean_snake_cased_string
    snake_cased_char_list = [                                             # A basic list comprehension consists of an expression followed by a for clause   
        '_' + char.lower() if char.isupper()                              # List comprehensions accept conditional statements, to evaluate the provided expression only if certain conditions are met 
        else char                                                         # if clause must be put after the for keyword.
        for char in pascal_or_camel_cased_string                          # Differently from the if clause, the if/else construct must be placed between the expression and the for keyword.
    ]
    return ''.join(snake_cased_char_list).strip('_')

def main():
    print(f'Converted text: {convert_to_snake_case(text)}')

main()
