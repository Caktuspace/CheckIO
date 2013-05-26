#Help Sofia make a decrypter for the passwords that Nikola will encrypt through the cipher map. A cipher grille is a 4 × 4 square of paper with four windows cut out. Placing the grille on a paper sheet of the same size, the encoder writes down the first four symbols of his password inside the windows (see fig. below). After that, the encoder turns the grille 90 degrees clockwise. The symbols written earlier become hidden under the grille and clean paper appears inside the windows. The encoder then writes down the next four symbols of the password in the windows and turns the grille 90 degrees again. Then, they write down the following four symbols and turns the grille once more. Lastly, they write down the final four symbols of the password. Without the same cipher grille, it is difficult to discern the password from the resulting square comprised of 16 symbols. Thus, the encoder can be confident that no hooligan will easily gain access to the locked door.
#Write a module that enables the robots to easily recall their passwords through codes when they return home.
#Input: Two lists. The first list with four lines contain the Robot's cipher grille. The next list with four lines contain the square with the ciphered password. All the symbols in the square are lowercase Latin letters.
#Output: Password
#Example:
#checkio([[
#'X...',
#'..X.',
#'X..X',
#'....'],[
#'itdf',
#'gdce',
#'aton',
#'qrdi']
#]) == 'icantforgetiddqd'
#
#checkio([[
#'....',
#'X..X',
#'.X..',
#'...X'],[
#'xhwc',
#'rsqx',
#'xqzz',
#'fyzr']
#]) == 'rxqrwsfzxqxzhczy'

FIRST_CIPHER = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
SECOND_CIPHER = [12,8,4,0,13,9,5,1,14,10,6,2,15,11,7,3]
THIRD_CIPHER = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0]
LAST_CIPHER = [3,7,11,15,2,6,10,14,1,5,9,13,0,4,8,12]
 
 
def checkio(data):
    grille, template = data
    un, deux, trois, quatre = grille
    cipher = [un[0], un[1], un[2], un[3], deux[0], deux[1], deux[2], deux[3], trois[0], trois[1], trois[2], trois[3], quatre[0], quatre[1], quatre[2], quatre[3]]
     
    un, deux, trois, quatre = template
    phrase = [un[0], un[1], un[2], un[3], deux[0], deux[1], deux[2], deux[3], trois[0], trois[1], trois[2], trois[3], quatre[0], quatre[1], quatre[2], quatre[3]]
    res = ''
    j = 0
    for i in FIRST_CIPHER:
        if cipher[i] == 'X':
            res += phrase[j]
        j += 1
    j = 0
    for i in SECOND_CIPHER:
        if cipher[i] == 'X':
            res += phrase[j]
        j += 1
    j = 0
    for i in THIRD_CIPHER:
        if cipher[i] == 'X':
            res += phrase[j]
        j += 1
    j = 0
    for i in LAST_CIPHER:
        if cipher[i] == 'X':
            res += phrase[j]
        j += 1
 
    return res
 
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([
        ['X...',
         '..X.',
         'X..X',
         '....'],
        ['itdf',
         'gdce',
         'aton',
         'qrdi']]) == 'icantforgetiddqd', 'First example'
 
    assert checkio([
        ['....',
         'X..X',
         '.X..',
         '...X'],
        ['xhwc',
         'rsqx',
         'xqzz',
         'fyzr']]) == 'rxqrwsfzxqxzhczy', 'Second example'