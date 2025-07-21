import random

"""
This function creates the minesweeper board, using lists within a list to create rows and columns
"""
def createBoard(gridSize, _type) -> list:
    emptyBoard = []
    
    for i in range(gridSize):
        newRow = []
        if _type == "system":
            for i in range(gridSize):
                newRow.append("0")
            emptyBoard.append(newRow)
        elif _type == "player":
            for i in range(gridSize):
                newRow.append("_")
            emptyBoard.append(newRow)
        
    return emptyBoard
"""
This function prints out the minesweeper board
"""
def printBoard(board):
    y = gridSize
    x = 1
    
    tempString = ""
    print("Y\n")
    for row in board:
        if y < 10:
            print(f"{y}. {row}")
        else:
            print(f"{y}.{row}")
        y -= 1
        tempString += f"{x}.  "
        if x < 10:
            tempString += " "
        x += 1
        
    
    print("     " + tempString + "  X")
"""
This function creates a menu with three options, Play, Credit, quit, Created by my teammate
"""
def displayTitleScreen():
    print("\n" + "=" * 30)
    print("      🚀  Welcome to  ")
    print("     _____  .__                _________                                          ")
    print("    /     \ |__| ____   ____  /   _____/_  _  __ ____   ____ ______   ___________ ")
    print("   /  \ /  \|  |/    \_/ __ \ \_____  \\ \/ \/ // __ \_/ __ \\____ \_/ __ \_  __ \"")
    print("  /    Y    \  |   |  \  ___/ /        \\     /\  ___/\  ___/|  |_> >  ___/|  | \/")
    print("  \____|__  /__|___|  /\___  >_______  / \/\_/  \___  >\___  >   __/ \___  >__|   ")
    print("          \/        \/     \/        \/             \/     \/|__|        \/       ")
    print("\n" + "=" * 30)
    print("\n🎮  Select an Option:")
    print("  [1] Play!")
    print("  [2] Credits")
    print("  [3] Quit\n")
    
"""
This asks the user for the choice of play, credits, or quit, labeled as 1, 2, and 3 
"""
def menu():
    while True:
        displayTitleScreen()
        choice = input("👉  Enter your choice: ")
        if choice == "1":
            return determineGridSize()
        elif choice == "2":
            print("\n🌟  All Credit to _, _, and _ 🌟\n")
            input("Press Enter to return to menu...")
        elif choice == "3":
            print("\n👋 Thanks for playing! Goodbye!\n")
            exit()
        else:
            print("\n❌ Invalid choice. Please enter 1, 2, or 3.")
        
"""
This function asks the user for the board size with three options: small, medium, and large labeled as 1, 2, and 3 Created by my teammate

"""
def determineGridSize():
    while True:
        print("")
        print("🌍  Choose Your Board Size:")
        print("  [1] Small (5x5)")
        print("  [2] Medium (10x10)")
        print("  [3] Large (20x20)")
        print("")
        
        size = input("👉  Enter your choice: ")
        if size == "1":
            return 5
        elif size == "2":
            return 10
        elif size == "3":
            return 20
        else:
            print("")
            print("❌ Invalid response. Try again.")
"""
Converts the coordinates so it is easier to associate with lists
"""

def findCoord(x,y):
    if gridSize == 5:
        y = abs(y-6) -1
    elif gridSize == 10:
        y = abs(y-11) -1
    elif gridSize == 20:
        y = abs(y-21)- 1
    x = x-1
    return y, x
    
    
"""
Determines the amount of mines
"""
def determineMineAmount(grid_size):
    if grid_size == 5:
        return 5
    elif grid_size == 10:
        return 21
    elif grid_size == 20:
        return 31

"""            
Checks if there is a duplicate mine in the mine list
"""
def checkIfDuplicateMine(listOfMineLocations, newCoordinate):
    for mineLocation in listOfMineLocations:
        if mineLocation == newCoordinate:
            return False
    return True            
            
"""
This function gives a specific amount of mines depending on the grid size
"""
def determineMineLocations(grid_size):
    amountOfMines = determineMineAmount(grid_size)
    listOfMineLocations = []
    listLength = len(listOfMineLocations)
    for i in range(amountOfMines):
        while True:
            x = random.randint(0,grid_size - 1)
            y = random.randint(0,grid_size - 1)
            newCoordinate = (x, y)
            
            if checkIfDuplicateMine(listOfMineLocations, newCoordinate):
                listOfMineLocations.append(newCoordinate)
                listLength = len(listOfMineLocations)
                break
    placeMines(listOfMineLocations)

"""
This function places mines across the board randomly
"""
def placeMines(listOfMineLocations):
    for mineLocation in listOfMineLocations:
        systemBoard[mineLocation[0]][mineLocation[1]] = "x"
"""
Checks the top row of the spot for bombs
"""
def checkTopRowAroundDesiredSpot(xIndex, yIndex, loopIndex, valueToBeChecked):
    try:
        if systemBoard[yIndex-1][xIndex+loopIndex] == valueToBeChecked and yIndex-1 != -1 and xIndex+loopIndex != -1:
                return 1
    except:
        pass
    return 0
"""
Checks the bottom row of the spot for bombs
"""
def checkBottomRowAroundDesiredSpot(xIndex, yIndex, loopIndex, valueToBeChecked):
    try:
        if systemBoard[yIndex+1][xIndex+loopIndex] == valueToBeChecked  and yIndex+1 != -1 and xIndex+loopIndex != -1:
                return 1
    except:
        pass
    return 0
"""
Checks the left and right of the spot for bombs
"""
def checkLeftAndRightAroundDesiredSpot(xIndex, yIndex, valueToBeChecked):
    total = 0
    try:
        if systemBoard[yIndex][xIndex-1] == valueToBeChecked and xIndex-1 != -1:
                total += 1
    except:
        pass
    
    #Checks the slot right of desired space
    try:
        if systemBoard[yIndex][xIndex+1] == valueToBeChecked and xIndex+1 != -1:
                total += 1
    except:
        pass
    return total

"""
Checks for the mines for all 8 slots around a single slot
"""
def tryIndexesAroundDesiredSpace(xIndex, yIndex):
    mineCounter = 0
    
    for i in range(-1,2):
        mineCounter += checkTopRowAroundDesiredSpot(xIndex, yIndex, i, "x") + checkBottomRowAroundDesiredSpot(xIndex, yIndex, i, "x")
    mineCounter += checkLeftAndRightAroundDesiredSpot(xIndex, yIndex, "x")
    
    return mineCounter

"""
Places all of the numbers on the board surrounding the mines
"""
def placeNumbers():
    for yIndex, currentList in enumerate(systemBoard):
        for xIndex, __ in enumerate(currentList):
            if systemBoard[yIndex][xIndex] == "0":
                systemBoard[yIndex][xIndex] = str(tryIndexesAroundDesiredSpace(xIndex, yIndex))

"""
Places a flag where the player chooses
"""
def placeFlag(x,y):
    global flagsamt
    systemBoardValue = systemBoard[x][y]
    if playerBoard[x][y] != "f":
        playerBoard[x][y] = "f"
    else:
        playerBoard[x][y] = "_"
        flagsamt += 1

"""
Reveals the spot that the player chooses on the board
"""
def revealSpot(x,y):
    systemBoardValue = systemBoard[x][y]
    playerBoard[x][y] = systemBoardValue
    if systemBoardValue != "x":
        return "nothing"
    else:
        print()
        print("---------------------------------------------------------------------")
        print("YOU LOSE")
        return "lost"
"""
Checks for a win and returns a boolean value
"""
def checkForWin():
    x = 0
    for i, currentList in enumerate(playerBoard):
        for j, __ in enumerate(currentList):
            currentSpot = playerBoard[i][j]
            if currentSpot == "_":
                x += 1
    
    if x > 0:
        return False
    else:
        return True
        

#This sets the menu equal to the grid size after asking for the grid size
gridSize = menu()

#This creates the player and system boards
systemBoard = createBoard(gridSize, "system")
playerBoard = createBoard(gridSize, "player")

determineMineLocations(gridSize)
print()
print()
placeNumbers()
print()

print()

print("\n\n\n\n" )

printBoard(systemBoard)

print("\n\n\n\n" )

printBoard(playerBoard)

#Lists the amount of flags available and allows you to choose whether you want to reveal or flag a square
print()
flagsamt = determineMineAmount(gridSize)
print("🚩 You have ", flagsamt, " Flags 🚩 ")
print("")

"""
This is the loop where the game is contained in
"""
while True:
    lost = False
    print("[1] Reveal 🔎  ")
    print("[2] Flag 🚩  ")
    print(" ")
    ask = input("👉  Enter Choice: ")
    print()
    print("Write your coordinates! (x,y)")
    x_pos = int(input("\nX coordinate❓  : " ))
    
    y_pos = int(input("\nY coordinate❓  : "))
    
    x,y = findCoord(x_pos,y_pos)
    
   
    if ask == "2":
        if flagsamt > 0:
            placeFlag(x,y)
            flagsamt -= 1
            print("\n🚩 You have placed a flag. You Have ", flagsamt, " Flags 🚩 ")
            print("")
    elif ask == "1":
        lost = revealSpot(x,y)
    
    if lost == "lost":
        break
    
    if checkForWin():
        print()
        print()
        print(" YOU WON !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n NICE JOBBBB")
        break
    
    print()

    
    printBoard(playerBoard)

print()
print()
printBoard(playerBoard)
    



