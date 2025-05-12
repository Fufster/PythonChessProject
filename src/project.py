import sys

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
    
    def getMoves(self, location, Pieces):
        moves = []
        match self.rank:
                
            case 'Pawn':
                if self.color == 'W':
                    if location[0]-1 >= 0:
                        if Pieces[location[0]-1][location[1]].color == 'E':
                            moves.append((location[0]-1, location[1]))
                            if location[0] == 6 and Pieces[4][location[1]].color == 'E':
                                moves.append((location[0]-2, location[1]))
                        if location[1]-1 >= 0:
                            if Pieces[location[0]-1][location[1]-1].color == 'B':
                                moves.append((location[0]-1, location[1]-1))
                        if location[1]+1 <= 7:
                            if Pieces[location[0]-1][location[1]+1].color == 'B':
                                moves.append((location[0]-1, location[1]+1))
                if self.color == 'B':
                    if location[0]+1 <= 7:
                        if Pieces[location[0]+1][location[1]].color == 'E':
                            moves.append((location[0]+1, location[1]))
                            if location[0] == 1 and Pieces[3][location[1]].color == 'E':
                                moves.append((location[0]+2, location[1]))
                        if location[1]-1 >= 0:
                            if Pieces[location[0]+1][location[1]-1].color == 'W':
                                moves.append((location[0]+1, location[1]-1))
                        if location[1]+1 <= 7:
                            if Pieces[location[0]+1][location[1]+1].color == 'W':
                                moves.append((location[0]+1, location[1]+1))
                for i in range(len(moves)):
                    moves[i] = movesConvert(moves[i])
                if len(moves) > 0:
                    return moves
                else:
                    for i in range(len(moves)):
                        moves[i] = movesConvert(moves[i])
                    if len(moves) > 0:
                        return moves
            
            case 'Bishop':
                ix = 1
                iy = 1
                #down-right
                while ix < (8 - location[1]) and iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]+ix].color == 'E':
                        moves.append((location[0]+iy, location[1]+ix))
                    else: 
                        if Pieces[location[0]+iy][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]+ix].color != self.color:
                            moves.append((location[0]+iy, location[1]+ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #up-right
                while ix < (8 - location[1]) and iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]+ix].color == 'E':
                        moves.append((location[0]-iy, location[1]+ix))
                    else: 
                        if Pieces[location[0]-iy][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]+ix].color != self.color:
                            moves.append((location[0]-iy, location[1]+ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #down-left
                while ix <= location[1] and iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]-ix].color == 'E':
                        moves.append((location[0]+iy, location[1]-ix))
                    else: 
                        if Pieces[location[0]+iy][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]-ix].color != self.color:
                            moves.append((location[0]+iy, location[1]-ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #up-left
                while ix <= location[1] and iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]-ix].color == 'E':
                        moves.append((location[0]-iy, location[1]-ix))
                    else: 
                        if Pieces[location[0]-iy][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]-ix].color != self.color:
                            moves.append((location[0]-iy, location[1]-ix))
                            break
                    ix = ix + 1
                    iy = iy + 1

                for i in range(len(moves)):
                    moves[i] = movesConvert(moves[i])
                if len(moves) > 0:
                    return moves
            
            case 'Knight':
                if location[0]-2 >= 0 and location[1]-1 >= 0:
                    if Pieces[location[0]-2][location[1]-1].color != self.color:
                        moves.append((location[0]-2, location[1]-1))
                if location[0]-2 >= 0 and location[1]+1 <= 7:
                    if Pieces[location[0]-2][location[1]+1].color != self.color:
                        moves.append((location[0]-2, location[1]+1))
                if location[0]+2 <= 7 and location[1]-1 >= 0:
                    if Pieces[location[0]+2][location[1]-1].color != self.color:
                        moves.append((location[0]+2, location[1]-1))
                if location[0]+2 <= 7 and location[1]+1 <= 7:
                    if Pieces[location[0]+2][location[1]+1].color != self.color:
                        moves.append((location[0]+2, location[1]+1))
                if location[0]+1 <= 7 and location[1]+2 <= 7:
                    if Pieces[location[0]+1][location[1]+2].color != self.color:
                        moves.append((location[0]+1, location[1]+2))
                if location[0]-1 >= 0 and location[1]+2 <= 7:
                    if Pieces[location[0]-1][location[1]+2].color != self.color:
                        moves.append((location[0]-1, location[1]+2))
                if location[0]+1 <= 7 and location[1]-2 >= 0:
                    if Pieces[location[0]+1][location[1]-2].color != self.color:
                        moves.append((location[0]+1, location[1]-2))
                if location[0]-1 >= 0 and location[1]-2 >= 0:
                    if Pieces[location[0]-1][location[1]-2].color != self.color:
                        moves.append((location[0]-1, location[1]-2))
                for i in range(len(moves)):
                    moves[i] = movesConvert(moves[i])
                if len(moves) > 0:
                    return moves
            
            case 'Rook':
                ix = 1
                iy = 1
                #right
                while ix < (8 - location[1]):
                    if Pieces[location[0]][location[1]+ix].color == 'E':
                        moves.append((location[0], location[1]+ix))
                    else: 
                        if Pieces[location[0]][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]][location[1]+ix].color != self.color:
                            moves.append((location[0], location[1]+ix))
                            break
                    ix = ix + 1
                #down
                while iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]].color == 'E':
                        moves.append((location[0]+iy, location[1]))
                    else: 
                        if Pieces[location[0]+iy][location[1]].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]].color != self.color:
                            moves.append((location[0]+iy, location[1]))
                            break
                    iy = iy + 1
                ix = 1
                iy = 1
                #left
                while ix <= location[1]:
                    if Pieces[location[0]][location[1]-ix].color == 'E':
                        moves.append((location[0], location[1]-ix))
                    else: 
                        if Pieces[location[0]][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]][location[1]-ix].color != self.color:
                            moves.append((location[0], location[1]-ix))
                            break
                    ix = ix + 1
                #up
                while iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]].color == 'E':
                        moves.append((location[0]-iy, location[1]))
                    else: 
                        if Pieces[location[0]-iy][location[1]].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]].color != self.color:
                            moves.append((location[0]-iy, location[1]))
                            break
                    iy = iy + 1

                for i in range(len(moves)):
                    moves[i] = movesConvert(moves[i])
                if len(moves) > 0:
                    return moves
                
            case 'Queen':
                ix = 1
                iy = 1
                #right
                while ix < (8 - location[1]):
                    if Pieces[location[0]][location[1]+ix].color == 'E':
                        moves.append((location[0], location[1]+ix))
                    else: 
                        if Pieces[location[0]][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]][location[1]+ix].color != self.color:
                            moves.append((location[0], location[1]+ix))
                            break
                    ix = ix + 1
                #down
                while iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]].color == 'E':
                        moves.append((location[0]+iy, location[1]))
                    else: 
                        if Pieces[location[0]+iy][location[1]].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]].color != self.color:
                            moves.append((location[0]+iy, location[1]))
                            break
                    iy = iy + 1
                ix = 1
                iy = 1
                #left
                while ix <= location[1]:
                    if Pieces[location[0]][location[1]-ix].color == 'E':
                        moves.append((location[0], location[1]-ix))
                    else: 
                        if Pieces[location[0]][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]][location[1]-ix].color != self.color:
                            moves.append((location[0], location[1]-ix))
                            break
                    ix = ix + 1
                #up
                while iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]].color == 'E':
                        moves.append((location[0]-iy, location[1]))
                    else: 
                        if Pieces[location[0]-iy][location[1]].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]].color != self.color:
                            moves.append((location[0]-iy, location[1]))
                            break
                    iy = iy + 1
                ix = 1
                iy = 1
                #down-right
                while ix < (8 - location[1]) and iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]+ix].color == 'E':
                        moves.append((location[0]+iy, location[1]+ix))
                    else: 
                        if Pieces[location[0]+iy][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]+ix].color != self.color:
                            moves.append((location[0]+iy, location[1]+ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #up-right
                while ix < (8 - location[1]) and iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]+ix].color == 'E':
                        moves.append((location[0]-iy, location[1]+ix))
                    else: 
                        if Pieces[location[0]-iy][location[1]+ix].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]+ix].color != self.color:
                            moves.append((location[0]-iy, location[1]+ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #down-left
                while ix <= location[1] and iy < (8 - location[0]):
                    if Pieces[location[0]+iy][location[1]-ix].color == 'E':
                        moves.append((location[0]+iy, location[1]-ix))
                    else: 
                        if Pieces[location[0]+iy][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]+iy][location[1]-ix].color != self.color:
                            moves.append((location[0]+iy, location[1]-ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                ix = 1
                iy = 1
                #up-left
                while ix <= location[1] and iy <= location[0]:
                    if Pieces[location[0]-iy][location[1]-ix].color == 'E':
                        moves.append((location[0]-iy, location[1]-ix))
                    else: 
                        if Pieces[location[0]-iy][location[1]-ix].color == self.color:
                            break
                        if Pieces[location[0]-iy][location[1]-ix].color != self.color:
                            moves.append((location[0]-iy, location[1]-ix))
                            break
                    ix = ix + 1
                    iy = iy + 1
                
                for i in range(len(moves)):
                    moves[i] = movesConvert(moves[i])
                if len(moves) > 0:
                    return moves
                
            case 'King':
                    if location[0]-1 >= 0:
                        if Pieces[location[0]-1][location[1]].color != self.color:
                            moves.append((location[0]-1, location[1]))
                        if location[1]-1 >= 0:
                            if Pieces[location[0]-1][location[1]-1].color != self.color:
                                moves.append((location[0]-1, location[1]-1))
                        if location[1]+1 <= 7:
                            if Pieces[location[0]-1][location[1]+1].color != self.color:
                                moves.append((location[0]-1, location[1]+1))
                    if location[0]+1 <= 7:
                        if Pieces[location[0]+1][location[1]].color != self.color:
                            moves.append((location[0]+1, location[1]))
                        if location[1]-1 >= 0:
                            if Pieces[location[0]+1][location[1]-1].color != self.color:
                                moves.append((location[0]+1, location[1]-1))
                        if location[1]+1 <= 7:
                            if Pieces[location[0]+1][location[1]+1].color != self.color:
                                moves.append((location[0]+1, location[1]+1))
                    if location[1]-1 >= 0:
                        if Pieces[location[0]][location[1]-1].color != self.color:
                            moves.append((location[0], location[1]-1))
                    if location[1]+1 <= 7:
                        if Pieces[location[0]][location[1]+1].color != self.color:
                            moves.append((location[0], location[1]+1))
                    
                    for i in range(len(moves)):
                        moves[i] = movesConvert(moves[i])
                    if len(moves) > 0:
                        return moves
                    
def createBoard():
    Board = [[0 for x in range(8)] for y in range(8)]
    Pieces = [[Piece('E', 'Empty') for x in range(8)] for y in range(8)]
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

def movesConvert(move):
    match move[1]:
        case 0:
            x = 'A'
        case 1:
            x = 'B'
        case 2:
            x = 'C'
        case 3:
            x = 'D'
        case 4:
            x = 'E'
        case 5:
            x = 'F'
        case 6:
            x = 'G'
        case 7:
            x = 'H'
    
    match move[0]:
        case 0:
            y = 8
        case 1:
            y = 7
        case 2:
            y = 6
        case 3:
            y = 5
        case 4:
            y = 4
        case 5:
            y = 3
        case 6:
            y = 2
        case 7:
            y = 1
    return f"{x}{y}"

def printBoard(Board, Pieces):
    
    for x in range(8):
        for y in range(8):
            if Pieces[x][y].rank != 'Empty':
                print(Pieces[x][y].getIcon().center(2), end="")
            else:
                print(Board[x][y], end="")
        print()

def move(Board, Pieces, currentLocation, moveLocation):
    end = False
    if Pieces[moveLocation[0]][moveLocation[1]].rank == 'King':
        match Pieces[currentLocation[0]][currentLocation[1]].color:
            case 'W':
                winner = 'White'
            case 'B':
                winner = 'Black'
        end = True   

    if Pieces[moveLocation[0]][moveLocation[1]].color != 'E':
        Pieces[moveLocation[0]][moveLocation[1]] = Piece('E', 'Empty')
    Pieces[moveLocation[0]][moveLocation[1]], Pieces[currentLocation[0]][currentLocation[1]] = Pieces[currentLocation[0]][currentLocation[1]], Pieces[moveLocation[0]][moveLocation[1]]

    if Pieces[moveLocation[0]][moveLocation[1]].rank == 'Pawn' and moveLocation[0] == 7:
        Pieces[moveLocation[0]][moveLocation[1]].rank = 'Queen'
    if Pieces[moveLocation[0]][moveLocation[1]].rank == 'Pawn' and moveLocation[0] == 0:
        Pieces[moveLocation[0]][moveLocation[1]].rank = 'Queen'

    if end == True:
        printBoard(Board, Pieces)
        print(f"{winner} Wins!")
        sys.exit()

def main():
    Board, Pieces = createBoard()
    while True:
        printBoard(Board, Pieces)
        currentPiece = input("Please enter a space: ")
        while True:
            if currentPiece == 'q' or currentPiece == 'Q':
                    break
            try:
                currentLocation = inputConvert(currentPiece)
            except:
                print("That space does not exist, please enter a new one: ")
                currentPiece = input()
            else:
                currentPiece = Pieces[currentLocation[0]][currentLocation[1]]
                if currentPiece.color == 'E':
                    print("That space is empty, please enter a new one: ")
                    currentPiece = input()
                else:
                    break
        if currentPiece == 'q' or currentPiece == 'Q':
            break

        print(currentPiece.rank)
        print(f"Possible Moves: {currentPiece.getMoves(currentLocation, Pieces)}")
        try:
            for item in currentPiece.getMoves(currentLocation, Pieces):
                break
        except:
            print("This piece cannot move.")
            continue
        currentMove = input("Enter a space to move to, or type 'back' to select a different space: ")
        if currentMove == 'back':
            continue
        while True:
            match = False
            try:
                moveLocation = inputConvert(currentMove)
            except:
                print("That space does not exist, please enter a new one: ")
                currentMove = input()
            else:
                for item in currentPiece.getMoves(currentLocation, Pieces):
                    if currentMove.upper() == item:
                        match = True
                if match == True:
                    break
                print("That is not in the list of valid moves, please enter a new one: ")
                currentMove = input()
        
        move(Board, Pieces, currentLocation, moveLocation)

if __name__ == "__main__":
    main()