'''
Name: Hana Chaudhury

This was developed for an assignment for CISC 101 at Queen's University.

This is a dice game. Using loops and if statements it allows the user to roll 2 dice, with
random outputs, get points for certain values rolled and get a running tally of their score.

'''
def diceGame():
    
    #imports random and allows us to use it later
    
    import random
    
    #welcomes the user to the game and asks if they would like to play the game and explains the point system 
    print("Welcome to a dice game. You will be asked if you want to roll the dice. Both dice will roll at once.",
          "You will get 10 points for every double rolled, 4 points for every 6 rolled, and 2 points if the sum",
          "of your rolls is 7. You will get a running tally of your score after each roll and point scored.")

    #defines the first variable for user to input if they would like to roll the dice to start the game 
    roll_choice = input("\nWould you like to roll the dice? Enter Y to roll again or N to stop: ")

    totalScore = 0 
    
    #activates if the user chooses to play the game 6y
    while roll_choice == "Y":

        #rolls both dice, randomizes the value from 1 - 6 and prints the result for each roll 
        first_roll = random.randint(1,6)
        print("\nYour first roll is", first_roll)

        second_roll = random.randint(1,6)
        print("Your second roll is", second_roll)

        #the following if statements assigns the user points based on the value of their rolls

        #assigns 10 points for doubles and adds to the total score 
        if first_roll == second_roll:
            totalScore += 10
            print("You rolled doubles. You get 10 points.")

        #assigns 4 points for rolling 6's and adds to the total score
        #both are needed in case they roll 6's both times 
        if first_roll == 6:
            totalScore += 4
            print("You rolled a 6 for your first roll. You get 4 points.")

        if second_roll == 6:
            totalScore += 4
            print("You rolled a 6 for your second roll. You get 4 points.")

        #assigns 7 points if the sum of both rolls is 7 and adds to the total score 
        if (first_roll + second_roll) == 7:
            totalScore += 2
            print("The sum of both rolls is 7. You get 2 points.")
        
        #prints the user's total score 
        print("Your total score is", totalScore)

        #asks the user if they would like to play again
        #if they select yes the loop repeats
        #if they select no the game will stop 
        roll_choice = input("\nWould you like to roll again? Enter Y to roll again or N to stop: ")

    #indicates end of game if user decides to quit 
    print("\nThanks for playing. Your final score is %d." % totalScore)

diceGame()




