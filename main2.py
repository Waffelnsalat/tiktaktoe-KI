import tkinter as tk
import random

window = tk.Tk()
window.title("TIKTAKTOE")
buttons = []
symbols = [['','',''],['','',''],['','','']]
player = "X"
turn = 0
possible_enemy = ["player","easy","normal","hard","impossible"]
enemy = possible_enemy[4]
AI_played = False

def click(i, j):
    global turn, player, symbols
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    buttons[i][j].config(text=player,command=lambda i=i, j=j: None)
    symbols[i][j] = player
    turn = turn + 1
    #check for winners
    for i in range(3):
        if symbols[i][0] == symbols[i][1] and symbols[i][0] == symbols[i][2] and not symbols[i][0]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][i] == symbols[1][i] and symbols[0][i] == symbols[2][i] and not symbols[0][i]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][0] == symbols[1][1] and symbols[1][1] == symbols[2][2] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][2] == symbols[1][1] and symbols[1][1] == symbols[2][0] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break


def easyplay():
    global turn, player, symbols
    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    turn = turn + 1
    while True:    
        spot1 = random.randint(0, 2)
        spot2 = random.randint(0, 2)
        if symbols[spot1][spot2] == "":
            buttons[spot1][spot2].config(text=player,command=lambda i=spot1, j=spot2: None)
            symbols[spot1][spot2] = player
            break
        else:
            if turn >= 9:
                print("tie")
                break
     #check for winners
    for i in range(3):
        if symbols[i][0] == symbols[i][1] and symbols[i][0] == symbols[i][2] and not symbols[i][0]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][i] == symbols[1][i] and symbols[0][i] == symbols[2][i] and not symbols[0][i]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][0] == symbols[1][1] and symbols[1][1] == symbols[2][2] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][2] == symbols[1][1] and symbols[1][1] == symbols[2][0] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break


def normalplay():
    global turn, player, symbols, AI_played
    AI_played = False

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    turn = turn + 1

    #make play
    for i in range(3):
        #horizontal check
        if symbols[i][0] == symbols[i][1] and symbols[i][2]== "" and not symbols[i][0] == "":
            buttons[i][2].config(text=player,command=lambda i=i, j=2: None)
            symbols[i][2] = player
            AI_played = True
            break
        elif symbols[i][1] == symbols[i][2] and symbols[i][0]== "" and not symbols[i][1] == "":
            buttons[i][0].config(text=player,command=lambda i=i, j=0: None)
            symbols[i][0] = player
            AI_played = True
            break
        elif symbols[i][0] == symbols[i][2] and symbols[i][1]== "" and not symbols[i][2] == "":
            buttons[i][1].config(text=player,command=lambda i=i, j=1: None)
            symbols[i][1] = player
            AI_played = True
            break
        #Vertical check
        elif symbols[0][i] == symbols[1][i] and symbols[2][i]=="" and not symbols[0][i] == "":
            buttons[2][i].config(text=player,command=lambda i=2, j=i: None)
            symbols[2][i] = player
            AI_played = True
            break
        elif symbols[2][i] == symbols[0][i] and symbols[1][i]=="" and not symbols[0][i] == "":
            buttons[1][i].config(text=player,command=lambda i=1, j=i: None)
            symbols[1][i] = player
            AI_played = True
            break
        elif symbols[1][i] == symbols[2][i] and symbols[0][i]=="" and not symbols[2][i] == "":
            buttons[0][i].config(text=player,command=lambda i=0, j=i: None)
            symbols[0][i] = player
            AI_played = True
            break

    # Random move if no strategic move found
    while not AI_played: 
        spot1 = random.randint(0, 2)
        spot2 = random.randint(0, 2)
        if symbols[spot1][spot2] == "":
            buttons[spot1][spot2].config(text=player,command=lambda i=spot1, j=spot2: None)
            symbols[spot1][spot2] = player
            AI_played = True
        else:
            if turn >= 9:
                print("tie")
                break

    #check for winners
    for i in range(3):
        if symbols[i][0] == symbols[i][1] and symbols[i][0] == symbols[i][2] and not symbols[i][0]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][i] == symbols[1][i] and symbols[0][i] == symbols[2][i] and not symbols[0][i]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][0] == symbols[1][1] and symbols[1][1] == symbols[2][2] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][2] == symbols[1][1] and symbols[1][1] == symbols[2][0] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break

def hardplay():
    global turn, player, symbols, AI_played
    AI_played = False

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    turn = turn + 1

    #make play
    for i in range(3):
        #horizontal check
        if symbols[i][0] == symbols[i][1] and symbols[i][2]== "" and not symbols[i][0] == "":
            if symbols[i][0] == "O":
                buttons[i][2].config(text=player,command=lambda i=i, j=2: None)
                symbols[i][2] = player
                AI_played = True
                break
        elif symbols[i][1] == symbols[i][2] and symbols[i][0]== "" and not symbols[i][1] == "":
            if symbols[i][1] == "O":
                buttons[i][0].config(text=player,command=lambda i=i, j=0: None)
                symbols[i][0] = player
                AI_played = True
                break
        elif symbols[i][0] == symbols[i][2] and symbols[i][1]== "" and not symbols[i][2] == "":
            if symbols[i][0] == "O":
                buttons[i][1].config(text=player,command=lambda i=i, j=1: None)
                symbols[i][1] = player
                AI_played = True
                break
        #Vertical check
        elif symbols[0][i] == symbols[1][i] and symbols[2][i]=="" and not symbols[0][i] == "":
            if symbols[0][i] == "O":
                buttons[2][i].config(text=player,command=lambda i=2, j=i: None)
                symbols[2][i] = player
                AI_played = True
                break
        elif symbols[2][i] == symbols[0][i] and symbols[1][i]=="" and not symbols[0][i] == "":
            if symbols[2][i] == "O":
                buttons[1][i].config(text=player,command=lambda i=1, j=i: None)
                symbols[1][i] = player
                AI_played = True
                break
        elif symbols[1][i] == symbols[2][i] and symbols[0][i]=="" and not symbols[2][i] == "":
            if symbols[1][i] == "O":
                buttons[0][i].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][i] = player
                AI_played = True
                break
        elif symbols[0][0] == symbols[1][1] and symbols[2][2] == "" and not symbols[0][0] == "":
            if symbols[1][1] == "O":
                buttons[2][2].config(text=player,command=lambda i=0, j=i: None)
                symbols[2][2] = player
                AI_played = True
                break
        elif symbols[0][2] == symbols[1][1] and symbols[2][0] == "" and not symbols[0][2] == "":
            if symbols[1][1] == "O":
                buttons[2][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[2][0] = player
                AI_played = True
                break
        elif symbols[0][0] == symbols[2][2] and symbols[1][1] == "" and not symbols[0][0] == "":
            if symbols[2][2] == "O":
                buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][1] = player
                AI_played = True
                break
        elif symbols[0][2] == symbols[2][0] and symbols[1][1] == "" and not symbols[0][2] == "":
            if symbols[2][0] == "O":
                buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][1] = player
                AI_played = True
                break
        elif symbols[1][1] == symbols[2][2] and symbols[0][0] == "" and not symbols[1][1] == "":
            if symbols[2][2] == "O":
                buttons[0][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][0] = player
                AI_played = True
                break
        elif symbols[1][1] == symbols[2][0] and symbols[0][2] == "" and not symbols[1][1] == "":
            if symbols[2][0] == "O":
                buttons[0][2].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][2] = player
                AI_played = True
                break
    if not AI_played:
        for i in range(3):
            #horizontal check
            if symbols[i][0] == symbols[i][1] and symbols[i][2]== "" and not symbols[i][0] == "":
                buttons[i][2].config(text=player,command=lambda i=i, j=2: None)
                symbols[i][2] = player
                AI_played = True
                break
            elif symbols[i][1] == symbols[i][2] and symbols[i][0]== "" and not symbols[i][1] == "":
                buttons[i][0].config(text=player,command=lambda i=i, j=0: None)
                symbols[i][0] = player
                AI_played = True
                break
            elif symbols[i][0] == symbols[i][2] and symbols[i][1]== "" and not symbols[i][2] == "":
                buttons[i][1].config(text=player,command=lambda i=i, j=1: None)
                symbols[i][1] = player
                AI_played = True
                break
            #Vertical check
            elif symbols[0][i] == symbols[1][i] and symbols[2][i]=="" and not symbols[0][i] == "":
                buttons[2][i].config(text=player,command=lambda i=2, j=i: None)
                symbols[2][i] = player
                AI_played = True
                break
            elif symbols[2][i] == symbols[0][i] and symbols[1][i]=="" and not symbols[0][i] == "":
                buttons[1][i].config(text=player,command=lambda i=1, j=i: None)
                symbols[1][i] = player
                AI_played = True
                break
            elif symbols[1][i] == symbols[2][i] and symbols[0][i]=="" and not symbols[2][i] == "":
                buttons[0][i].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][i] = player
                AI_played = True
                break
            elif symbols[0][0] == symbols[1][1] and symbols[2][2] == "" and not symbols[0][0] == "":
                    buttons[2][2].config(text=player,command=lambda i=0, j=i: None)
                    symbols[2][2] = player
                    AI_played = True
                    break
            elif symbols[0][2] == symbols[1][1] and symbols[2][0] == "" and not symbols[0][2] == "":
                    buttons[2][0].config(text=player,command=lambda i=0, j=i: None)
                    symbols[2][0] = player
                    AI_played = True
                    break
            elif symbols[0][0] == symbols[2][2] and symbols[1][1] == "" and not symbols[0][0] == "":
                    buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                    symbols[1][1] = player
                    AI_played = True
                    break
            elif symbols[0][2] == symbols[2][0] and symbols[1][1] == "" and not symbols[0][2] == "":
                    buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                    symbols[1][1] = player
                    AI_played = True
                    break
            elif symbols[1][1] == symbols[2][2] and symbols[0][0] == "" and not symbols[1][1] == "":
                    buttons[0][0].config(text=player,command=lambda i=0, j=i: None)
                    symbols[0][0] = player
                    AI_played = True
                    break
            elif symbols[1][1] == symbols[2][0] and symbols[0][2] == "" and not symbols[1][1] == "":
                    buttons[0][2].config(text=player,command=lambda i=0, j=i: None)
                    symbols[0][2] = player
                    AI_played = True
                    break


    # Random move if no strategic move found
    while not AI_played:
        print("test") 
        spot1 = random.randint(0, 2)
        spot2 = random.randint(0, 2)
        if symbols[spot1][spot2] == "":
            buttons[spot1][spot2].config(text=player,command=lambda i=spot1, j=spot2: None)
            symbols[spot1][spot2] = player
            AI_played = True
        else:
            if turn >= 9:
                print("tie")
                break

    #check for winners
    for i in range(3):
        if symbols[i][0] == symbols[i][1] and symbols[i][0] == symbols[i][2] and not symbols[i][0]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][i] == symbols[1][i] and symbols[0][i] == symbols[2][i] and not symbols[0][i]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][0] == symbols[1][1] and symbols[1][1] == symbols[2][2] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][2] == symbols[1][1] and symbols[1][1] == symbols[2][0] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break

def impossibleplay():
    global turn, player, symbols, AI_played
    AI_played = False

    if turn % 2 == 0:
        player = "X"
    else:
        player = "O"
    turn = turn + 1

    #make play
    for i in range(3):
        #horizontal check
        if symbols[i][0] == symbols[i][1] and symbols[i][2]== "" and not symbols[i][0] == "":
            if symbols[i][0] == "O":
                buttons[i][2].config(text=player,command=lambda i=i, j=2: None)
                symbols[i][2] = player
                AI_played = True
                break
        elif symbols[i][1] == symbols[i][2] and symbols[i][0]== "" and not symbols[i][1] == "":
            if symbols[i][1] == "O":
                buttons[i][0].config(text=player,command=lambda i=i, j=0: None)
                symbols[i][0] = player
                AI_played = True
                break
        elif symbols[i][0] == symbols[i][2] and symbols[i][1]== "" and not symbols[i][2] == "":
            if symbols[i][0] == "O":
                buttons[i][1].config(text=player,command=lambda i=i, j=1: None)
                symbols[i][1] = player
                AI_played = True
                break
        #Vertical check
        elif symbols[0][i] == symbols[1][i] and symbols[2][i]=="" and not symbols[0][i] == "":
            if symbols[0][i] == "O":
                buttons[2][i].config(text=player,command=lambda i=2, j=i: None)
                symbols[2][i] = player
                AI_played = True
                break
        elif symbols[2][i] == symbols[0][i] and symbols[1][i]=="" and not symbols[0][i] == "":
            if symbols[2][i] == "O":
                buttons[1][i].config(text=player,command=lambda i=1, j=i: None)
                symbols[1][i] = player
                AI_played = True
                break
        elif symbols[1][i] == symbols[2][i] and symbols[0][i]=="" and not symbols[2][i] == "":
            if symbols[1][i] == "O":
                buttons[0][i].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][i] = player
                AI_played = True
                break
        elif symbols[0][0] == symbols[1][1] and symbols[2][2] == "" and not symbols[0][0] == "":
            if symbols[1][1] == "O":
                buttons[2][2].config(text=player,command=lambda i=0, j=i: None)
                symbols[2][2] = player
                AI_played = True
                break
        elif symbols[0][2] == symbols[1][1] and symbols[2][0] == "" and not symbols[0][2] == "":
            if symbols[1][1] == "O":
                buttons[2][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[2][0] = player
                AI_played = True
                break
        elif symbols[0][0] == symbols[2][2] and symbols[1][1] == "" and not symbols[0][0] == "":
            if symbols[2][2] == "O":
                buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][1] = player
                AI_played = True
                break
        elif symbols[0][2] == symbols[2][0] and symbols[1][1] == "" and not symbols[0][2] == "":
            if symbols[2][0] == "O":
                buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][1] = player
                AI_played = True
                break
        elif symbols[1][1] == symbols[2][2] and symbols[0][0] == "" and not symbols[1][1] == "":
            if symbols[2][2] == "O":
                buttons[0][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][0] = player
                AI_played = True
                break
        elif symbols[1][1] == symbols[2][0] and symbols[0][2] == "" and not symbols[1][1] == "":
            if symbols[2][0] == "O":
                buttons[0][2].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][2] = player
                AI_played = True
                break
    if not AI_played:
        for i in range(3):
            #horizontal check
            if symbols[i][0] == symbols[i][1] and symbols[i][2]== "" and not symbols[i][0] == "":
                buttons[i][2].config(text=player,command=lambda i=i, j=2: None)
                symbols[i][2] = player
                AI_played = True
                break
            elif symbols[i][1] == symbols[i][2] and symbols[i][0]== "" and not symbols[i][1] == "":
                buttons[i][0].config(text=player,command=lambda i=i, j=0: None)
                symbols[i][0] = player
                AI_played = True
                break
            elif symbols[i][0] == symbols[i][2] and symbols[i][1]== "" and not symbols[i][2] == "":
                buttons[i][1].config(text=player,command=lambda i=i, j=1: None)
                symbols[i][1] = player
                AI_played = True
                break
            #Vertical check
            elif symbols[0][i] == symbols[1][i] and symbols[2][i]=="" and not symbols[0][i] == "":
                buttons[2][i].config(text=player,command=lambda i=2, j=i: None)
                symbols[2][i] = player
                AI_played = True
                break
            elif symbols[2][i] == symbols[0][i] and symbols[1][i]=="" and not symbols[0][i] == "":
                buttons[1][i].config(text=player,command=lambda i=1, j=i: None)
                symbols[1][i] = player
                AI_played = True
                break
            elif symbols[1][i] == symbols[2][i] and symbols[0][i]=="" and not symbols[2][i] == "":
                buttons[0][i].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][i] = player
                AI_played = True
                break
            elif symbols[0][0] == symbols[1][1] and symbols[2][2] == "" and not symbols[0][0] == "":
                    buttons[2][2].config(text=player,command=lambda i=0, j=i: None)
                    symbols[2][2] = player
                    AI_played = True
                    break
            elif symbols[0][2] == symbols[1][1] and symbols[2][0] == "" and not symbols[0][2] == "":
                    buttons[2][0].config(text=player,command=lambda i=0, j=i: None)
                    symbols[2][0] = player
                    AI_played = True
                    break
            elif symbols[0][0] == symbols[2][2] and symbols[1][1] == "" and not symbols[0][0] == "":
                    buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                    symbols[1][1] = player
                    AI_played = True
                    break
            elif symbols[0][2] == symbols[2][0] and symbols[1][1] == "" and not symbols[0][2] == "":
                    buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                    symbols[1][1] = player
                    AI_played = True
                    break
            elif symbols[1][1] == symbols[2][2] and symbols[0][0] == "" and not symbols[1][1] == "":
                    buttons[0][0].config(text=player,command=lambda i=0, j=i: None)
                    symbols[0][0] = player
                    AI_played = True
                    break
            elif symbols[1][1] == symbols[2][0] and symbols[0][2] == "" and not symbols[1][1] == "":
                    buttons[0][2].config(text=player,command=lambda i=0, j=i: None)
                    symbols[0][2] = player
                    AI_played = True
                    break


    # Random move if no strategic move found
    while not AI_played: 
        spot1 = random.randint(0, 2)
        spot2 = random.randint(0, 2)
        if symbols[1][1] == player:
            if symbols[0][1] == "" and symbols[2][1] == "":
                buttons[0][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][1] = player
                AI_played = True
            elif symbols[1][0] == "" and symbols [1][2] == "":
                buttons[1][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][0] = player
                AI_played = True
            elif not symbols[1][0] == "" or not symbols[2][0] == "" and not symbols[0][1] == "" or not symbols[0][2] == "":
                buttons[0][0].config(text=player,command=lambda i=0, j=i: None)
                symbols[0][0] = player
                AI_played = True
            elif not symbols[1][2] == "" or not symbols[1][2] == "" and not symbols[2][1] == "" :
                buttons[2][2].config(text=player,command=lambda i=0, j=i: None)
                symbols[2][2] = player
                AI_played = True
            elif symbols[spot1][spot2] == "":
                buttons[spot1][spot2].config(text=player,command=lambda i=spot1, j=spot2: None)
                symbols[spot1][spot2] = player
                AI_played = True
                print("test")
            else:
                if turn >= 9:
                    print("tie")
                    break
        elif symbols[1][1] == "":
                buttons[1][1].config(text=player,command=lambda i=0, j=i: None)
                symbols[1][1] = player
                AI_played = True
        elif symbols[spot1][spot2] == "":
            buttons[spot1][spot2].config(text=player,command=lambda i=spot1, j=spot2: None)
            symbols[spot1][spot2] = player
            AI_played = True
            print("test")
        else:
            if turn >= 9:
                print("tie")
                break

    #check for winners
    for i in range(3):
        if symbols[i][0] == symbols[i][1] and symbols[i][0] == symbols[i][2] and not symbols[i][0]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][i] == symbols[1][i] and symbols[0][i] == symbols[2][i] and not symbols[0][i]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][0] == symbols[1][1] and symbols[1][1] == symbols[2][2] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
        elif symbols[0][2] == symbols[1][1] and symbols[1][1] == symbols[2][0] and not symbols [1][1]== "":
            print(player +" won")
            winner()
            break
    

def winner():
    global player, turn
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=player,command=lambda i=i, j=j: None)
    turn = 0


def playercheck():
    #check who plays
    if turn % 2:
        if enemy == "player":
            None
        elif enemy == "easy":
            easyplay()
        elif enemy == "normal":
            normalplay()
        elif enemy == "hard":
            hardplay()
        elif enemy == "impossible":
            impossibleplay()
    window.after(100,playercheck)

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 40), width=5, height=2,command=lambda i=i, j=j: click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

window.after(0, playercheck)
window.mainloop()