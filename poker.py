from deuces import *

NUM_CARDS_HAND = 2
NUM_BOARD_CARDS = 5

# for pretty printing
PRETTY_SUITS = {
    "s" : u"\u2660".encode('utf-8'), # spades
    "h" : u"\u2764".encode('utf-8'), # hearts
    "d" : u"\u2666".encode('utf-8'), # diamonds
    "c" : u"\u2663".encode('utf-8') # clubs
}


def main():
    printArt()
    for num in range(0, 3):
        print
    end = "Y"
    while(end == "Y" or end == "y" or end == "yes"):
        play()
        end = raw_input("Play again? Y/N ")

# plays one turn of the simulator, giving the user the option to choose whether
# or not he wants to randomize the choice of the cards to use in the table and
# players' hands. Then, evaluates the ranks of the different players' hands,
# through each turn of the game, and decides whose hands is the best, finally
# printing who is the winning hand.
def play():
    try:
        players = int(raw_input("Please, enter the number of players"
                            + " you want to simulate: "))
    except ValueError:
        print("Invalid number. Exiting...")
        exit()
    deck = Deck()
    evaluator = Evaluator()
    print
    auto = raw_input("Do you want me to choose the cards? Y/N ")
    if (auto == "Y" or auto == "y" or auto == "yes"):
        playersParty = getHands(players, deck)
        board = deck.draw(NUM_BOARD_CARDS)
    else:
        playersParty = setHands(players, deck)
        board = setBoard(deck)
    print
    printPlayerHands(playersParty)
    printTableCards(board)
    print
    summary(playersParty, board, evaluator)

# prints how to manually input the cards, using the rank + suit notation
def tutorial():
    print
    print
    print ("You will input each card one by one, in the following format: ")
    print("(card rank)(suit). Ranks are 2-10, J, Q, K, A and suits are "
            + " h: hearts" + PRETTY_SUITS["h"]
            + " d: diamonds" + PRETTY_SUITS["d"]
            + " c: clubs" + PRETTY_SUITS["c"]
            + " s: spades" + PRETTY_SUITS["s"])
    print
    print("E.g. 10 Hearts " + PRETTY_SUITS["h"] + " will be: 10h ")

# prints all of the cards on the table, or board, in a pretty format, showing
# the suits in colour.
def printTableCards(board):
    print ("Cards on the table: ")
    print
    Card.print_pretty_cards(board)

# prints each of the players' hands in a pretty format, showing ths suits in
# colour
def printPlayerHands(playersParty):
    i = 0
    for player in playersParty:
        print ("Player " + str(i) + "'s hand: ")
        print
        Card.print_pretty_cards(player)
        print
        i += 1

# chooses the player's hands manually, prompting the user for input one card at
# a time
def setHands(players, deck):
    playersParty = []
    tutorial()
    for player in range(0, players):
            playerHand = []
            print
            first = raw_input("Choose player " + str(player) + "'s first card: ")
            if first[0] == "1" :
                newFirst = "T" + first[2]
            else:
                newFirst = first
            firstCard = Card.new(newFirst)
            print
            second = raw_input("Choose player " + str(player) + "'s second card: ")
            if second[0] == "1":
                newSecond = "T" + second[2]
            else:
                newSecond = second
            secondCard = Card.new(newSecond)
            playerHand.append(firstCard)
            playerHand.append(secondCard)
            playersParty.append(playerHand)
    return playersParty

# chooses the board cards manually, prompting the user for one card at a time
def setBoard(deck):
    tutorial()
    board = []
    for num in range(0, NUM_BOARD_CARDS):
        card = raw_input("Board card " + str(num) + " :")
        if card[0] == "1":
            newCard = "T" + card[2]
        else:
            newCard = card
        board.append(Card.new(newCard))
    return board

# automatically chooses each of the players' hands and returns a list with all
# of the players' hands.
def getHands(players, deck):
    playersParty = []
    for player in range(0, players):
        playerHand = deck.draw(NUM_CARDS_HAND)
        playersParty.append(playerHand)
    return playersParty

# prints the summary of the poker turns, bearing who is winning on each of these
# their corresponding ranks, and the final score of the winning hand.
def summary(players, board, eval):
    eval.hand_summary(board, players)


def printArt():
    print("+-----------------------------+")
    print("+        Poker Client         +")
    print("+    For my brother, David    +")
    print("+-----------------------------+")

if __name__ == "__main__":
    main()
