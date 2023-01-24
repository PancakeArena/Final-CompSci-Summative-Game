# Name: Ansh
# Start date: 01/11/23
# Due date: 01/23/23
# BlackJack_game
# Final computer science sourse summative - create a game. I decided to create
# the game Blackjack in python using various coding concepts taught in this
# course and to compile my knowledge.

from random import randint
from graphics import *

# Functions
# this function allows the Ace card to be chosen as 1 or 11 according to the player
def card_value(card):
    if card[:1] in ('J','Q','K','1'):
        return int(10)
    elif card[:1] in ('2','3','4','5','6','7','8','9'):

        return int(card[:1])
    elif card[:1] == 'A':
        print ("\n"+ str(card))
        num = input("Do you want this to be 1 or 11?\n>")
        while num !='1' or num !='11':
            if num == '1':
                return int(1)
            elif num == '11':
                return int(11)
            else:
                num = input("Do you want this to be 1 or 11?\n>")

# deck function/draw card function
def card_create():
    suits = ['Clubs','Spades','Hearts','Diamonds']
    deck = []
    value = ['Ace','2','3','4','5','6','7','8','9','10','J','Q','K']
    for type in suits:
        for num in value:
            deck.append(num + ' of ' + type)
    return deck

# draw card function
def new_card(deck):
    return deck[randint(0,len(deck)-1)]

# remove card function
def remove_card(deck,card):
    return deck.remove(card)

# menu screen function
def menu_screen():
  # creating the window
  win = GraphWin("Menu_window", 1250, 550)

  # displaying the menu image
  menu_img = Image(Point(625, 275), "Blackjack.menu.screen.png")
  menu_img.draw(win)

  win.getMouse()
  win.close()

# exit screen function
def exit_screen():
  # creating the window
  win = GraphWin("Exit_window", 799, 449)

  # displaying the exit image
  exit_img = Image(Point(400, 225), "Blackjack.exit.screen.png")
  exit_img.draw(win)

  win.getMouse()
  win.close()

# Main program
menu_screen()
play_again = ''
# using .upper so that game will always exit no matter how 'exit' is typed/inputted
while play_again.upper() != 'EXIT':
    # creating the deck and cards with their values, summing up the total
    new_deck = card_create()
    card1 = new_card(new_deck)
    remove_card(new_deck,card1)
    card2 = new_card(new_deck)
    remove_card(new_deck,card2)
    print ("\nYou Have a " + card1 + " and " + card2) # doing this statement first allows for the 'Ace' card value selection between 1 and 11
    valu1 = card_value(card1)
    valu2 = card_value(card2)
    total = valu1 + valu2
    print("For a total of " + str(total) )

    # dealer
    dealer_card1 = new_card(new_deck)
    remove_card(new_deck,dealer_card1)
    dealer_card2 = new_card(new_deck)
    remove_card(new_deck,dealer_card2)
    dealer_value1 = card_value(dealer_card1)
    dealer_value2 = card_value(dealer_card1)
    dealer_total = dealer_value1 + dealer_value2
    print ("\nFirst the dealer draws a " + dealer_card1 + " and Face down card.\nFor a Total of", dealer_value1)

    # instant win
    if total == 21:
        print("Blackjack! Perfect!")
    else:
        while total < 21: # the game is not won/lost
            answer = input("\nWould you like to hit or stand?\n> ")
            # if player decided to hit (draw another card)
            if answer.lower() == 'hit':
                # additional card creation and summing up the total
                more_card = new_card(new_deck)
                remove_card(new_deck,more_card)
                more_value = card_value(more_card)
                total += int(more_value)
                print (more_card + " for a new total of " + str(total))
                if total > 21: # losing condition
                    print("You Bust Loser")
                    play_again = input("Would you like to continue? EXIT to leave\n")
                    
                elif total == 21: # winning condition 
                    print("You WIN BIG WOO WOO")
                    play_again = input("Would you like to continue? EXIT to leave\n")
                     
                else:
                    continue
            # if player decided to stand (keep cards and view dealers hidden card + dealer draws another card)
            elif answer.lower() == 'stand':
                print("The Dealer reveals his other card to be ")
                print("a " + dealer_card2 + " \nfor a total of " + str(dealer_total))
                if dealer_total < 17:
                    print("The Dealer hits again.")
                    dealer_more = new_card(new_deck)
                    more_dealer_value = card_value(dealer_more)
                    print("The card is a " + str(dealer_more))
                    dealer_total += int(more_dealer_value)
                    # player win
                    if dealer_total > 21 and total <=21:
                        print("Dealer Bust! You win!")
                    # player loss
                    elif dealer_total < 21 and dealer_total > total:
                        print("Dealer has " + str(dealer_total) + " You lose!")
                    else:
                        continue
                # tie game
                elif dealer_total == total:
                    print("Equal Deals, no winner")
                # player win dealer loss
                elif dealer_total < total:
                    print("You win!")
                # player loss, dealer win
                else:
                    print("You Lose!")
                # replayability
                play_again = input("\nWould you like to continue? EXIT to leave\n")
              
                break
print("Thank you for Playing")
exit_screen()

 
  