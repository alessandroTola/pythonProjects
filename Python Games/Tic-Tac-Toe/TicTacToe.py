import os
import time
from playsound import playsound
from pathlib import Path


def print_intro():
    print("""
        █░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀   ▀█▀ █▀█
        ▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄   ░█░ █▄█
        """)
    print("""      
        ████████╗██╗░█████╗░  ████████╗░█████╗░░█████╗░  ████████╗░█████╗░███████╗
        ╚══██╔══╝██║██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝
        ░░░██║░░░██║██║░░╚═╝  ░░░██║░░░███████║██║░░╚═╝  ░░░██║░░░██║░░██║█████╗░░
        ░░░██║░░░██║██║░░██╗  ░░░██║░░░██╔══██║██║░░██╗  ░░░██║░░░██║░░██║██╔══╝░░
        ░░░██║░░░██║╚█████╔╝  ░░░██║░░░██║░░██║╚█████╔╝  ░░░██║░░░╚█████╔╝███████╗
        ░░░╚═╝░░░╚═╝░╚════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░  ░░░╚═╝░░░░╚════╝░╚══════╝
        """)
    print("""        
        █▀▀ █▀█ █▀█ █▀▄   █░░ █░█ █▀▀ █▄▀ █
        █▄█ █▄█ █▄█ █▄▀   █▄▄ █▄█ █▄▄ █░█ ▄
        """)


def print_cell(board):
    blankBoard = """
          #################################
          #x1 o1 o1 o1 x1##x2 o2 o2 o2 x2##x3 o3 o3 o3 x3#
          # o1x1   x1o1 ## o2x2   x2o2 ## o3x3   x3o3 #
          #o1   1   o1##o2   2   o2##o3   3   o3#
          # o1x1   x1o1 ## o2x2   x2o2 ## o3x3   x3o3 #
          #x1 o1 o1 o1 x1##x2 o2 o2 o2 x2##x3 o3 o3 o3 x3#
          #################################
          #################################
          #x4 o4 o4 o4 x4##x5 o5 o5 o5 x5##x6 o6 o6 o6 x6#
          # o4x4   x4o4 ## o5x5   x5o5 ## o6x6   x6o6 #
          #o4   4   o4##o5   5   o5##o6   6   o6#
          # o4x4   x4o4 ## o5x5   x5o5 ## o6x6   x6o6 #
          #x4 o4 o4 o4 x4##x5 o5 o5 o5 x5##x6 o6 o6 o6 x6#
          #################################
          #################################
          #x7 o7 o7 o7 x7##x8 o8 o8 o8 x8##x9 o9 o9 o9 x9#
          # o7x7   x7o7 ## o8x8   x8o8 ## o9x9   x9o9 #
          #o7   7   o7##o8   8   o8##o9   9   o9#
          # o7x7   x7o7 ## o8x8   x8o8 ## o9x9   x9o9 #
          #x7 o7 o7 o7 x7##x8 o8 o8 o8 x8##x9 o9 o9 o9 x9#
          #################################
    """
    
    for i in range(1,10):
        if (board[i] == 'O'):
            blankBoard = blankBoard.replace('o' + str(i), board[i])
            blankBoard = blankBoard.replace('x' + str(i), ' ')
            blankBoard = blankBoard.replace(str(i), '#')
        else:
            if (board[i] == 'X'):
                blankBoard = blankBoard.replace('x' + str(i), board[i])
                blankBoard = blankBoard.replace('o' + str(i), ' ')
                blankBoard = blankBoard.replace(str(i), '#')
            else:
                blankBoard = blankBoard.replace('o' + str(i), ' ')
                blankBoard = blankBoard.replace('x' + str(i), ' ')
                
                
    print(blankBoard)

def check_move(cells, move):
        return cells[move] == move
    
    
def make_move(cells, turn):
    
    if (turn % 2) != 0:
        print("""    
            █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   ▄█   █▀▄▀█ █▀█ █░█ █▀▀ █
            █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   ░█   █░▀░█ █▄█ ▀▄▀ ██▄ ▄
            """)
        move = int(input())
        if check_move(cells, move):
            cells[move] = 'X'
            return turn + 1
        else :
            print("Invalid move")
    else :
        print("""
            █▀█ █░░ ▄▀█ █▄█ █▀▀ █▀█   ▀█   █▀▄▀█ █▀█ █░█ █▀▀ █
            █▀▀ █▄▄ █▀█ ░█░ ██▄ █▀▄   █▄   █░▀░█ █▄█ ▀▄▀ ██▄ ▄
            """)
        move = int(input())
        if check_move(cells, move):
            cells[move] = 'O'
            return turn + 1
        else :
            print("Invalid move")
    
    return turn     
    

def check_win(cells):
    if cells[1] == cells[2] == cells[3] == 'X' or cells[1] == cells[2] == cells[3] == 'O':
        return cells[1]
    if cells[4] == cells[5] == cells[6] == 'X' or cells[4] == cells[5] == cells[6] == 'O':
        return cells[4]
    if cells[7] == cells[8] == cells[9] == 'X' or cells[7] == cells[8] == cells[9] == 'O':
        return cells[7]
    if cells[1] == cells[4] == cells[7] == 'X' or cells[1] == cells[4] == cells[7] == 'O':
        return cells[1]
    if cells[2] == cells[5] == cells[8] == 'X' or cells[2] == cells[5] == cells[8] == 'O':
        return cells[2]
    if cells[3] == cells[6] == cells[9] == 'X' or cells[3] == cells[6] == cells[9] == 'O':
        return cells[3]
    if cells[1] == cells[5] == cells[9] == 'X' or cells[3] == cells[6] == cells[9] == 'O':
        return cells[1]
    if cells[3] == cells[5] == cells[7] == 'X' or cells[3] == cells[5] == cells[7] == 'O':
        return cells[3]
    
    return 0
    
            
def print_winner(winner):
    if winner == 'X':
        print("""           
            ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░  ░░███╗░░
            ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗  ░████║░░
            ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝  ██╔██║░░
            ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗  ╚═╝██║░░
            ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║  ███████╗
            ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝
            """)
    else :
        print("""
            ██████╗░██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░  ██████╗░
            ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██╔════╝██╔══██╗  ╚════██╗
            ██████╔╝██║░░░░░███████║░╚████╔╝░█████╗░░██████╔╝  ░░███╔═╝
            ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██╔══╝░░██╔══██╗  ██╔══╝░░
            ██║░░░░░███████╗██║░░██║░░░██║░░░███████╗██║░░██║  ███████╗
            ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ╚══════╝
            """)
        
    print("""      
                            ░██╗░░░░░░░██╗██╗███╗░░██╗██╗
                            ░██║░░██╗░░██║██║████╗░██║██║
                            ░╚██╗████╗██╔╝██║██╔██╗██║██║
                            ░░████╔═████║░██║██║╚████║╚═╝
                            ░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗
                            ░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝
            """)
    

def print_draw(winner):       
    print("""
        ██╗████████╗██╗░██████╗  ██████╗░██████╗░░█████╗░░██╗░░░░░░░██╗
        ██║╚══██╔══╝╚█║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗░██║░░██╗░░██║
        ██║░░░██║░░░░╚╝╚█████╗░  ██║░░██║██████╔╝███████║░╚██╗████╗██╔╝
        ██║░░░██║░░░░░░░╚═══██╗  ██║░░██║██╔══██╗██╔══██║░░████╔═████║░
        ██║░░░██║░░░░░░██████╔╝  ██████╔╝██║░░██║██║░░██║░░╚██╔╝░╚██╔╝░
        ╚═╝░░░╚═╝░░░░░░╚═════╝░  ╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░
            """)
        
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    cells = [1,1,2,3,4,5,6,7,8,9]
    turn = 1
    winner = 0
    __location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    win = os.path.join(__location__, 'win.mp3')
    draw = os.path.join(__location__, 'game_over.wav')
    
    print_intro()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(win)
    while turn < 10 and winner == 0:    
        print_cell(cells)
        turn = make_move(cells, turn)
        os.system('cls' if os.name == 'nt' else 'clear')
        winner = check_win(cells)
    
    if turn == 10:
        print_draw(winner)
        playsound(draw)
    else: 
        print_winner(winner)
        playsound(win)
                

main()