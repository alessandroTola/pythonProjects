

def print_cell(board):
    blankBoard = """"
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
            blankBoard = blankBoard.replace(str(i), ' ')
        else:
            if (board[i] == 'X'):
                blankBoard = blankBoard.replace('x' + str(i), board[i])
                blankBoard = blankBoard.replace('o' + str(i), ' ')
                blankBoard = blankBoard.replace(str(i), 'x')
            else:
                blankBoard = blankBoard.replace('o' + str(i), ' ')
                blankBoard = blankBoard.replace('x' + str(i), ' ')
                #blankBoard = blankBoard.replace(str(i), ' ')
                
                
    print(blankBoard)


def main():
    cells = [1,'O',2,'X',4,'O','O',7,8,'X']
    print_cell(cells)
    

main()