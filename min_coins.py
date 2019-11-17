### Calculates the number of coins to return to customer, returns array, and prints string

# This function should take values between 1 : 99 cents


# Changing the number of coins in the registar may change which coins are returned
num_coins_reg = [99, 99, 99, 99] #How many of the coins are in the registar
coin_val = [25, 10, 5, 1] #Quarters, Dimes, Nickels, Pennies

def min_coins(Value):

    coin_change = [0, 0, 0, 0]

    #How many Quarters are returned (if enough are in registar)
    num_Quart_check  = Value // coin_val[0] #How many quarters go whole into Value
    if num_coins_reg[0] >= num_Quart_check : #If there are enough Quarters in the registar
        coin_change[0] = num_Quart_check #Set the number of quarters returned to the maximum avaliable quarters
        Value -= coin_change[0] * coin_val[0] #Reduce the remaining value by the calculated amount already returned

    #Dimes
    num_Dime_check   = Value // coin_val[1]
    if num_Dime_check <= num_coins_reg[1] :
        coin_change[1] = num_Dime_check
        Value -= coin_change[1] * coin_val[1]

    #Nickels
    num_Nickel_check   = Value // coin_val[2]
    if num_coins_reg[2] >= num_Nickel_check :
        coin_change[2] = num_Nickel_check
        Value -= coin_change[2] * coin_val[2]

    #Pennies
    num_Penny_check   = Value // coin_val[3]
    if num_coins_reg[3] >= num_Penny_check :
        coin_change[3] = num_Penny_check
        Value -= coin_change[3] * coin_val[3]

    if Value > 0:
        print("Insufficiant change")

    print(f"{coin_change[0]} Quarters, {coin_change[1]} Dimes, {coin_change[2]} Nickels, {coin_change[3]} Pennies")
    return coin_change


# min_coins(33) --> [1, 0, 1, 3]
#Enter value between 0:99
min_coins(5)
