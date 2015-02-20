import random

#Initialize
game_running = True
bonus_flag = False

print ("Welcome to Northwest Vista College!")
name = input("What is your name?\n\n")

score = 20
gear = "wallet"

while game_running:


    print("\nGet ready,", name, ", the game is starting!")
    
    flag01 = True
    flag02 = True
    flag03 = True
    flag04 = True
    
    while flag01:

    
        print ("\nYou're sitting at a table.",
            "Your bag lies on top of the table.")

        choice = input("What would you like to do? \n[1] - Take \n[2] - Leave\n\n")                    

        if choice == '1':

            print ("\nYou take the bag.\n")
            score += 5
            flag01 = False
            
        elif choice == '2':

            print ("\nYou shouldn't leave without your things.")

        else:

            print ("\nThat is not a valid choice.\n")




    while flag02:

        print("There are paths to the Left and the Right. \nWhich way will you go?")
        choice = input("[1] - Left\n[2] - Right\n\n")


        if choice == '1':

            print("\nYou come to the stairs leading up to the second floor where your class is.")
            flag02 = False


        elif choice == '2':

            flag02B = True
                  

            while flag02B != False:
                  
                print("\nA student stops you and asks you for directions to the Library. \nWhat do you do?")
                choice = input("[1] - Give them directions\n[2] - Lie. Tell them you don't know.\n\n")

                if choice == '1':

                    print("\nYou give the student directions to their destination.")
                    score += 10
                    
                    print("You continue forward and come across the stairs leading",
                        "up to the second floor where your class is.")
                    flag02 = False
                    flag02B = False
                    
                elif choice == '2':

                    print("The student waves and departs.\n",
                        "You continue on your way and arrive at the stairs leading",
                        "to the second floor where your classroom is\n")
                    score -= 5
                    flag02 = False
                    flag02B = False

                else:

                    print("That is not a valid response. Please try again.")

        else:

            print("That is not a valid response. Please try again.")





    while flag03:


        print("You are standing at the foot of the stairwell. \nWhat will you do?")
        choice = input("[1] - Climb the stairs to the 2nd floor\n[2} - Skip class and go home\n\n")

        if choice == '1':

            print("\nYou arrive at the second floor and find two hallways, one to your left and one to your right.",
                "\nStudent and staff dot each hallway making light conversation.",
                "Your class is down the left hallway.")
                
            print("Which hall do you take?:")
            choice = input("[1] - Right hallway\n[2] - Left Hallway\n\n")

            if choice == '1':

                print("\nYou take the right hallway, recalling the sole vending machine that sells your favorite",
                    "drink is down this hallway.\nYou make a beeline directly to it, hoping it's still stocked.")
                score += 5
                
                print("Having made your selection, the vending machine prompts you for one dollar and twenty-five cents.",
                    "\nYou can:")
                
                choice = input("[1] - Check your wallet\n[2] - Beg (annoy) people for it.\n\n")

                if choice == '1':

                    print("\nYou find your credit card stashed in your wallet and use it to purchase the drink.",
                        "\nYou take the drink and make your way to your classroom.")
                    score += 5
                    gear = "Cherry Cola"
                    
                    flag03 = False
                          
                elif choice == '2':

                    print("\nYou plead, quite pathetically, for someone to loan you money for your drink.",
                        "Eventually, someone does. You buy your drink and take off to class.")
                    score -= 10
                    gear = "Cherry Cola"
                    
                    flag03 = False

            elif choice == '2':

                print("\nYou head down the left hallway and make it a few feet from the classroom when nature calls.",
                    "Heading for the bathroom, you take some time to recover and readjust yourself.")
                score -= 5
                
                flag03 = False

            else:

                print("That is not a valid answer, please try again.")

        if choice == '2':

            print("\nYou turn around and go home. Game Over.",
                "Your final score is: ", score)
            
            flag03 = False
            flag04 = False
            game_running = False

                              



    while flag04:


        print("You are standing outside your classroom. \nStudents trickle in",
            "preparing for the start of class. \nWhat would you like to do?")
        
        choice = input("[1] - Enter the classroom\n[2] - Put your drink in your bag\n\n")
        
        if choice == '1':

            print("As you enter the classroom, the professor anounces that class is about to start in",
                "one minute and\nrequests that everyone who has their completed homework turn it in before",
                "class starts.\nRemembering that you finished your homework and brought it with you, you fish",
                "through your bag.\nRight before you take it out of the bag, the Professor announces that",
                "class has started and that she is no longer accepting homework.")
            score -= 10

            flag04 = False
                  
        elif choice == '2':

            print("You place your", gear, "in your bag and see your homework at the back of your folder.",
                "Recalling that this assignment is due before class starts, you quickly look it over to",
                "make sure your name is on it and all the questions are answered. \nThey are. You step in", 
                "the classroom, greet the Professor, hand in your assignment, and take your seat.",
                "A few minutes later the Professor announces that class has begun.\n")
            score += 15

            flag04 = False

        else:

            print("That is not a valid answer. Please try again.")

    print("Your final score is:", score)

    if score == 60:

        bonus_flag = True
        
    while bonus_flag:


        player_level = 1

        def player_health( player_level ):
            health = 30 + ( (player_level - 1 ) * 30)
            return health;
            
        def player_offense( player_level ):
            player_attack = 0
            attack_one = (random.randint(2, 3) + player_level * 3)
            attack_two = (random.randint(2, 3) + player_level * 3)
            player_attack = attack_one + attack_two + player_level - 1
            return player_attack;

        def skill_mend( player_level ):
            healing = 5 ((5 * player_level) + player_level)
            return healing;

        def enemy_health( player_level ):
            health = 30 * ( (player_level - 1) + 1)
            return health;
            
        def janitor_offense():
            janitor_attack = 0
            attack_one = random.randint(1, 4)
            attack_two = random.randint(1, 4)
            janitor_attack = attack_one + attack_two
            return janitor_attack;

        def intern_offense():
            intern_attack = 0
            attack_one = random.randint(2, 6)
            attack_two = random.randint(1, 5)
            intern_attack = attack_one + attack_two
            return intern_attack;

        def professor_offense():
            professor_attack = 0
            attack_one = random.randint(3, 4)
            attack_two = random.randint(2, 8)
            professor_attack = attack_one + attack_two
            return professor_attack;

        print("Your Professor leaps onto her desk wearing a black cloak and pointed hat.",
            "\nShe points directly at you and says, 'Seeing as how you managed to get to",
            "the Bonus Round, we'll play a little game.\nIf you can defeat my 2 henchmen", 
            "and myself, I give extra credit points on your final grade!'")

        print("At that moment, a 'husky' janitors bursts into the room, swinging his",
           "push-broom like a clumsy halberd.\nAfter a show of wild, but not particularly", 
           "impressive 'moves', he targets you and charges. Get ready!")
            
        battle_one = True

        print("\nBattle One begins!")
        print(name, "and Evil Janitor enter the battle.")

        player_hitpoints = player_health( player_level )
        janitor_hitpoints = enemy_health( player_level )


        while battle_one:

                    
            print(name, "has", player_hitpoints, "hit points and Evil Janitor has", janitor_hitpoints, " hit points.\nCommands:")
            choice = input("[1] - Attack \n[2] - Skill: Mend\n\n")

            if choice == '1':

                player_attack = player_offense( player_level )
                janitor_attack = janitor_offense()
                
                janitor_hitpoints -= player_attack
                player_hitpoints -= janitor_attack
                            
                print(name, "hits Evil Janitor for", player_attack, "damage.",
                    "Evil Janitor hits", name, "for", janitor_attack, "points.")

            elif choice == '2':

                healing = skill_mend( player_level )
                janitor_attack = janitor_offense()

                print(name, "uses MEND, restoring", healing, "health.")
                player_hitpoints += healing

                print("Evil Janitor attacks", name, "for", janitor_attack, ".")
                player_hitpoints -= janitor_attack

            else:

                 print("That is not a valid command. Please try again.")

            if player_hitpoints < 1:

                print(name, "has been slain by Evil Janitor. Game Over.")

                battle_one = False
                bonus_flag = False
                game_running = False
                                      
            if janitor_hitpoints < 1:

                print("Evil Janitor falls to the floor and after a moment, lies completely still.", name,
                    "has defeated Evil Janitor!")
                print(name, "has gained a level.\n\n",
                    name, "is now level 2!")

                battle_one = False


        print("The Professor, observing the battle, claps slowly.", "Congratulations, but you still have my",
            "other minion to worry about. Let's see how well you do against... THE INTERN OF UNPAID LABOR!",
            "\nA willowy thin young girl approaches you slowly, and after struggling a bit to meet your gaze",
            "brandishes a taser and a bottle of pepper spray. Her resentful gaze pierces your soul.")

        battle_two = True

        print("\nBattle Two begins.",
            "\n", name, "and Intern of Unpaid Labor enter the battle.")

        player_level += 1
        player_hitpoints = player_health( player_level )
        intern_hitpoints = enemy_health( player_level )
    
        while battle_two:
    
            print(name, "has", player_hitpoints, "hit points and Intern of Unpaid Labor has", intern_hitpoints, ".\nCommands:")
            choice = input("[1] - Attack \n[2] - Skill: Mend\n\n")
                    
            if choice == '1':

                player_attack = player_offense( player_level )
                intern_attack = intern_offense()

                intern_hitpoints -= player_attack
                player_hitpoints -= intern_attack

                print(name, "hits Intern of Unpaid Labor for", player_attack, "hit points",
                    "Intern of Unpaid Labor hit", name, "for", intern_attack, "hit points.")

            elif choice == '2':

                intern_attack = intern_offense()
                healing = skill_mend( player_level )
                player_hitpoints += healing
                            
                print(player, "has recovered", healing, "hitpoints.")
                            
                player_hitpoints -= intern_attack
                print("Intern of Unpaid Labor attacks", name, "for", intern_attack, "points of damage.")

            else:

                print("\nThat is not a valid command.\n")

            if player_hitpoints < 1:

                print(name, "has been slain by Intern of Unpaid Labor. Game Over.")

                battle_two = False
                bonus_flag = False
                game_running = False
                                      
            if intern_hitpoints < 1:

                print("Intern of Unpaid Labor lies on the floor, glaring at you.",
                    "\nGraudually, her breathing slows and soon, stops all together.",
                    "\bHer eyes remained fixed on yours and the glare never leaves her face.",
                    "\n", name, "has defeated Intern of Unpaid Labor!")

                print(name, "has gained a level.\n",
                    name, "is now level 3!\n\n")
                            
                battle_two = False


        battle_three = True

        print("\nBattle Three begins.",
            name, "and The Profesor enter the battle.")     

        player_level += 1
        player_hitpoints = player_health( player_level )
        professor_hitpoints = enemy_health( player_level )
                
        while battle_three:


            print(name, "has", player_hitpoints, "hit points,  The Professor has", professor_hitpoints, "hit points.\nCommands:")
            choice = input("[1] - Attack \n[2] - Skill: Mend\n\n")
                
            if choice == '1':

                player_attack = player_offense( player_level )
                professor_attack = professor_offense()

                player_hitpoints -= professor_attack
                professor_hitpoints -= player_attack
                
                print("\n\n", name, "hits The Professor for", player_attack, ".\n",
                    "The Professor hits", name, "for", professor_attack, ".")

            elif choice == '2':
                
                healing = skill_mend( player_level )
                player_hitpoints += healing

                print("\n\n", player, "has recovered", healing, "hitpoints.")

                professor_attack = professor_offense()        
                player_hitpoints -= professor_attack

                print("The Professor attacks", name, "for", professor_attack, "points of damage.")

            else:

                print("\n\nThat is not a valid command.\n")

            if player_hitpoints < 1:

                print("\n", name, "has been slain by Intern of Unpaid Labor. Game Over.")

                battle_three = False
                bonus_flag = False
                game_running = False
                                  
            if professor_hitpoints < 1:

                print("\nThe Professor collapses to the floor. 'Well... I guess... you win...\n",
                    "My only regret... is using this bonus round instead of homework...\n",
                    "Your classmates sit up from their chairs. The bewildered look on their faces doesn't \n",
                    "leave for a moment as they gather up their things and mutter thanks for a homework free weekend.")

                print("As you turn to leave, the Evil Janitor, Intern of Unpaid Labor, and The Professor get up and,",
                    "continue about their business as if nothing happend.",)
                
                battle_three = False

        bonus_flag = False
        
            
        print("Congratulations, you've won the game!")

        game_running = False

    else:

        print("You made it to the end. Would you like to play again?")
        choic = input("[1] - Play again")

        if input != '1':
            game_running = False

    
print("Thank you for playing! Good bye!")




