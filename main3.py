
import tkinter as tk
import time

window = tk.Tk()
window.title("TIKTAKTOE")
buttons = []
symbols = [['','',''],['','',''],['','','']]
player = "X"
turn = 0
possible_enemy = ["player","KI"]
enemy = possible_enemy[0]
AI_played = False
gameend = False

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

def winner():
    global player, turn, symbols, gameend
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=player,command=lambda i=i, j=j: None)
    gameend = True

def reset():
    global turn, symbols, gameend
    if gameend or turn >= 9:
        time.sleep(1)
        turn = 0
        symbols = [['','',''],['','',''],['','','']]
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(text="", command=lambda i=i, j=j: click(i, j))
        gameend = False
    window.after(100, reset)

def playercheck():
    #check who plays
    if turn % 2:
        if enemy == "player":
            None
        if enemy == "KI":
            KIplay()
    window.after(100,playercheck)
            

def KIplay():
    None

for i in range(3):
    row = []
    for j in range(3):
        button = tk.Button(window, text="", font=("Arial", 40), width=5, height=2,command=lambda i=i, j=j: click(i, j))
        button.grid(row=i, column=j)
        row.append(button)
    buttons.append(row)

window.after(0, reset)
window.after(0, playercheck)
window.mainloop()