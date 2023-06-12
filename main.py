import tkinter as tk

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
        self.turn = "X"
        self.buttons = []
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 40), width=5, height=2, command=lambda i=i, j=j: self.click_button(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    
    def start(self):
        self.root.mainloop()
    
    def click_button(self, i, j):
        if self.board[i][j] == "":
            self.buttons[i][j].config(text=self.turn)
            self.board[i][j] = self.turn
            if self.check_win():
                self.show_win_message()
            elif self.check_draw():
                self.show_draw_message()
            else:
                self.switch_turn()
                if self.turn == "O":
                    i, j = self.minimax(self.board, "O")
                    self.board[i][j] = "O"
                    self.buttons[i][j].config(text="O")
                    if self.check_win():
                        self.show_win_message()
                    elif self.check_draw():
                        self.show_draw_message()
                    else:
                        self.switch_turn()
    
    def switch_turn(self):
        self.turn = "O" if self.turn == "X" else "X"
    
    def check_win(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    
    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    return False
        return True
    
    def reset_board(self):
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="")
        self.turn = "X"
    
    def show_win_message(self):
        winner = self.turn
        message = f"{winner} wins!"
        self.show_message(message)
    
    def show_draw_message(self):
        message = "Draw!"
        self.show_message(message)
    
    def show_message(self, message):
        win = tk.Toplevel()
        win.wm_title("Game Over")
        label = tk.Label(win, text=message, font=("Arial", 20))
        label.pack(side="top", pady=20)
        button = tk.Button(win, text="Play again", font=("Arial", 20), command=lambda: (win.destroy(), self.reset_board()))
        button.pack(side="top", pady=20)
    
def minimax(self, board, player):
    if self.check_win():
        if player == "X":
            return -1
        elif player == "O":
            return 1
    elif self.check_draw():
        return 0

    if player == "O":
        best_score = -1000
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player
                    score = self.minimax(board, "X")
                    board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.best_move = best_move
            return best_score
        else:
            return 0
    elif player == "X":
        best_score = 1000
        best_move = None
        for i in range(3):
            for j in range(3):
                if board[i][j] == "":
                    board[i][j] = player
                    score = self.minimax(board, "O")
                    board[i][j] = ""
                    if score < best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            self.best_move = best_move
            return best_score
        else:
            return 0


game = TicTacToe()
game.start()
