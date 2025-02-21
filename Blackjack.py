# My updated (better) version of our class Blackjack project
# (Supposedly) fixed issues: Multiple aces logic
# TODO: Add logic for splitting, fix spacing on rarer scenarios (aces, blackjack?).

import random
import time
import sys

game = True
new_game = True
play_game = False
double = False
error = False
not21 = True
first_choice = True
split_option = False
bank = 1000
option = ''
games = 0
wins = 0
ties = 0
losses = 0
bet = 0
val, dealer_val, dealer_soft_val, soft_val = 0, 0, 0, 0
dealer_cards = []
cards = []

def gen_suit():
    suits = ['♣', '♦', '♥', '♠']
    suit = random.choice(suits)
    return suit

def logic(v): # will process rng, turn it into cards with names and values
    if v == 1: # if card is an ace
        return 'A', 1, 11 # first value will be unpacked as "card", the other as "new_val", and the third "soft_val"
    elif v == 11:
        return 'J', 10, 10
    elif v == 12:
        return 'Q', 10, 10
    elif v == 13:
        return 'K', 10, 10
    else:
        return str(v), v, v

while game:
    if bank <= 0:
        print(f'\nYou are out of money. Better luck next time!')
        break
    if not error:
        if new_game:
            while not play_game:
                if games > 0:
                    again = input('\nPlay again? [y/n]: ')
                    print()
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
            double = False
            first_choice = True
            betting = True
            cards = []
            dealer_cards = []
            games += 1
            while betting:
                print(f'Your bankroll is: {bank}')
                try:
                    bet = int(input(f'Place your bet: '))
                    if bet > bank:
                        print(f"\nInvalid input. You don't have enough money!\n")
                        continue
                    if bet <= 0:
                        print('\nInvalid input. Bets must be greater than zero.\n')
                        continue
                    if type(bet) == float:
                        print('\nInvalid input. Bets must be whole numbers.\n')
                    betting = False
                except ValueError:
                    print('\nInvalid input. Bets must be whole numbers.\n')
                    continue
            print(f'\nSTART GAME #{games}')
            time.sleep(1)

            num = random.randint(1, 13)
            dealer_card1, dealer_val1, dealer_soft_val = logic(num)
            dealer_cards.append(dealer_card1)
            dealer_val += dealer_val1
            print(f'\nThe dealer has drawn the: ', end='')
            time.sleep(0.8)
            print(f'{dealer_card1}{gen_suit()}')
            time.sleep(1)
            # End of initial dealer logic

            num1 = 1
            num2 = 1
            card1, card_val1, soft_val1 = logic(num1)
            card2, card_val2, soft_val2 = logic(num2)
            cards.append(card1)
            cards.append(card2)
            val += card_val1 + card_val2
            soft_val = soft_val1 + soft_val2

            print(f'\nYou have drawn: ', end='')
            time.sleep(0.8)
            print(f'{card1}{gen_suit()} ', end='')
            time.sleep(0.8)
            print(f'{card2}{gen_suit()}')
            time.sleep(1)

            if soft_val == 21:
                val = soft_val

            if 'A' not in cards:
                print(f'Your hand is: {val}')
            elif 'A' in cards and soft_val < 21:
                print(f'Your hand is: {val} / {soft_val}')
            else: print(f'Your hand is: {val}')
            time.sleep(1)

            # If player draws blackjack
            if soft_val == 21 and dealer_soft_val != 11:
                print('\nBLACKJACK! You win!')
                wins += 1
                new_game = True
                bank += (bet * 1.5)
                continue
            elif soft_val == 21 and dealer_soft_val == 11:
                not21 = False
                option = '2'
            # End of new game player logic

        if not new_game:
            num = random.randint(1, 13)
            card, card_val, card_soft_val = logic(num)
            cards.append(card)
            val += card_val
            soft_val += card_soft_val
            print(f'The dealer shows you the: ', end='')
            time.sleep(1)
            print(f'{card}{gen_suit()}')
            time.sleep(1)

            while soft_val > 21 and 'A' in cards:
                soft_val -= 10

            if soft_val == 21:
                val = soft_val

            if 'A' in cards and (val < soft_val < 21):
                print(f"You're now at: {val} / {soft_val}")
            else:
                print(f"You're now at {val}.")
            time.sleep(1)

            if val > 21:
                print('You have exceeded 21. You lose.')
                losses += 1
                bank -= bet
                new_game = True
                continue

            if val == 21:
                not21 = False
                option = '2'

            if double:
                option = '2'

    if not21 and not double:
        if not error:
            if first_choice:
                print('\nYour move:')
                print('1. Hit\n2. Stand\n3. Double\n4. Print statistics\n5. Exit\n')
            else:
                print('\nYour move:')
                print('1. Hit\n2. Stand\n3. Print statistics\n4. Exit\n')
        error = False
        option = input('Choose an option: ')
        print()

    if option == '1': # if user wants another card run the loop back
        new_game = False
        first_choice = False
        continue

    elif option == '3' and first_choice: # doubles
        if bet <= (bank * 0.5):
            bet *= 2
        else:
            error = True
            print("Insufficient balance to double.")
            continue
        double = True
        new_game = False
        first_choice = False
        continue

    elif option == '2': # stand logic
        val = soft_val if soft_val <= 21 else val
        while dealer_val < 17:
            num = random.randint(1, 13)
            dealer_card, dealer_card_val, dealer_card_soft_val = logic(num)
            dealer_cards.append(dealer_card)
            dealer_val += dealer_card_val
            dealer_soft_val += dealer_card_soft_val
            time.sleep(0.3)
            if not not21: # lol
                print()
                not21 = True
            if 17 <= dealer_soft_val <= 21:
                dealer_val = dealer_soft_val
            if 'A' in dealer_cards and dealer_soft_val < 17:
                print(f"The dealer has drawn the: {dealer_card}{gen_suit()}. They're now at: {dealer_val} / {dealer_soft_val}")
            else: print(f"The dealer has drawn the: {dealer_card}{gen_suit()}. They're now at: {dealer_val}")
            time.sleep(1)

        if val < dealer_val <= 21:
            new_game = True
            print('\nDealer wins!')
            losses += 1
            bank -= bet
            continue
        elif dealer_val <= 21 and val > dealer_val:
            new_game = True
            print("\nDealer couldn't get there. You win!")
            wins += 1
            bank += bet
            continue
        elif dealer_val > 21:
            new_game = True
            print("\nThat's too many. You win!")
            wins += 1
            bank += bet
            continue
        elif dealer_val == val:
            new_game = True
            print("It's a push! No one wins.")
            ties += 1
            continue

    # elif option == '4' and split_option: # splits
    #     pass

    elif (option == '3' and not first_choice and not split_option) or (option == '4' and double) or (option == '5' and split_option): # prints stats
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

    elif (option == '4' and not double and not split_option) or (option == '5' and not split_option) or (option == '6' and split_option): # exits
        print('Thank you for playing.')
        break

    else: # invalid input case
        error = True
        if len(cards) < 2:
            first_choice = True
        print('Invalid input! Please enter an integer value between 1 and 4.\n')
        continue
