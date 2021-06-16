import random
from collections import Counter
import math
from functools import reduce
from functools import partial
import string
import re
import urllib
#import requests

value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
suits = ['spades', 'clubs', 'hearts', 'diamonds']


def generate_deck(value, suits):
    ''' This function takes suits and value list, combines them and returns the deck
    # Input :
        suits: list
        value: list
    # Functionality:
        Iterates over suits and value and combines each value.

    # Returns:
        A list is returned containing the result of combination of value and suits.
    '''
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    deck = [i+j for i in suits for j in value]
    return deck

generate_deck(value, suits)

# Function generate deck of 52 cards Solely using map, lambda and zip function
def generate_deck_using_lambda_map_zip(value, suits):
    # using lambda zip and map fubction
    value = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    suits = ['spades', 'clubs', 'hearts', 'diamonds']
    x = list(map(lambda cards: ''.join(cards), zip(suits*len(value), value*len(suits))))
    return x

test_list = generate_deck_using_lambda_map_zip(value, suits)
print(test_list)

# From a pre-stored fibonacci list, a given number has to be checked if it's a fibonacci number

fib_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
fib_check = lambda x: True if x in fib_list else False

# From 2 lists, even number from 1st list and odd number from 2nd list should be added...using list comprehension, lambda/filter can also be used
def even_odd(l1, l2):
    if len(l1) == 0:
        raise ValueError('list1 cannot be empty')
    if len(l2) == 0:
        raise ValueError('list2 cannot be empty')
    else:
        return [x + y for x, y in zip(l1, l2) if x % 2 == 0 and y % 2 != 0]

# Vowels should be stripped from a given string using list comprehension
def strip_vowel_str(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if len(str) <= 1:
        raise ValueError("string should have more than one character")

    else:
        return "".join([x for x in str if x not in vowels])

# RelU function should be defined using list comprehension

def relu_activation(l):
    if len(l) == 0:
        raise ValueError("atleast one value must be entered in the list")
    for i in l:
        if type(i) not in (int, float):
            raise TypeError("only ints or floats are allowed")
        else:
            pass
    else:
        return[0 if x < 0 else x for x in l]

# sigmoid function should be defined using list comprehension
def sigmoid_activation(l):
    if len(l) == 0:
        raise ValueError("atleast one value must be entered in the list")
    for i in l:
        if type(i) not in (int, float):
            raise TypeError("only ints or floats are allowed")
        else:
            pass
    else:
        return[round(1/(1+math.exp(-x)), 2) for x in l]

# function to shift the characters by 5 places
def shift_5_char(str):
    if len(str) <= 1:
        raise ValueError("string should have more than one character")
    else:
        str = str.lower()
        return "".join([chr(ord(x)+5) if (ord(x)+5) <= 122 else chr(ord(x)+5-122+96) for x in str])


# checks whether a string matches any of the swear words mentioned in https://github.com/RobertJGabriel/Google-profanity-words/blob/master/list.txt
# response = requests.get("https://raw.githubusercontent.com/RobertJGabriel/Google-profanity-words/master/list.txt")
# data = response.text
# data
# def profane_filter(str):
#     if len(str) <= 1:
#         raise ValueError("string should have more than one character")
#     else:
#         return True if str.lower() in data else False

# Using reduce , lambda etc the even numbers in a list must be added.
def add_even_num(l):
    if len(l) == 0:
        raise ValueError("atleast one value must be entered in the list")
    for i in l:
        if type(i) != int:
            raise TypeError("only ints are allowed")
        else:
            pass
    sum = reduce(lambda a, b: a + b, filter(lambda a: (a % 2 == 0), l))
    return sum

# Using reduce, lambda etc the biggest ascii character in a given string must be found
def big_char_str(str):
    if len(str) <= 1:
        raise ValueError("string should have more than one character")
    else:
        result = reduce(lambda a, b: a if ord(a) > ord(b) else b, str)
        return result

# Using reduce, lambda function every third number must be added in a list
def add_third_num(l):
    if len(l) == 0:
        raise ValueError("atleast one value must be entered in the list")
    for i in l:
        if type(i) != int:
            raise TypeError("only ints are allowed")
        else:
            pass
    else:
        add_third_number = reduce(lambda a, b: a + b, l[2::3])
        return add_third_number

# Using randint, random.choice and list comprehensions, 15 random KADDAADDDD number plates must be generated, where KA is fixed, D stands for a digit, and A stands for Capital alphabets
def num_plate(x='KA', *y):
    Alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return [x + str(random.randint(10,99)) + str(random.choice(Alphabet)) + str(random.choice(Alphabet)) + str(random.randint(1000, 9999)) for i in range(15)]

# Using the above, we write a partial function such that 1000/9999 are hardcoded, but KA can be provided

new_plate = partial(num_plate)
new_plate("DL")
