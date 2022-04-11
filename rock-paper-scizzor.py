import random 
import time
from playsound import playsound
choice = True
user_life = 3
bot_life = 3
print("RULES ==> You have 3 lifes. if you go to zero you lose.")
while choice == True:
    choicelist = ["rock","paper","scizzor"]
    user_attack = input("pls enter the action: ")
    bot_attack = random.choice(choicelist)
    if user_attack == bot_attack:
        print(f"nothing happened you still have {user_life} lives!!")
    if user_attack == "rock" and bot_attack == "scizzor":
        print("You won!!")
        time.sleep(0.5)
        bot_life = bot_life -1
        print(f"Bot has {bot_life} lives. ")
    if user_attack == "rock" and bot_attack == "paper":
        print("You lost!!")
        time.sleep(0.5)
        user_life = user_life - 1
        print(f"bot's action was {bot_attack}")
        time.sleep(0.5)
        print(f"you have {user_life} lives.")
    if user_attack == "paper" and bot_attack == "rock":
        print("You won!!")
        time.sleep(0.5)
        bot_life = bot_life -1
        print(f"bot has {bot_life} lives.")
    if user_attack == "paper" and bot_attack == "scizzor":
        print("You lost!!")
        time.sleep(0.5)
        user_life = user_life-1
        print(f"bot's action was {bot_attack}")
        time.sleep(0.5)
        print(f"you have {user_life} lives.")
    if user_attack == "scizzor" and bot_attack == "paper":
        print("You won!")
        time.sleep(0.5)
        bot_life = bot_life -1
        print(f"bot has {bot_life} lives.")
    if user_attack == "scizzor" and bot_attack == "rock":
        print("You lost")
        time.sleep(0.5)
        user_life = user_life -1
        print(f"bot's action was {bot_attack}")
        time.sleep(0.5)
        print(f"You have {user_life} lives.")
    if user_life == 0 or bot_life ==0:
        a = True
        while a == True:
            answer = input("Would you like to play again? ")
            print("Write yes or no")
            if answer == "yes":
                choice = True
                a = False
            if answer == "no":
                choice = False
                break
            
