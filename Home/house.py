#Help Nikola develop a password security check module for Sofia. The password will be considered strong enough if its length is greater than or equal 10 symbols, it has at least one number, one uppercase letter and one lowercase letter in it.
#Input data: A string that is a password.
#Output data: The output will be true if the password is safe.
#Example:
#checkio('A1213pokl')==False
#checkio('bAse730onE')==True
#checkio('asasasasasasasaas')==False
#checkio('QWERTYqwerty')==False
#checkio('123456123456')==False
#checkio('QwErTy911poqqqq')==True

import re
 
def checkio(data):
    if re.search(r'[a-z]', data) != None:
        if re.search(r'[A-Z]', data) != None:
            if re.search(r'[0-9]', data) != None:
                if data.__len__() > 9:
                    return True
    return False
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"