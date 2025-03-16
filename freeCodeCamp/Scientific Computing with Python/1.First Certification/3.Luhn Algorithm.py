# In this project, you will implement the Luhn Algorithm. This algorithm is a formula to validate a variety of identification numbers.
# The Luhn algorithm is as follows:
#    1.From the right to left, double the value of every second digit; if the product is greater than 9, sum the digits of the products.
#    2.Take the sum of all the digits.
#    3.If the sum of all the digits is a multiple of 10, then the number is valid; else it is not valid.

def verify_card_number(card_number):
    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]                             # string[start:stop:step]
    odd_digits = card_number_reversed[::2]                              # empyt parameters = default values // [0:(end)]

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)                                 # must operate values from the same type

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]                            
    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:                                                # if the product number is > 9 then sum both digits
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    #print(total)
    return total % 10 == 0                                              # verifies is the total sum is a multiple of 10 

def main(card_number):
    card_translation = str.maketrans({'-':'', ' ' : ''})                # str.maketrans({ A : B, C : D}) replace all A and C characters in a string for B and D
    translated_card_number = card_number.translate(card_translation)    # The translate method must be called on the string to be translated with the translation table as an argument

    if verify_card_number(translated_card_number):                      # if True
        print('Your card number is VALID!')
    else:
        print('Your card number is INVALID!')

try:
    card_number = str(input('Insert your card number in the following format: '))
    main(card_number)
except ValueError:
    print('Invalid format, please try again.')
    card_number = str(input('Insert your card number in the following format: '))
    main(card_number)