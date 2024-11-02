import tkinter as tk
from tkinter import messagebox

# Game Logic Class
class UserInterface:
    def __init__(self, board_size, game_mode):

        self.board_size = board_size # Initializing board size
        self.game_mode = game_mode # Initializing game mode

        self.board = [['' for _ in range(board_size)] for _ in range(board_size)] # 2D Board
        # The starting player will be blue
        self.current_player = 'blue'
        self.blue_player_win_count = 0 # starts at 0
        self.red_player_win_count = 0 # starts at 0
        self.tile_count = board_size * board_size
        self.turn_count = 1
        
    def make_move(self, row, col, letter,buttons):
        # Check if the selected cell is empty
        if self.board[row][col] == '':
            # Place the letter in the cell
            self.board[row][col] = letter 
            buttons[row][col].config(text=letter)  # Update the button text
            # Update the button color based on the current player
            
            buttons[row][col].config(fg=f"{self.current_player}")

            #Check if game ends
            self.check_game_end(row, col, letter, buttons)         

        else:
            # Raise an error if the cell is already occupied
            raise ValueError("Cell is already occupied.")

    def switch_turn(self):
        # Toggle the current turn between 'blue' and 'red'
        self.current_player = 'red' if self.current_player == 'blue' else 'blue'

    def check_game_end(self, row, col, current_letter, buttons):
        self.simple_game_ended = False
        win_count = 0

        # Vertical and horizontal
        if current_letter == 'S':
            letter_O = 'O'

            if row+2 < self.board_size and self.board[row+1][col] == letter_O :
                #check same direction for another S
                if self.board[row+2][col] == current_letter:
                    self.simple_game_ended = True  
                    win_count = win_count+1     
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created 
                    buttons[row+2][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and self.board[row-1][col] == letter_O :
                #check same direction for another S
                if self.board[row-2][col] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col+2 < self.board_size and self.board[row][col+1] == letter_O :
                #check same direction for another S
                if self.board[row][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col-2 >= 0 and self.board[row][col-1] == letter_O :
                #check same direction for another S
                if self.board[row][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and col-2 >= 0 and self.board[row-1][col-1] == letter_O :          
                #check same direction for another S
                if self.board[row-2][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row-2 >= 0 and col+2 < self.board_size and self.board[row-1][col+1] == letter_O :          
                #check same direction for another S
                if self.board[row-2][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-2][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+2 < self.board_size and col+2 < self.board_size and self.board[row+1][col+1] == letter_O :          
                #check same direction for another S
                if self.board[row+2][col+2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+2][col+2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+2 < self.board_size and col-2 >= 0 and self.board[row+1][col-1] == letter_O :          
                #check same direction for another S
                if self.board[row+2][col-2] == current_letter:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+2][col-2].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
        # If the last played letter is 'O'
        elif current_letter == 'O':
            letter_S = 'S'

            if row+1 < self.board_size and self.board[row+1][col] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and self.board[row-1][col] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if col+1 < self.board_size and self.board[row][col+1] == letter_S :
                #check opposite direction for another S
                if col-1 >= 0 and self.board[row][col-1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+1 < self.board_size and col+1 < self.board_size and self.board[row+1][col+1] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and col-1 >= 0 and self.board[row-1][col-1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
            if row+1 < self.board_size and col-1 >= 0 and self.board[row+1][col-1] == letter_S :
                #check opposite direction for another S
                if row-1 >= 0 and col+1 < self.board_size and self.board[row-1][col+1] == letter_S:
                    self.simple_game_ended = True
                    win_count = win_count+1
                    buttons[row][col].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row+1][col-1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
                    buttons[row-1][col+1].config(bg=f"{self.current_player}",fg="black") # Used to turn the letters on the board to black, because the dissapeard when the tiles switched colors when the SOS sequence was created
        if self.game_mode == "Simple Game":
            if self.simple_game_ended == True:
                #game ended!!!
                messagebox.showinfo("WIN", f"{self.current_player.upper()} WON!!!!!!!")

            elif self.turn_count == self.tile_count:
                messagebox.showinfo("WHO WON?", "IT'S A DRAW!")

        elif self.game_mode == "General Game":
            if self.current_player == 'blue':
                self.blue_player_win_count = self.blue_player_win_count + win_count 
            else:
                self.red_player_win_count = self.red_player_win_count + win_count
            # Checking whether the General Game has ended when the board is full and it announces the winner or if it's a draw 
            if self.turn_count == self.tile_count:
                if self.blue_player_win_count == self.red_player_win_count:
                    messagebox.showinfo("WHO WON?", "IT'S A DRAW!")
                elif self.blue_player_win_count > self.red_player_win_count:
                    messagebox.showinfo("WIN", "BLUE WON!!!!!!!")
                elif self.red_player_win_count > self.blue_player_win_count:
                    messagebox.showinfo("WIN", "RED WON!!!!!!!!")

        
