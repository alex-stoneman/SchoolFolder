# Skeleton Program for the AQA AS1 Summer 2016 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 programming environment

# Version Number 1.0

import random

def MakePlayerTorpedoMove(Board, Ships, Row, Column):
    while Row > -1:
        if Board[Row][Column] in ["A", "B", "S", "D", "P"]:
            print("Hit at (" + str(Column) + "," + str(Row) + ").")
            CheckSunk(Board, Ships, Row, Column)
            Board[Row][Column] = "h"
            Row = -1
        elif Board[Row][Column] == "h":
            print("There was already a hit at (" + str(Column) + "," + str(Row) + ").")
            Row = -1
        else:
            print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
            Board[Row][Column] = "m"
            Row -= 1



def CheckSunk(Board, Ships, Row, Column):
    for Ship in Ships:
        if Board[Row][Column] == Ship[0][0]:
            Ship[1] -= 1
            if Ship[1] == 0:
                print(f"{Ship[0]} sunk")

def GetRowColumn():
    while True:
        print()
        Column = int(input("Please enter column: "))
        Row = int(input("Please enter row: "))
        if -1 < Row < 10:
            print()
            return Row, Column
        else:
            print("Invalid Value entered")


def MakePlayerMove(Board, Ships, Torpedo):
    Row, Column = GetRowColumn()
    if Torpedo and input("D you want yo fire a Torpedo (y/n)") == "y":
        MakePlayerTorpedoMove(Board, Ships, Row, Column)
        return False
    else:
        if Board[Row][Column] == "m" or Board[Row][Column] == "h":
            print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
        elif Board[Row][Column] == "-":
            print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
            Board[Row][Column] = "m"
        else:
            print("Hit at (" + str(Column) + "," + str(Row) + ").")
            CheckSunk(Board,Ships,Row,Column)
            Board[Row][Column] = "h"
        return Torpedo



def SetUpBoard():
    Board = []
    for Row in range(10):
        BoardRow = []
        for Column in range(10):
            BoardRow.append("-")
        Board.append(BoardRow)
    return Board


def LoadGame(Filename, Board):
    BoardFile = open(Filename, "r")
    for Row in range(10):
        Line = BoardFile.readline()
        for Column in range(10):
            Board[Row][Column] = Line[Column]
    BoardFile.close()


def PlaceRandomShips(Board, Ships):
    for Ship in Ships:
        Valid = False
        while not Valid:
            Row = random.randint(0, 9)
            Column = random.randint(0, 9)
            HorV = random.randint(0, 1)
            if HorV == 0:
                Orientation = "v"
            else:
                Orientation = "h"
            Valid = ValidateBoatPosition(Board, Ship, Row, Column, Orientation)
        print("Computer placing the " + Ship[0])
        PlaceShip(Board, Ship, Row, Column, Orientation)


def PlaceShip(Board, Ship, Row, Column, Orientation):
    if Orientation == "v":
        for Scan in range(Ship[1]):
            Board[Row + Scan][Column] = Ship[0][0]
    elif Orientation == "h":
        for Scan in range(Ship[1]):
            Board[Row][Column + Scan] = Ship[0][0]


def ValidateBoatPosition(Board, Ship, Row, Column, Orientation):
    if Orientation == "v" and Row + Ship[1] > 10:
        return False
    elif Orientation == "h" and Column + Ship[1] > 10:
        return False
    else:
        if Orientation == "v":
            for Scan in range(Ship[1]):
                if Board[Row + Scan][Column] != "-":
                    return False
        elif Orientation == "h":
            for Scan in range(Ship[1]):
                if Board[Row][Column + Scan] != "-":
                    return False
    return True


def CheckWin(Board):
    for Row in range(10):
        for Column in range(10):
            if Board[Row][Column] in ["A", "B", "S", "D", "P"]:
                return False
    return True


def PrintBoard(Board):
    print()
    print("The board looks like this: ")
    print()
    print(" ", end="")
    for Column in range(10):
        print(" " + str(Column) + "  ", end="")
    print()
    for Row in range(10):
        print(str(Row) + " ", end="")
        for Column in range(10):
            if Board[Row][Column] == "-":
                print(" ", end="")
            elif Board[Row][Column] in ["A", "B", "S", "D", "P"]:
                print(" ", end="")
            else:
                print(Board[Row][Column], end="")
            if Column != 9:
                print(" | ", end="")
        print()


def DisplayMenu():
    print("MAIN MENU")
    print()
    print("1. Start new game")
    print("2. Load training game")
    print("9. Quit")
    print()


def GetMainMenuChoice():
    print("Please enter your choice: ", end="")
    Choice = int(input())
    print()
    return Choice


def PlayGame(Board, Ships):
    GameWon = False
    Torpedo = True
    while not GameWon:
        PrintBoard(Board)
        Torpedo = MakePlayerMove(Board, Ships, Torpedo)
        GameWon = CheckWin(Board)
        if GameWon:
            print("All ships sunk!")
            print()


if __name__ == "__main__":
    TRAININGGAME = "Training.txt"
    MenuOption = 0
    while not MenuOption == 9:
        Board = SetUpBoard()
        Ships = [["Aircraft Carrier", 5,"A"], ["Battleship", 4,"B"], ["Submarine", 3,"S"], ["Destroyer", 3,"D"], ["Patrol Boat", 2,"P"]]

        DisplayMenu()
        MenuOption = GetMainMenuChoice()
        if MenuOption == 1:
            PlaceRandomShips(Board, Ships)
            PlayGame(Board, Ships)
        if MenuOption == 2:
            LoadGame(TRAININGGAME, Board)
            PlayGame(Board, Ships)
