'''
Name: Hana Chaudhury 

This program was developed for an assignment for CISC 101 at Queen's University.
This allows users to play a simple one round Crown and Anchor game. Users should be able to
enter a symbol they'd like to bet on and and associated bet amount. Users start with $10 and can
enter bets as long as they have money. A "wheel" spins and returns three random symbols - this is
compared to a user's bet. Winnings are divided as follows: if your symbol doesn't apepar you lose your bet,
if it appears once, you get your bet amount back plus your bet amount, if it appears twice, you get your bet
amount back plus 2x your bet amount and if it appears three times you get your bet amount back plus 3x your
bet amount. The program is currently being modified to become multi-round.
'''

#imports the random and counter functions
#random is for generating random symbols
#counter is to count the number of times each symbol show up in the winning wheel 
import random
from collections import Counter

def createFile():
    f = open("crownanchorsgame_hanachaudhury.txt", "w+")
    f.close()
    
#user enters the number of players in the game 
def numPlayers():
    
    num_players = int(input("Please enter the number of players: "))
    
    return num_players

#this function collects all the user bets - parameter bets that stores all the bets is passed
def playerBets(bets):
    
    #every player starts with $10 -- this would need to be changed with the balance from each round's end
    player_credits = 10
    
    #while player still wants to play and has money the loop will run and ask for bets 
    player_start = input("\nHi! Would you like to play this round? Please enter Y to play, or S to skip round: ")

    #if the player wants to play in the round enter loop 
    if player_start == "Y":
        
        #asks them each time if they want to enter a new bet and because I couldn't get my while loop to work
        #without it
        play_choice = input("Would you like to enter a bet? Enter Y to do so or another key to quit: ")
    
        #while player still wants to enter bets and they have enough money to do so         
        while play_choice == "Y" and player_credits > 0: 
            
            #enter symbol to bet on and amount to bet on each symbol 
            symbol_choice = input("What symbol would you like to bet on? Enter S to skip round: ")
            amount = int(input("How much would you like to bet? Enter 1, 2, 5, or 10: "))

            #should be an error check here but I couldn't figure it out -- user has to enter valid number
            
            #add to the list of dictionaries with symbol being the key and value being the associated bet
            bets.append({symbol_choice: amount})
            #decreases their credit by amount the bet 
            player_credits -= amount
            #tells player how much they have remaining for user friendliness
            print("You have $", player_credits, "remaining.")
            #allows them to enter another bet or close betting
            play_choice = input("\nEnter Y to submit another bet or any other key to close betting: ")

            #if they enter a bet that takes more money than they have 
            if player_credits < 0:
                print("You don't have enough money to bet that.")
                play_choice = "N"

    #skip the round 
    else:
        print("You have skipped this round.")

    #return player credit value 
    return player_credits

#this spins the wheel and returns 3 random symbols 
def spinWheel():
    
    all_symbols = ['crowns', 'anchor', 'hearts', 'diamonds', 'spades', 'clubs']
    wheel_turn= [random.choice(all_symbols), random.choice(all_symbols), random.choice(all_symbols)]
    #wheel_turn = ['anchor', 'anchor', 'anchor'] -- for you check if it's all three anchors 

    #tells the user 
    print("This is the winning wheel:", wheel_turn) 

    #returns the winning wheel 
    return wheel_turn

#function that does the arithmetic 
def winning(wheel_turn, bets, player_credits):

    #dictionary that holds number of times each symbol appears in the winning wheel
    num_elements_wheel = {}
    #variable name that changes player's credit
    balance = player_credits
    new_balance = [] 
    #loops through the winning wheel and adds it to the dictionary where key is the symbol
    #and the value is the number of times it apepars 
    for key, value in Counter(wheel_turn).items():
        num_elements_wheel[key] = value
        
    #loops through each elements in bets - i.e. each dictionary 
    for index in range(len(bets)):
        #accesses each key in each dictionary 
        for key in bets[index]:
            #if the key is present in the winning wheel 
            if key in num_elements_wheel:
                #get the value for the key associated with it 
                number_of_wins = num_elements_wheel[key]
                #output based on number of time each symbol appears

                #if anchor is your bet and appears all three tiems
                if key == "anchor" and number_of_wins == 3:
                    balance += 3*bets[index][key]
                    print("Winner on Anchors -- Ahoy!!!!")

                #outputs based on number of times your bets appear 
                if number_of_wins == 1:
                    #adds right value to balance
                    balance += bets[index][key]
                    #prints what you won for and how much you won
                    print("You won once for", key, "! You win:", balance) 
                elif number_of_wins == 2:
                    balance += 2*bets[index][key]
                    print("You won twice for", key, "! You win:", balance) 
                elif number_of_wins == 3:
                    balance += 3*bets[index][key]
                    print("You won thrice for", key, "! You win:", balance) 
      
            #if key is not in winning wheel then subtracts bet value 
            elif key not in num_elements_wheel:
                print("For", key, "You didn't win. You lost your bet amount.") 
                balance -= bets[index][key]
                
            new_balance.append(balance)
            print(new_balance) 

   #prints and returns balance 
    print("Your balance is: $", balance) 
    return balance

def writetofile(new_balance): 
    #writes the results to the text file
    f = open("crownanchorsgame_hanachaudhury.txt", "a")
    f.write("\nPlayer's balance")
    f.write(str(new_balance))
    f.close() 

#main function 
def main():
    
    #creates the file! 
    createFile()
    #sets out rules 
    print("Welcome to a Crown and Anchors Game! Here are some rules. You can only bet"
          "\non the following symbols: crowns, anchor, hearts, diamonds, clubs and spades."
          "\nYou can only bet in increments of 1, 2, 5, or 10. You cannot enter bets more"
          " than once per symbol in each round. Good luck!\n")

    #holds the bets per player
    bets = []
    #number of players 
    num_players = numPlayers() 
    player_credits = playerBets(bets)
    wheel_turn = spinWheel()
    #passes winning wheel, list of bets, and how much player has 
    balance = winning(wheel_turn, bets, player_credits)
    #writes file with appropriate balance
    writetofile(balance)
    #reminds the user of their bet
    print("This was your bet:", bets)

    #if there are multiple user loops through again and lets the next player play the game
    while balance > 0: 
        for i in range(num_players-1):
        #new dictionaries created for each new player 
            bets = []
            #calls all functions again 
            player_credits = playerBets(bets)
            wheel_turn = spinWheel()
            balance = winning(wheel_turn, bets, player_credits)
            writetofile(balance)
            print("This was your bet:", bets)

    main()
