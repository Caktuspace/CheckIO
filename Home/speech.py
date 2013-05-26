#Stephen's speech module is broken. This module is responsible for his number pronunciation. He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time. Help the robot to speak properly and faster by writing his speech module. All the words in the string must be separated by exactly one space character.
#Input: Integer number from 0 to 999.
#Output: A string representation of this number.
#Example:
#checkio(4)=='four'
#checkio(143)=='one hundred forty three'
#checkio(12)=='twelve'
#checkio(101)=='one hundred one'
#checkio(212)=='two hundred twelve'
#checkio(40)=='forty'

FIRST_TEN = ["zero", "one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"

import math
 
def checkio(number):
    if number < 10:
        return FIRST_TEN[number]
    string = ''
    if number >= 100:
        if number % 100 > 0:
            string += FIRST_TEN[math.floor(number / 100)] + " " + HUNDRED + " "
        else:
            string += FIRST_TEN[math.floor(number / 100)] + " " + HUNDRED
         
    if number % 100 >= 20:
        if number % 10 > 0:
            string += OTHER_TENS[math.floor((number % 100) / 10) - 2] + " "
        else:
            string += OTHER_TENS[math.floor((number % 100) / 10) - 2]
    elif number % 100 >= 10:
        string += SECOND_TEN[number % 10]
         
    if number % 10 > 0 and (number % 100 > 19 or number % 100 < 10):
        string += FIRST_TEN[number % 10]
		
    return string
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"