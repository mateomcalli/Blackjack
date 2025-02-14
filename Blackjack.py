# My updated (better) version of our class Blackjack project
# TODO: Add logic for splitting and doubling, spacing is currently good and game is playable.

import random
import time
import sys

game = True
new_game = True
play_game = False
error = False
not21 = True
option = ''
games = 0
wins = 0
ties = 0
losses = 0
val = 0
dealer_val = 0
dealer_cards = []
cards = []

def gen_suit():
    suits = ['♣', '♦', '♥', '♠']
    suit = random.choice(suits)
    return suit

def logic(v): # will process rng, turn it into cards with names and values
    if v == 1:
        return 'A', 1 # first value will be unpacked as "card", the other as "new_val"
    elif v == 11:
        return 'J', 10
    elif v == 12:
        return 'Q', 10
    elif v == 13:
        return 'K', 10
    else:
        return str(v), v

while game:
    if not error:
        if new_game:
            while not play_game:
                if games > 0:
                    again = input('\nPlay again? [y/n]: ')
                    if again == 'y':
                        break
                    elif again == 'n':
                        print('Thank you for playing!')
                        sys.exit()
                    else:
                        print('Invalid input. Please try again.')
                        play_game = False
                        continue
                else: break

            val = 0
            dealer_val = 0
            cards = []
            dealer_cards = []
            games += 1
            print(f'\nSTART GAME #{games}')
            time.sleep(1)

            dealer = random.randint(1, 13)
            dealer_card1, dealer_val1 = logic(dealer)
            dealer_cards.append(dealer_card1)
            dealer_val += dealer_val1
            print(f'\nThe dealer has drawn the: ', end='')
            time.sleep(0.8)
            print(f'{dealer_card1}{gen_suit()}')
            time.sleep(1)
            # End of initial dealer logic

            num1 = random.randint(1, 13)
            num2 = random.randint(1, 13)
            card1, card_val1 = logic(num1)
            card2, card_val2 = logic(num2)
            cards.append(card1)
            cards.append(card2)
            val += (card_val1 + card_val2)
            print(f'\nYou have drawn: ', end='')
            time.sleep(0.8)
            print(f'{card1}{gen_suit()} ', end='')
            time.sleep(0.8)
            print(f'{card2}{gen_suit()}')
            time.sleep(1)
            print(f'Your hand is: {val}')
            time.sleep(1)
            # End of new game player logic

            if val == 21:
                print('BLACKJACK! You win!\n')
                wins += 1
                new_game = True
                continue

        if not new_game:
            num = random.randint(1, 13)
            card, card_val = logic(num)
            cards.append(card)
            val += card_val
            print(f'The dealer shows you the: ', end='')
            time.sleep(1)
            print(f'{card}{gen_suit()}')
            time.sleep(1)
            print(f"You're now at {val}.")
            time.sleep(1)

            if val > 21:
                print('You have exceeded 21. You lose.')
                losses += 1
                new_game = True
                continue

            if val == 21:
                not21 = False
                option = '2'

    if not21:
        if not error:
            print('\nYour move:')
            print('1. Hit\n2. Stand\n3. Print statistics\n4. Exit\n')
        error = False
        option = input('Choose an option: ')
        print()

    if option == '1': # if user wants another card run the loop back
        new_game = False
        continue

    elif option == '2': # dealer logic
        while dealer_val < 17:
            num = random.randint(1,13)
            dealer_card, dealer_card_val = logic(num)
            dealer_cards.append(dealer_card)
            dealer_val += dealer_card_val
            time.sleep(0.3)
            if not not21: # lol
                print()
                not21 = True
            print(f"The dealer has drawn the: {dealer_card}{gen_suit()}. They're now at {dealer_val}.")
            time.sleep(1)

        if dealer_val <= 21 and dealer_val > val:
            new_game = True
            print('\nDealer wins!')
            losses += 1
            continue
        elif dealer_val <= 21 and val > dealer_val:
            new_game = True
            print("\nDealer couldn't get there. You win!")
            wins += 1
            continue
        elif dealer_val > 21:
            new_game = True
            print("\nThat's too many. You win!")
            wins += 1
            continue
        elif dealer_val == val:
            new_game = True
            print("It's a push! No one wins.")
            ties += 1
            continue

    elif option == '3': # prints stats
        if games > 1:
            error = True
            games -= 1
            print(f'Total # of games played: {games}')
            print(f'Number of Player wins: {wins}')
            print(f'Number of Dealer wins: {losses}')
            print(f'Number of pushes: {ties}')
            print(f'Percentage of Player wins: {(wins / games) * 100: .1f}%\n')
        else:
            error = True
            print("Invalid input! There aren't any games to display statistics.\n")
            continue

    elif option == '4':
        break

    else: # invalid input case
        error = True
        print('Invalid input! Please enter an integer value between 1 and 4.\n')
        continue
        break
