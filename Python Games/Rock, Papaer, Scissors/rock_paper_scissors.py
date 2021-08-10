from random import randint
import os
import time
from playsound import playsound


def print_intro():
    print("""
        █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
        ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█
        """)
    print("""      
        ██████╗░░█████╗░░█████╗░██╗░░██╗░░░  ██████╗░░█████╗░██████╗░███████╗██████╗░░░░
        ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝░░░  ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗░░░
        ██████╔╝██║░░██║██║░░╚═╝█████═╝░░░░  ██████╔╝███████║██████╔╝█████╗░░██████╔╝░░░
        ██╔══██╗██║░░██║██║░░██╗██╔═██╗░██╗  ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗██╗
        ██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗╚█║  ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║╚█║
        ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝░╚╝  ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝░╚╝
        """)
    print("""            
        ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
        ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
        ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
        ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
        ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
        ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░
        """)
    print("""        
        █▀▀ █▀█ █▀█ █▀▄   █░░ █░█ █▀▀ █▄▀ █
        █▄█ █▄█ █▄█ █▄▀   █▄▄ █▄█ █▄▄ █░█ ▄
        """)
    

def print_game_choice():
    print("""      
        █─▄▄─███▀▀▀▀███▄─▄▄▀█─▄▄─█─▄▄▄─█▄─█─▄█
        █─██─███▀▀▀▀████─▄─▄█─██─█─███▀██─▄▀██
        ▀▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▀▄▄▀▄▄▄▄▀▄▄▄▄▄▀▄▄▀▄▄▀
        """)
    print("""      
        █▀░████▀▀▀▀███▄─▄▄─██▀▄─██▄─▄▄─█▄─▄▄─█▄─▄▄▀█
        ██░████▀▀▀▀████─▄▄▄██─▀─███─▄▄▄██─▄█▀██─▄─▄█
        ▀▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▀▀▀▄▄▀▄▄▀▄▄▄▀▀▀▄▄▄▄▄▀▄▄▀▄▄▀
        """)
    print("""
        █▀▄▄▀███▀▀▀▀███─▄▄▄▄█─▄▄▄─█▄─▄█─▄▄▄▄█─▄▄▄▄█─▄▄─█▄─▄▄▀█─▄▄▄▄█
        ██▀▄████▀▀▀▀███▄▄▄▄─█─███▀██─██▄▄▄▄─█▄▄▄▄─█─██─██─▄─▄█▄▄▄▄─█
        ▀▄▄▄▄▀▀▀▀▀▀▀▀▀▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀
        """)
    print("""
        █▀▄▀█ ▄▀█ █▄▀ █▀▀   █▄█ █▀█ █░█ █▀█   █▀▀ █░█ █▀█ █ █▀▀ █▀▀
        █░▀░█ █▀█ █░█ ██▄   ░█░ █▄█ █▄█ █▀▄   █▄▄ █▀█ █▄█ █ █▄▄ ██▄
        """)
        
        
def print_symbol_game(choice):
    
    if(choice == 0):
        # Rock
        print("""
            _______
        ---'   ____)
            (_____)
            (_____)
            (____)
        ---.__(___)
        """)

    if(choice == 1):
        # Paper
        print("""
            _______
        ---'    ____)_____
                __________)
                __________)
                ________)
        ---.__________)
        """)

    if(choice == 2):
        # Scissors
        print("""
            _______
        ---'   ____)__
                ______)
            __________)
            (____)
        ---.__(___)
        """)


def print_draw():
    print("""
        ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░███░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░██████████░░░░░░█
        █░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██████████░░▄▀░░█
        █░░░░▄▀░░░░█░░░░░░▄▀░░░░░░█░░░░░░█░░▄▀░░░░░░░░░░████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
        ███░░▄▀░░███████░░▄▀░░█████████░░█░░▄▀░░████████████░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██████████░░▄▀░░█
        ███░░▄▀░░███████░░▄▀░░████████████░░▄▀░░░░░░░░░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░░░░░██░░▄▀░░█
        ███░░▄▀░░███████░░▄▀░░████████████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
        ███░░▄▀░░███████░░▄▀░░████████████░░░░░░░░░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░██░░▄▀░░█
        ███░░▄▀░░███████░░▄▀░░████████████████████░░▄▀░░████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
        █░░░░▄▀░░░░█████░░▄▀░░████████████░░░░░░░░░░▄▀░░████░░▄▀░░░░▄▀▄▀░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█
        █░░▄▀▄▀▄▀░░█████░░▄▀░░████████████░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░░░▄▀░░█
        █░░░░░░░░░░█████░░░░░░████████████░░░░░░░░░░░░░░████░░░░░░░░░░░░███░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░██░░░░░░██░░░░░░█
        ████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        """)
       
        
def print_win():
    print("""
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░████░░░░░░██████████░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█
        █░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░░░░░░░░░██░░▄▀░░█
        █░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░█░░░░▄▀░░░░█░░▄▀▄▀▄▀▄▀▄▀░░██░░▄▀░░█
        ███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██████████░░▄▀░░███░░▄▀░░███░░▄▀░░░░░░▄▀░░██░░▄▀░░█
        ███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░░░░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
        █████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
        ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░██░░▄▀░░██░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░██░░▄▀░░█
        ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░░░░░▄▀░░░░░░▄▀░░███░░▄▀░░███░░▄▀░░██░░▄▀░░░░░░▄▀░░█
        ███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░████░░▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀░░█░░░░▄▀░░░░█░░▄▀░░██░░▄▀▄▀▄▀▄▀▄▀░░█
        ███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀░░░░░░▄▀░░░░░░▄▀░░█░░▄▀▄▀▄▀░░█░░▄▀░░██░░░░░░░░░░▄▀░░█
        ███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░██░░░░░░██░░░░░░█░░░░░░░░░░█░░░░░░██████████░░░░░░█
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████████
        """)


def print_lose():
    print("""     
        █████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        █░░░░░░░░██░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░████░░░░░░█████████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        █░░▄▀▄▀░░██░░▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░░░▄▀░░██░░▄▀░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        ███░░▄▀▄▀░░▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████
        ███░░░░▄▀▄▀▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        █████░░░░▄▀░░░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
        ███████░░▄▀░░███████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░████░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████████░░▄▀░░█░░▄▀░░█████████
        ███████░░▄▀░░███████░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█
        ███████░░▄▀░░███████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        ███████░░░░░░███████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░████░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        █████████████████████████████████████████████████████████████████████████████████████████████████████████████████
        """)
    

def print_play_again():
    print('''
        █▀▄ █▀█   █▄█ █▀█ █░█   █░█░█ ▄▀█ █▄░█ ▀█▀   ▀█▀ █▀█   █▀█ ▄▀█ █░░ █▄█   ▄▀█ █▀▀ ▄▀█ █ █▄░█ ▀█
        █▄▀ █▄█   ░█░ █▄█ █▄█   ▀▄▀▄▀ █▀█ █░▀█ ░█░   ░█░ █▄█   █▀▀ █▀█ █▄▄ ░█░   █▀█ █▄█ █▀█ █ █░▀█ ░▄▀
        ''')

        
def print_choice():
    print("""     
        █▄█ █▀▀ █▀   █▀█ █▀█   █▄░█ █▀█ ▀█
        ░█░ ██▄ ▄█   █▄█ █▀▄   █░▀█ █▄█ ░▄
        """)


def computer_choice(choice_options):
    '''
    Function to return random value from 0 to len(choice_options)
    '''
    computer_choice = randint(0,len(choice_options)-1)
    return computer_choice


def user_input(): 
    '''
    Function to get user input and return it
    '''
    print_game_choice()
    
    user_choice = int(input())
    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    return user_choice


def check_results(player, computer):
    '''
    Function to check the game results
    '''
    print("""
        █▄█ █▀█ █░█
        ░█░ █▄█ █▄█
    """)
    print_symbol_game(player)
    print("\n\n\n")
    print("""  
        █▀▀ █▀█ █▀▄▀█ █▀█ █░█ ▀█▀ █▀▀ █▀█
        █▄▄ █▄█ █░▀░█ █▀▀ █▄█ ░█░ ██▄ █▀▄
    """)
    print_symbol_game(computer)
    
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    win = os.path.join(__location__, 'win.mp3')
    lose = os.path.join(__location__, 'game_over.wav')
    
    if(player == computer):
        print_draw()
    else:
        if((player == 0 and computer == 2) or (player>computer and not(player==2 and computer==0))):
            print_win()
            playsound(win)
        else:
            print_lose()
            playsound(lose)


def play_game():
    '''
    Game function
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    options_list = ['Rock', 'Paper', 'Scissors']
    
    user_choice = user_input()
    computer_choice_input = computer_choice(options_list)
    check_results(user_choice, computer_choice_input)
        
    
def main():
    play_again = ""
    print("\n")
    print_intro()
    print("\n")
    time.sleep(3)
    while play_again != "n":
        play_game()
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        print_play_again()
        print_choice()
        play_again = input()      
        os.system('cls' if os.name == 'nt' else 'clear')  
        
        
main()