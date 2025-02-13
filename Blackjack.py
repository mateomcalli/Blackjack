# My updated (better) version of our class Blackjack project

import random
new_game = True
error = False
games = 0
wins = 0
ties = 0
losses = 0
val = 0
dealer_val = 0
dealer_cards = []
cards = []

def logic(v): # will process rng, turn it into cards with names and values
    if v == 1:
        return 'ACE', 1 # first value will be unpacked as "card", the other as "new_val"
    elif v == 11:
        return 'JACK', 10
    elif v == 12:
        return 'QUEEN', 10
    elif v == 13:
        return 'KING', 10
    else:
        return str(v), v

def initial_draw(first, second):



while True:
    if not error:
        if new_game:
            val = 0
            dealer_val = 0
            cards = []
            dealer_cards = []
            games += 1
            print(f'START GAME #{games}')
        num1 = random.randint(1, 13)
        num2 = random.randint(1, 13)
        card, new_val = logic(num1)
        cards.append(card)
        val += new_val
        print(f'\nYour card is a {card}!')
        print(f'Your hand is: {val}\n')
        dealer = random.randint(1,13)
        dealer_card, dealer_new_val = logic(dealer)
        dealer_cards.append(dealer_card)
        dealer_val += dealer_new_val
        print(f'\nThe dealer has drawn a {dealer_card}.')
        if val == 21:
            new_game = True
            print('BLACKJACK! You win!\n')
            wins += 1
            continue
        elif val > 21:
            new_game = True
            print('You exceeded 21! You lose.\n')
            losses += 1
            continue
    error = False
    print('1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n')
    option = input('Choose an option: ')

    if option == '1': # if user wants another card run the loop back
        new_game = False
        continue

    elif option == '2': # dealer logic
        dealer = random.randint(1,13)
        print(f"\nDealer's hand: {dealer}\nYour hand is: {val}\n")
        if dealer <= 21 and dealer > val:
            new_game = True
            print('Dealer wins!\n')
            losses += 1
            continue
        elif dealer <= 21 and val > dealer:
            new_game = True
            print('You win!\n')
            wins += 1
            continue
        elif dealer > 21:
            new_game = True
            print('You win!\n')
            wins += 1
            continue
        elif dealer == val:
            new_game = True
            print("It's a tie! No one wins!\n")
            ties += 1
            continue
    elif option == '3': # prints stats
        error = True
        games -= 1
        print(f'\nNumber of Player wins: {wins}\nNumber of Dealer wins: {losses}\nNumber of tie games: {ties}\nTotal # of games played is: {games}\nPercentage of Player wins: {(wins/games) * 100:.1f}%\n')
    elif option == '4':
        break
    else: # invalid input case
        error = True
        print('Invalid input!\n\nPlease enter an integer value between 1 and 4.')
        continue