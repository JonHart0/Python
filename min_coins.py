### Calculates the number of coins to return to customer, returns array, and prints string

# This function should take values between 1 : 99 cents


# Changing the number of coins in the registar may change which coins are returned
num_coins_reg = [99, 0, 99, 99] #How many of the coins are in the registar
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



#More efficient code than last attempt
def min_coins_short(Value):

    coin_change = [0, 0, 0, 0] #Array of coins that will return to customer
    coin_check = [0, 0, 0, 0] #Array of coins compared to registar coins to ensure enough coin avaliable

    #Loop through each coin type, each time reducing the remaining change
    for i, coin in enumerate(coin_check):
        coin_check[i] = Value // coin_val[i] #How many "Whole" coins fit into value
        if num_coins_reg[i] >= coin_check[i]: #If there are enough coins in registar
            Value -= coin_check[i] * coin_val[i] #Reduce value by "Whole" coins used
            coin_change[i] = coin_check[i] #Update returned change array

    if Value > 0: #If there was not enough change in registar to meet needs
        print("Insufficiant change")

    print(f"{coin_change[0]} Quarters, {coin_change[1]} Dimes, {coin_change[2]} Nickels, {coin_change[3]} Pennies")
    return coin_change


# min_coins(33) --> [1, 0, 1, 3]
#Enter value between 0:99
min_coins_short(33)

min_coins(33)
