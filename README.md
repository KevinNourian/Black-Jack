# Black Jack

## Description
This is a simulation of the Black Jack card game. 

## Rules
* Two players: Player and Dealer
* Player places a bet and is dealt two cards.
* Dealer receives two card.
* Player continues to hit (get a card) until Player stays or exceeds 21.
* If Player exceeds 21, it's a BUST. Player loses.
* After Player stays, Dealer draws cards until Dealer stays or exceeds 21.
* If Dealer exceeds 21, it's a BUST. Dealer loses.
* If Player has a sum higher than Dealer, Player wins.
* If Dealer has a sum higher than Player, Player wins.
* If Dealer and Player have the same sum. No one wins.

## Logic
1. Create shuffled deck of cards. 
2. Create two players: Player and Dealer
3. Pop two card from the deck and add to Player card list. 
4. Pop two card from the deck and add to Dealer card list. 
5. While sum is less than 21:
  * Ask Player if another card is needed.
  * If sum exceeds 21, Player loses. Game is over.
6. While sum in less than 21:
  * Delaer draws another card.
  * If sum exceeds 21, Dealer loses. Game is over.
7. As Player is hit, the sum is shown. When Player stays, the sum of the dealer's deck begins showing.
8. The sum of Player and Dealer are compared. The higher sum wins.
9. Player and Dealer winning and losing are calculated.
10. Player is asked if he/she wants to play again.

## Execution
Run `Blackjack.py`

