from art import *
import time
from colorama import Fore, Back, Style
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format



def little_animation(delay):
    print("*")
    time.sleep(delay)
    print("**")
    time.sleep(delay)
    print("***")

init()
cprint(figlet_format("Tip calculator", font='starwars'),
       'yellow', attrs=['bold'])
little_animation(0.5)
price =int(input(f"\n {Fore.GREEN}Please enter the price: "))
time.sleep(1)
percent= int(input(f"{Fore.CYAN} Please enter the percent: "))

final = price * (percent/100)

print(f"{Fore.RED} you have to pay {final} dollars [+]")

