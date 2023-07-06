import tkinter as tk

window = tk.Tk()
window.title("TIKTAKTOE")

buttons = []
board = [['', '', ''], ['', '', ''], ['', '', '']]
players = ["X", "O"]
current_player = players[0]

def click(i, j):
    global current_player
    if board[i][j] == '':
        buttons[i][j].config(text=current_player, state=tk.DISABLED)
        board[i][j] = current_player
        check_winner()
        current_player = players[1] if current_player == players[0] else players[0]



def check_winner():
    if (
        (board[0][0] == board[0][1] == board[0][2] != '') or
        (board[1][0] == board[1][1] == board[1][2] != '') or
        (board[2][0] == board[2][1] == board[2][2] != '') or
        (board[0][0] == board[1][0] == board[2][0] != '') or
        (board[0][1] == board[1][1] == board[2][1] != '') or
        (board[0][2] == board[1][2] == board[2][2] != '') or
        (board[0][0] == board[1][1] == board[2][2] != '') or
        (board[0][2] == board[1][1] == board[2][0] != '')
    ):
        print(current_player + " won")
        winner()
    elif((board[0][0] and board[0][1] and board[0][2] 
          and board[1][0] and board[1][1] and board[1][2]
          and board[1][0] and board[1][1] and board[1][2]) != ''):
        tie()


def winner():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=current_player, state=tk.DISABLED)
    window.after(1000, reset)


def tie():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="tie", state=tk.DISABLED)
    window.after(1000, reset)

def reset():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL)
            board[i][j] = ''

def create_buttons():
    for i in range(3):
        row = []
        for j in range(3):
            button = tk.Button(window, text="", font=("Arial", 40), width=5, height=2, command=lambda i=i, j=j: click(i, j))
            button.grid(row=i, column=j)
            row.append(button)
        buttons.append(row)

create_buttons()
window.mainloop()
