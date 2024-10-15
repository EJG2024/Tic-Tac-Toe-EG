import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tic-Tac-Toe")
        self.window.configure(bg="grey")  # Set background color to grey

        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(
                    self.window,
                    text=" ",
                    font=("Helvetica", 24),
                    width=5,
                    height=2,
                    command=lambda row=i, col=j: self.on_button_click(row, col),
                )
                self.buttons[i][j].grid(row=i, column=j)

        reset_button = tk.Button(
            self.window,
            text="Reset",
            font=("Helvetica", 12),
            command=self.reset_game
        )
        reset_button.grid(row=3, column=1)

    def on_button_click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            if self.current_player == "X":
                self.buttons[row][col].config(text=self.current_player, fg="blue")  # Blue for X
            else:
                self.buttons[row][col].config(text=self.current_player, fg="red")  # Red for O

            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] and row[0] != " ":
                return True
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != " ":
                return True
        # Check diagonals
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] or
                self.board[0][2] == self.board[1][1] == self.board[2][0]) and self.board[1][1] != " ":
            return True
        return False

    def is_board_full(self):
        for row in self.board:
            for cell in row:
                if cell == " ":
                    return False
        return True

    def reset_game(self):
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()