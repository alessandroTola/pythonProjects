from random import randint


def computer_choice(choice_options):
    '''
    Function to return random value from 0 to len(choice_options)
    '''
    computer_choice = randint(0,len(choice_options)-1)
    return computer_choice


def user_input(options): 
    '''
    Function to get user input and return it
    '''
    for index,options in enumerate(options):
        print(f'{index} = {options}')
        
    user_choice = int(input('make your choice '))
    return user_choice


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
        ---'    ____)____
                ______)
                _______)
                _______)
        ---.__________)
        """)

    if(choice == 2):
        # Scissors
        print("""
            _______
        ---'   ____)____
                ______)
            __________)
            (____)
        ---.__(___)
        """)
   
        
def check_results(player, computer):
    '''
    Function to check the game results
    '''
    print_symbol_game(player)
    print("\n\n\n")
    print_symbol_game(computer)
    
    if(player == computer):
        return  "It's draw"
    elif((player == 0 and computer == 2) or (player>computer and not(player==2 and computer==0))):
        return "You won"
    
    return "You lose"


def play_game():
    '''
    Game function
    '''
    print("\n")
    print("Welcome to the Rock, Paper, Scissors, game")
    print("Good luck")
    print("\n")
    
    options_list = ['Rock', 'Paper', 'Scissors']
    
    user_choice = user_input(options_list)
    computer_choice_input = computer_choice(options_list)
    result = check_results(user_choice, computer_choice_input)
    
    print(result)
    
    
def main():
    play_again = ""
    
    while play_again != "n":
        play_game()
        print("Do you want to play again?")
        print("y/n")
        play_again = input()        
        
        
main()