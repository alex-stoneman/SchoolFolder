# Skeleton Program for the AQA AS1 Summer 2016 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA AS1 Programmer Team
# developed in a Python 3 programming environment

# Version Number 1.0

import random

def GetRowColumn():
    while True:
        try:
            print()
            Column = int(input("Please enter column: "))
            Row = int(input("Please enter row: "))
            print()
            if 10 > Column > -1 and 10 > Row > -1:
                return Row, Column
            else:
                print("That is outside of the  area")
        except ValueError:
            print("Please enter an integer value\n")


def RadarScan(Board, Row, Column):
    if Board[Row+1][Column] in ["A", "B", "S", "D", "P", "F"] or Board[Row-1][Column] in ["A", "B", "S", "D", "P", "F"]:
        return True
    elif Board[Row][Column+1] in ["A", "B", "S", "D", "P", "F"] or Board[Row][Column-1] in ["A", "B", "S", "D", "P", "F"]:
        return True
    else:
        return False


def MakePlayerMove(Board, Ships):
    Row, Column = GetRowColumn()
    if Board[Row][Column] == "m" or Board[Row][Column] == "h":
        print("Sorry, you have already shot at the square (" + str(Column) + "," + str(Row) + "). Please try again.")
        return False
    elif Board[Row][Column] == "-":
        print("Sorry, (" + str(Column) + "," + str(Row) + ") is a miss.")
        Board[Row][Column] = "m"
    else:
        print(f"Hit at ({str(Column)},{str(Row)}).")
        Board[Row][Column] = "h"

    if RadarScan(Board, Row, Column):
        print("Enemy Near!")
    else:
        print("All quiet")
    return True


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


def playerPlaceShips(Board, Ships):
    for Ship in Ships:
        Valid = False
        while not Valid:
            orientation = ""
            while orientation != "h" or "v":
                orientation = (input("Enter h for a horizontal boat\nEnter v for a vertical boat\n: "))
            Row, Column = GetRowColumn()
            Valid = ValidateBoatPosition(Board, Ship, Row, Column, orientation)


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
            if Board[Row][Column] in ["A", "B", "S", "D", "P", "F"]:
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
            elif Board[Row][Column] in ["A", "B", "S", "D", "P", "F"]:
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
    print("3. Load saved game")
    print("4. Board Test")
    print("9. Quit")
    print()


def GetMainMenuChoice():
    while True:
        try:
            print("Please enter your choice: ", end="")
            Choice = int(input())
            print()
            return Choice
        except ValueError:
            print("Please enter an integer\n")


def PlayGame(Board, Ships):
    GameWon = False
    GameLost = False
    ammo = 20
    while not GameWon and not GameLost:
        PrintBoard(Board)
        print(f"You have {ammo} torpedoes remaining\n")
        if MakePlayerMove(Board, Ships):
            ammo -= 1
        if ammo == 0:
            GameLost = True
        GameWon = CheckWin(Board)

        if GameWon:
            print("All ships sunk!")
            print()
        elif GameLost:
            print("GAME OVER\n You ran out of ammo")
        else:
            if input("Do you want to save the game (Y/N)? ").upper() == "Y":
                newFilename = input("Enter a filename: ")
                SaveGame(Board, newFilename)
                break


def SaveGame(Board, filename):
    f = open(f"{filename}.txt", "w")
    for line in Board:
        chars = ""
        for char in line:
            chars += char
        f.writelines(f"{chars}\n")


def BoardTest(Board, Ships):
    PlaceRandomShips(Board, Ships)
    print("\nThe board looks like this: \n\n ", end = "")
    for Column in range(10):
        print(f" {str(Column)}  ", end="")
    print()
    for Row in range(10):
        print(f"{str(Row)} ", end="")
        for Column in range(10):
            if Board[Row][Column] == "-":
                print(" ", end="")
            else:
                print(Board[Row][Column], end="")
            if Column != 9:
                print(" | ", end="")
        print()
    print()


if __name__ == "__main__":
    TRAININGGAME = "Training.txt"
    MenuOption = 0
    while not MenuOption == 9:
        Board = SetUpBoard()
        Ships = [["Aircraft Carrier", 5], ["Battleship", 4], ["Submarine", 3], ["Destroyer", 3], ["Patrol Boat", 2],["Frigate", 3]]
        DisplayMenu()
        MenuOption = GetMainMenuChoice()
        if MenuOption == 1:
            PlaceRandomShips(Board, Ships)
            PlayGame(Board, Ships)
        if MenuOption == 2:
            LoadGame(TRAININGGAME, Board)
            PlayGame(Board, Ships)
        if MenuOption == 3:
            filename = input("What is the filename: ")
            LoadGame(f"{filename}.txt", Board)
            PlayGame(Board, Ships)
        if MenuOption == 4:
            BoardTest(Board, Ships)
        if MenuOption ==9:
            check = input("Are you sure? ")
            if check.upper() != "Y":
                MenuOption = 0

