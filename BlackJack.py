'''
Black Jack Card Game Between Player and Dealer
'''
from random import shuffle



class Deck:
    def __init__(self, ranks, suits):
        self.ranks = ranks
        self.suits = suits
        self.card_list = []
        self.card = []

    def create_deck(self):
        for self.rank in ranks:
            for self.suit in suits:
                self.card = self.rank, self.suit
                self.card_list.append(self.card)

        return self.card_list

    def shuffle_deck(self):
        shuffle(self.card_list)
        shuffled_deck = self.card_list

        return shuffled_deck


class Person:
    def __init__(self, player, cash):
        self.player = player
        self.cash = cash

    def lose_your_bet(self, bet_amount):
        self.cash = self.cash - bet_amount

    def win_your_bet(self, bet_amount):
        self.cash = self.cash + bet_amount

    def __str__(self):
        return f'{self.player}!'


def determine_sum_of_cards_in_the_hand(hand):
    sum = 0

    for i in range(len(hand)):
        sum = sum + values[hand[i][0]]

    if sum > 21:
        for i in range(len(hand)):
            if hand[i][0] == 'A':
                sum = sum - 10

    return sum


def evaluate_the_sum(sum):
    sum_is_OK = False

    if sum == 21:
        sum_is_OK = True

    elif sum < 21:
        sum_is_OK = True

    elif sum > 21:
        sum_is_OK = False

    return sum_is_OK


def determine_win_or_lose(player_cards_sum, dealer_sum_cards):
    player_win = False

    if player_cards_sum == 21:
        player_win = True
        print('\nPLAYER JACK POT. PLAYER WINS THE BET.')

    elif dealer_sum_cards != 0 and player_cards_sum > dealer_sum_cards and player_cards_sum < 21:
        player_win = True
        print('\nPlayer wins the bet.')

    elif player_cards_sum > 21:
        player_win = False
        print('\nPLAYER BUST. PLAYER LOSES THE BET.')

    elif dealer_sum_cards == 21:
        player_win = False
        print('\nDEALER JACK POT. PLAYER LOSES THE BET.')

    elif dealer_sum_cards > player_cards_sum and dealer_sum_cards < 21:
        player_win = False
        print('\nDealer Wins. Players loses the bet.')

    elif dealer_sum_cards > 21:
        player_win = True
        print('\nDEALER BUST. PLAYER WINS THE BET.')

    elif player_cards_sum == dealer_sum_cards:
        player_win = 3 # Anything besides True, False, Zero or One is OK here.
        print('\nDRAW. No One Wins')

    return player_win


def determine_cash_amount (player_win):
    if player_win == True:
        player.win_your_bet(bet_amount)
        print('Amount of Cash Left:',player.cash)
    elif player_win == False:
        player.lose_your_bet(bet_amount)
        print('Amount of Cash Left:',player.cash)
    else:
        print('Amount of Cash Left:',player.cash)

##
# The Main Program
##

if __name__ == "__main__":

    suits = ("♠", "♥", "♦", "♣")
    ranks = ("K", "Q", "J", "2", "3", "4", "5", "6", "7", "8", "9", "10", "A")
    values = {
            "K": 10,
            "Q": 10,
            "J": 10,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "A": 11
            }

    player = input('Please introduce yourself: ')
    player = Person(player, cash = 100)


    # The Main Loop
    play_again = True
    end = False

    while play_again == True:
        while end == False:

            player_hand = []
            hit_or_stay = 'y'
            player_cards_sum = 0
            dealer_sum_cards = 0

            card = []
            card_list = []

            deck = Deck(ranks, suits)
            deck.create_deck()
            shuffled_deck = deck.shuffle_deck()


            print()
            print(player)
            print('This is your cash amount:', player.cash)
            bet_amount = int(input('Please place your bet: '))
            print('This is your bet amount:', bet_amount)

            player_hand.append(shuffled_deck.pop())
            player_hand.append(shuffled_deck.pop())

            print('\nPlayer Hand')
            print(player_hand)

            player_cards_sum = determine_sum_of_cards_in_the_hand(player_hand)
            print('Player Cards Sum:', player_cards_sum)

            while hit_or_stay == 'y':
                hit_or_stay = input('\nPlayer: Would you like another card (y/n): ')
                if hit_or_stay == 'n':
                    player_cards_sum = determine_sum_of_cards_in_the_hand(player_hand)
                    print('Player Cards Sum:', player_cards_sum)
                    if player_cards_sum == 21:
                        player_win = determine_win_or_lose(player_cards_sum, dealer_sum_cards)
                        determine_cash_amount (player_win)
                        end = True
                    break

                else:
                    player_hand.append(shuffled_deck.pop())

                print('\nPlayer Hand')
                print(player_hand)
                player_cards_sum = determine_sum_of_cards_in_the_hand(player_hand)
                print('Player Cards Sum:', player_cards_sum)
                player_sum_is_OK = evaluate_the_sum(player_cards_sum)
                if player_sum_is_OK == False:
                    player_win = determine_win_or_lose(player_cards_sum, dealer_sum_cards)
                    determine_cash_amount (player_win)
                    end = True
                    break

            if end == True:
                break

            else:
                dealer_hand = []
                dealer = Person('Dealer', cash = 300)

                dealer_hand.append(shuffled_deck.pop())
                dealer_hand.append(shuffled_deck.pop())

                print('\nDealer Hand')
                print(dealer_hand)

                dealer_sum_cards = determine_sum_of_cards_in_the_hand(dealer_hand)
                print('Dealer Cards Sum:', dealer_sum_cards)
                dealer_sum_is_OK = evaluate_the_sum(dealer_sum_cards)
                if dealer_sum_is_OK == False:
                    end = True
                    print('\nDealer Bust. Player wins the bet.')
                    player.win_your_bet(bet_amount)
                    break


                hit_or_stay = 'y'

                while hit_or_stay == 'y':
                    hit_or_stay = input('\nDealer: Would you like another card (y/n): ')
                    if hit_or_stay == 'n':
                        dealer_sum_cards = determine_sum_of_cards_in_the_hand(dealer_hand)
                        print('Dealer Cards Sum:', dealer_sum_cards)
                        if dealer_sum_cards == 21:
                            break
                    else:
                        dealer_hand.append(shuffled_deck.pop())

                    print('\nDealer Hand')
                    print(dealer_hand)
                    dealer_sum_cards = determine_sum_of_cards_in_the_hand(dealer_hand)
                    print('Dealer Cards Sum:', dealer_sum_cards)
                    dealer_sum_is_OK = evaluate_the_sum(dealer_sum_cards)
                    if dealer_sum_is_OK == False:
                        break

                print('\n\nPlayer Cards Sum:', player_cards_sum)
                print('Dealer Cards Sum:', dealer_sum_cards)

                player_win = determine_win_or_lose(player_cards_sum, dealer_sum_cards)
                determine_cash_amount (player_win)

                end = True

        another_round = input('\nWould you like to play again? (y/n): ')
        if another_round == 'y':
            play_again = True
            end = False
        else:
            print('Thank you for playing. The program will end.')
            play_again = False
            end = True
