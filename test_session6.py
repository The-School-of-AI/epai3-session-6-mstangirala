import pytest
import random
from collections import Counter
import string
import session6
import os
import inspect
import re
import math
from functools import reduce
from functools import partial

README_CONTENT_CHECK_FOR = [
    fib_check,
    even_odd,
    strip_vowel_str,
    relu_activation,
    sigmoid_activation
]

def test_session6_readme_exists():
    """ A. failure_message: Found README.md file
        B. Once you write this test, it needs to print the filures_message for failing this test.
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_session6_readme_500_words():
    """ A. failures_message: Make your README.md file interesting! Add atleast 300 words
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"


def test_session6_readme_proper_description():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_session6_readme_file_for_more_than_10_hashes():
    """ A. failures_message: You have not described all the functions/classes well in your README.md file
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10


def test_session6_indentations():
    """ Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
        A.  failures_message_1: Your script contains misplaced indentations
            failures_message_2: Your code indentation does not follow PEP8 guidelines
        B. Once you write this test, it needs to print the failures_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    lines = inspect.getsource(session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session6_function_name_had_cap_letter():
    """ A. failures_message: You have used Capital letter(s) in your function names
        B. Once you write this test, that checks formatting by checking # being used more than 10 times, \
        it needs to print the failure_message
        C. Delete lines A, B and C, write proper function description after writing this test successfully. 
    """
    functions = inspect.getmembers(session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_generate_deck_using_Normal_func():
    assert session6.generate_deck(suits,value) == ['spades2', 'spades3', 'spades4', 'spades5', 'spades6', 'spades7', 'spades8', 'spades9', 'spades10', 'spadesjack', 'spadesqueen', 'spadesking', 'spadesace',
 'clubs2', 'clubs3', 'clubs4', 'clubs5', 'clubs6', 'clubs7', 'clubs8', 'clubs9', 'clubs10', 'clubsjack', 'clubsqueen', 'clubsking', 'clubsace',
 'hearts2', 'hearts3', 'hearts4', 'hearts5', 'hearts6', 'hearts7', 'hearts8', 'hearts9', 'hearts10', 'heartsjack', 'heartsqueen', 'heartsking', 'heartsace',
 'diamonds2', 'diamonds3', 'diamonds4', 'diamonds5', 'diamonds6', 'diamonds7', 'diamonds8', 'diamonds9', 'diamonds10', 'diamondsjack', 'diamondsqueen', 'diamondsking', 'diamondsace'], 'functionality not working as expected'


def test_generate_deck_lambda_map_zip():
    assert session6.generate_deck_using_lambda_map_zip(suits,value) == ['2spades', '3clubs', '4hearts', '5diamonds', '6spades',
     '7clubs', '8hearts', '9diamonds', '10spades', 'jackclubs', 'queenhearts', 'kingdiamonds', 'acespades', '2clubs', '3hearts', '4diamonds', '5spades', '6clubs', '7hearts', '8diamonds', '9spades', '10clubs', 'jackhearts', 'queendiamonds', 'kingspades', 'aceclubs', '2hearts', '3diamonds', '4spades', '5clubs', '6hearts', '7diamonds', '8spades', '9clubs', '10hearts', 'jackdiamonds', 'queenspades', 'kingclubs', 'acehearts', '2diamonds', '3spades', '4clubs', '5hearts', '6diamonds', '7spades',
     '8clubs', '9hearts', '10diamonds', 'jackspades', 'queenclubs', 'kinghearts', 'acediamonds'], 'functionality not working as expected'


def test_even_odd():
    assert session6.even_odd([2,4,6,9,10,22,33], [12,4,7,16,15,25,26]) == [13, 25, 47], "functionality not working as expected"

def test_strip_vowel_str():
    assert session6.strip_vowel_str('python') == 'pythn', "functionality not working as expected"

def test_relu_activation():
    assert session6.relu_activation([-3, -2, -1, 0, 1, 2, 3.5]) == [0, 0, 0, 0, 1, 2, 3.5], "functionality not working as expected"

def test_sigmoid_activation():
    assert sesssion6.sigmoid_activation([-3, -2, -1, 0, 1, 2, 3.5]) == [0.05, 0.12, 0.27, 0.5, 0.73, 0.88, 0.97], "functionality not working as expected"

def test_shift_5_char():
    assert session6.shift_5_char('abcde') == 'fghij', "functionality not working as expected"


def test_add_even_num():
    assert session6.add_even_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 30, "functionality not working as expected"

def test_big_char_str():
    assert session6.big_char_str('Welcome') == 'o', "functionality not working as expected"

def test_add_third_num():
    assert session6.add_third_num([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 18, "functionality not working as expected"

def test_num_plate():
    assert session6.num_plate() != ['KA29QD1029', 'KA22IU3699', 'KA88VT3796', 'KA77VK7525', 'KA26NC7952', 'KA62IB6018', 'KA84IH9472', 'KA69UT6490',
                                 'KA98PP3681', 'KA42QI1845', 'KA27ID7921', 'KA46JT4251', 'KA96BW1429', 'KA47HT8486', 'KA50BN1069'], "functionality not working as expected"

