import random

money = 100

#Write your game of chance functions here

# Helper methods
# - - - - - - - -

def validBet(bet):
    if bet <= 0:
        print("Bet must be a positive amount!")
        return False
    if bet > money:
        print("Insufficient funds! Max bet is " + str(money))
        return False
    return True

def rand(a, b):
    return random.randint(a, b)

def coin():
    return rand(0, 1)

def dice():
    return rand(1, 6)

def card_to_string(num):
    switcher = {
        11: "Jack",
        12: "Queen",
        13: "King",
        14: "Ace"
    }
    return switcher.get(num, str(num))

def invalid_roulette():
    print("Please call either Odd, Even, 0, 00 or a number from 1 to 36.")
    
def roulette_to_string(result):
    if (result == 0):
        print("Landed on 0")
    elif (result == 37):
        print("Landed on 00")
    else:
        print("Landed on " + str(result))
        
def win_message():
    print("You win!")
    
def lose_message():
    print("You lose.")
        

# Games
# - - -

def flip_coin(bet, call):
    print(" - - - - - -")
    # Bet is invalid
    if (not validBet(bet)):
        return 0
    
    print("Starting game: Coin Toss")
    print("Starting bank: " + str(money))
    print("Bet: " + str(bet))
    print("You called: " + str(call))
    
    heads = "heads"
    tails = "tails"
    call_lower = call.lower()
    
    heads_found = True if call_lower.find(heads) != -1 else False
    tails_found = True if call_lower.find(tails) != -1 else False
    
    # Call invalid
    if not (heads_found ^ tails_found):
        print("Call heads or tails!")
        return 0
    
    # Flip
    win = True if (coin() == 1) else False
    print("Flipping coin...")
    if win:
        call_sanitised = "heads" if heads_found else "tails"
        print("Coin is a " + call_sanitised + ", you win!")
        return bet
    else:
        opposite = "heads" if tails_found else "tails"
        print("Coin is a " + opposite + ". Sorry, you lost.")
        loss = 0 - bet
        return loss

        

def cho_han(bet, call):
    print(" - - - - - -")
    # Bet is invalid
    if (not validBet(bet)):
        return 0
    
    print("Starting game: Cho-Han")
    print("Starting bank: " + str(money))
    print("Bet: " + str(bet))
    print("You called: " + str(call))
    
    odd = "odd"
    even = "even"
    call_lower = call.lower()
    
    odd_found = True if (odd in call_lower) else False
    even_found = True if (even in call_lower) else False
    
    # Call invalid
    if not (odd_found ^ even_found) or (odd_found and even_found):
        print("Call odd or even!")
        return 0
    
    # Roll
    dice1 = dice()
    dice2 = dice()
    total = dice1 + dice2
    throw_is_even = True if (total%2 == 0) else False
    call_is_even = False if (call_lower.find(even) == -1) else True
    
    if throw_is_even:
        parity_string = " (even)"
    else:
        parity_string = " (odd)"
        
    print("Dice 1: " + str(dice1))
    print("Dice 2: " + str(dice2))
    print("Total: " + str(total) + parity_string)
    
    if (throw_is_even ^ call_is_even):
        print("Sorry, you lose.")
        loss = 0 - bet
        return loss
    else:
        print("You win!")
        return bet;

    
    
def card_game(bet):
    print(" - - - - - -")
    # Bet is invalid
    if (not validBet(bet)):
        return 0
    
    print("Starting game: Cards")
    print("Starting bank: " + str(money))
    print("Bet: " + str(bet))
    
    card1 = rand(2, 14)
    suite1 = rand(0, 3)
    card2 = card1
    suite2 = suite1
    
    while (card1 is card2) and (suite1 is suite2):
        card2 = rand(2, 14)
        suite2 = rand(0, 3)

    card1_as_string = card_to_string(card1)
    
    if (card1 is card2):
        print("Both have " + card1_as_string + ", it's a tie!")
        return 0
    
    card2_as_string = card_to_string(card2)
    print("You picked: " + card1_as_string)
    print("Dealer picks: " + card2_as_string)
    
    if (card1 > card2):
        print("You win!")
        return bet
    else:
        print("You lost.")
        loss = 0 - bet
        return loss
        
        
        
def roulette(bet, call):
    print(" - - - - - -")
    # 0: 0
    # 00: 37
    # 1-36: 1-36
    
    # Bet is invalid
    if (not validBet(bet)):
        return 0
    
    print("Starting game: Roulette")
    print("Starting bank: " + str(money))
    print("Bet: " + str(bet))
    print("You called: " + str(call))
    
    odd = "odd"
    even = "even"
    zero = "0"
    double_zero = "00"
    call_lower = call.lower()
    
    odd_found = True if (odd in call_lower) else False
    even_found = True if (even in call_lower) else False
    zero_found = True if (zero == call_lower) else False
    double_zero_found = True if (double_zero == call_lower) else False
    
    parse_success_count = 0
    if (odd_found):
        parse_success_count += 1
    if (even_found):
        parse_success_count += 1
    if (zero_found):
        parse_success_count += 1
    if (double_zero_found):
        parse_success_count += 1
        
    if parse_success_count > 1:
        invalid_roulette()
        return 0
    
    # Spin the roulette wheel
    spin = rand(0, 37)
    if parse_success_count == 0:
        # Call is either invalid or a 1-36 num
        try:
            call_num = int(call)
            if (call_num < 1) or (call_num > 36):
                # Edge cases:
                # Zero should not make it here legitimately,
                # Negative numbers not allowed,
                # Highest number in roulette is 36
                invalid_roulette()
                return 0
            else:
                # Valid number parsed from user input
                roulette_to_string(spin)
                if (call_num == spin):
                    # Win
                    win = bet * 35
                    win_message()
                    return win
                else:
                    # Loss
                    loss = 0 - bet
                    lose_message()
                    return loss

        except:
            invalid_roulette()
            return 0
    else:
        # Either called Odd, Even, Zero or 00
        roulette_to_string(spin)
        if (double_zero_found):
            if (spin == 37):
                # Win
                win = bet * 35
                win_message()
                return win
            else:
                # Loss
                loss = 0 - bet
                lose_message()
                return loss
        elif (zero_found):
            if (spin == 0):
                # Win
                win = bet * 35
                win_message()
                return win
            else:
                # Loss
                loss = 0 - bet
                lose_message()
                return loss
        elif (even_found):
            if (spin%2 == 0 and spin != 0):
                # Win
                win = bet
                win_message()
                return win
            else:
                # Loss
                loss = 0 - bet
                lose_message()
                return loss
        elif (odd_found):
            if (spin%2 != 0):
                # Win
                win = bet
                win_message()
                return win
            else:
                # Loss
                loss = 0 - bet
                lose_message()
                return loss
    # All unforseen edge cases
    invalid_roulette()
    return 0

                
    
    
    

#Call your game of chance functions here

# Coin Toss / flip_coin
money += flip_coin(5, "heads")
print("Bank: " + str(money))

money += flip_coin(5, "tails")
print("Bank: " + str(money))

money += flip_coin(5, "heads tails")
print("Bank: " + str(money))

money += flip_coin(5, "heads 2346")
print("Bank: " + str(money))

money += flip_coin(10, "either")
print("Bank: " + str(money))

money += flip_coin(9999, "heads")
print("Bank: " + str(money))
print()

# Cho-Han / cho_han
money += cho_han(5, "odd")
print("Bank: " + str(money))

money += cho_han(5, "eVeN 123")
print("Bank: " + str(money))

money += cho_han(5, "odd even")
print("Bank: " + str(money))

money += cho_han(5, "both")
print("Bank: " + str(money))

money += cho_han(9999, "both")
print("Bank: " + str(money))
print()


# Card Game / card_game
money += card_game(1)
print("Bank: " + str(money))

money += card_game(3)
print("Bank: " + str(money))

money += card_game(9999)
print("Bank: " + str(money))
print()


# Roulette / roulette
money += roulette(5, "odd")
print("Bank: " + str(money))

money += roulette(5, "oDd 123")
print("Bank: " + str(money))

money += roulette(5, "even")
print("Bank: " + str(money))

money += roulette(5, "both eVeN")
print("Bank: " + str(money))

money += roulette(5, "odd even")
print("Bank: " + str(money))

money += roulette(5, "either")
print("Bank: " + str(money))

money += roulette(1, "0")
print("Bank: " + str(money))

money += roulette(1, "00")
print("Bank: " + str(money))

money += roulette(1, "1")
print("Bank: " + str(money))

money += roulette(1, "36")
print("Bank: " + str(money))

money += roulette(1, "15")
print("Bank: " + str(money))

money += roulette(1, "-1")
print("Bank: " + str(money))

money += roulette(1, "37")
print("Bank: " + str(money))

money += roulette(1, "")
print("Bank: " + str(money))

money += roulette(9999, "10")
print("Bank: " + str(money))
