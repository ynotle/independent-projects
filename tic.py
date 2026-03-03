list = {
    "Top Left":" ",
    "Top Middle":" ",
    "Top Right":" ",
    "Middle Left":" ",
    "Middle Middle":" ",
    "Middle Right":" ",
    "Bottom Left":" ",
    "Bottom Middle":" ",
    "Bottom Right":" "
}
def board():
    print(f"      |      |      \n   {list["Top Left"]}  |   {list["Top Middle"]}  |   {list["Top Right"]}   \n______|______|______\n      |      |      \n   {list["Middle Left"]}  |   {list["Middle Middle"]}  |   {list["Middle Right"]}   \n______|______|______\n      |      |      \n   {list["Bottom Left"]}  |   {list["Bottom Middle"]}  |   {list["Bottom Right"]}   \n      |      |      \n")
# print("      |      |      \n      |      |      \n______|______|______")
# print("      |      |      \n      |      |      \n______|______|______")
# print("      |      |      \n      |      |      \n      |      |      ")

#for the list there are four states, False, XTrue, OTrue
def Turn(x):
      x+=1
      return x

def checker(list,location): 
    if list[location]=="O" or list[location]=="X":
         print("you've already been here")
         return True
    else:
         return False

# def EvenOdd():
#       if (ticker % 2) ==0:
#             print("even")
#       else: 
#             print("odd")

Player1=True

ticker=int(0)

def win():
    #for player X
    if list["Bottom Left"]=="X" and list["Bottom Middle"]=="X" and list["Bottom Right"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Middle Left"]=="X" and list["Middle Middle"]=="X" and list["Middle Right"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Left"]=="X" and list["Top Middle"]=="X" and list["Top Right"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Left"]=="X" and list["Middle Left"]=="X" and list["Bottom Left"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Middle"]=="X" and list["Middle Middle"]=="X" and list["Bottom Middle"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Right"]=="X" and list["Middle Right"]=="X" and list["Bottom Right"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Right"]=="X" and list["Middle Middle"]=="X" and list["Bottom Left"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    if list["Top Left"]=="X" and list["Middle Middle"]=="X" and list["Bottom Right"]=="X":
        print("yay!! FOR PLAYER X")
        return True
    #for player O
    if list["Bottom Left"]=="O" and list["Bottom Middle"]=="O" and list["Bottom Right"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Middle Left"]=="O" and list["Middle Middle"]=="O" and list["Middle Right"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Left"]=="O" and list["Top Middle"]=="O" and list["Top Right"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Left"]=="O" and list["Middle Left"]=="O" and list["Bottom Left"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Middle"]=="O" and list["Middle Middle"]=="O" and list["Bottom Middle"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Right"]=="O" and list["Middle Right"]=="O" and list["Bottom Right"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Right"]=="O" and list["Middle Middle"]=="O" and list["Bottom Left"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    if list["Top Left"]=="O" and list["Middle Middle"]=="O" and list["Bottom Right"]=="O":
        print("yay!! FOR PLAYER O")
        return True
    
    else:
        return False
     

while True:
    board()
    if Player1:
        location = input("What's Your Move, Player O: ")   
    else:
        location = input("What's Your Move, Player X: ")   
    location=location.title()
    if location.title() in list: #this checks if ANY move is VALID
        if checker(list,location): # this checks if the move made is taken or not, if this is true, then pass
             pass
        else: #underneath here is for all the stuff if its a valid move
            if Player1:
                #print("it's player 'O's turn")
                list[location]="O"
                # print(f"List Location T/F: {list[location]}")
                # ticker=Turn(ticker)
                # print(f"Turn Number: {ticker}")
                Player1=not Player1
                # print(f"Player 1 Counter: {Player1}")
                #print(list["Bottom Right"])
            else:
                # print("it's player 'X's turn")
                list[location]="X"
                # print(f"List Location T/F: {list[location]}")
                # ticker=Turn(ticker)
                # print(f"Turn Number: {ticker}")
                Player1=not Player1
                # print(f"Player 1 Counter: {Player1}")
        if win():
            break
    if location=="J":
        print(list)
    if location=="W":
        list["Bottom Left"]="X"
        list["Bottom Middle"]="X"
        list["Bottom Right"]="X"
        print("hello there")
    else:
        pass

# currently this list is only true or false, but it doesn't indicate if its an x or an o taking up that spot
