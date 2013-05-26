#Write a program that will (depending on Sofia and the old man’s initial bargaining sums--the steps by which they will increase or decrease the price during their negotiations) calculate which final price they will agree upon. If Sofia's offer is lower than or equal to the old man's offer, she will accept the old man's price and vice versa.
#Sofi makes her offer first. She never offers an amount higher than what is offered to her. On the other hand, the old man never offers an amount lower than what is offered to him.
#Input data: Contains four integer numbers: Sofia's initial offer, Sofia's raise to her offer, the initial counteroffer from the old man, and the old man's reduction in his offer;
#Output data: The amount of money that Sofia will pay for the spaceship.
#Example:
#checkio([150, 50, 1000, 100]) == 450
#Sofi: 200
#Oldman: 900
#Sofi: 250
#Oldman: 800
#Sofi: 300
#Oldman: 700
#Sofi: 350
#Oldman: 600
#Sofi: 400
#Oldman: 500
#Sofi: 450
#... old man will be ok with it, because his next proposition will be lower than 450.
# a bit shorter example
#checkio([500, 300, 700, 100]) == 700
#Sofi will be ok with 700 because her next proposition will be higher

def checkio(data):
    sofiTurn = True
 
    initial_sofi, raise_sofi, initial_oldman, reduction_oldman = data
     
    while True:
        if sofiTurn:
            if initial_sofi + raise_sofi > initial_oldman:
                return initial_oldman
            else:
                initial_sofi += raise_sofi
        else:
            if initial_oldman - reduction_oldman < initial_sofi:
                return initial_sofi
            else:
                initial_oldman -= reduction_oldman
        sofiTurn = not sofiTurn

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([150, 50, 1000, 100]) == 450, "1st example"
    assert checkio([150, 50, 900, 100]) == 400, "2nd example"