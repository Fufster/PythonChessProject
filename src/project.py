class Piece:
    def __init__(self, color, rank):
        self.color = color
        self.rank = rank
    
    def getIcon(self):
        if self.color == 'W':
            match self.rank:
                case 'Pawn':
                    return '♟'
                case 'Bishop':
                    return '♝'
                case 'Knight':
                    return '♞'
                case 'Rook':
                    return '♜'
                case 'Queen':
                    return '♛'
                case 'King':
                    return '♚'
        elif self.color == 'B':
            match self.rank:
                case 'Pawn':
                    return '♙'
                case 'Bishop':
                    return '♗'
                case 'Knight':
                    return '♘'
                case 'Rook':
                    return '♖'
                case 'Queen':
                    return '♕'
                case 'King':
                    return '♔'
            
def createBoard():
    Board = [[0 for x in range(8)] for y in range(8)]
    Pieces = [[0 for x in range(8)] for y in range(8)]
    #board
    for x in range(8):
        for y in range(8):
            if (x - (y%2))%2 == 0:
                Board[x][y] = '⬜'
            else:
                Board[x][y] = '⬛'
    #pawns
    for y in range(8):
        Pieces[1][y] = Piece('B', 'Pawn')
    for y in range(8):
        Pieces[6][y] = Piece('W', 'Pawn')
    #rooks
    Pieces[0][0] = Piece('B', 'Rook')
    Pieces[7][0] = Piece('W', 'Rook')
    Pieces[0][7] = Piece('B', 'Rook')
    Pieces[7][7] = Piece('W', 'Rook')
    #knights
    Pieces[0][1] = Piece('B', 'Knight')
    Pieces[0][6] = Piece('B', 'Knight')
    Pieces[7][1] = Piece('W', 'Knight')
    Pieces[7][6] = Piece('W', 'Knight')
    #bishops
    Pieces[0][2] = Piece('B', 'Bishop')
    Pieces[0][5] = Piece('B', 'Bishop')
    Pieces[7][2] = Piece('W', 'Bishop')
    Pieces[7][5] = Piece('W', 'Bishop')
    #kings and queens
    Pieces[0][3] = Piece('B', 'Queen')
    Pieces[0][4] = Piece('B', 'King')
    Pieces[7][3] = Piece('W', 'Queen')
    Pieces[7][4] = Piece('W', 'King')

    return Board, Pieces

def inputConvert(input):
    match input[0].upper():
        case 'A':
            x = 0
        case 'B':
            x = 1
        case 'C':
            x = 2
        case 'D':
            x = 3
        case 'E':
            x = 4
        case 'F':
            x = 5
        case 'G':
            x = 6
        case 'H':
            x = 7
    
    match input[1].upper():
        case '1':
            y = 7
        case '2':
            y = 6
        case '3':
            y = 5
        case '4':
            y = 4
        case '5':
            y = 3
        case '6':
            y = 2
        case '7':
            y = 1
        case '8':
            y = 0
    
    return y, x
        



def printBoard(Board, Pieces):
    
    for x in range(8):
        for y in range(8):
            if Pieces[x][y] != 0:
                print(Pieces[x][y].getIcon().center(2), end="")
            else:
                print(Board[x][y], end="")
        print()

def main():
    Board, Pieces = createBoard()
    printBoard(Board, Pieces)
    testMove = input()
    print(inputConvert(testMove))


if __name__ == "__main__":
    main()