import tkinter as tk
from tkinter import Canvas, Frame, BOTH
import time

global canvas
global tic_tac_toe
global player_symbol
global win_pos_list

win_pos_list = []
tic_tac_toe =[['?' for j in range(3)] for i in range(3)]
player_symbol = 'O'

class Application(tk.Frame):
    global canvas
    def draw_main_board(self):
        """Draw a board of 3x3 size"""
        canvas.create_rectangle(100,100,400,400,outline="blue", width = 7)
        canvas.create_rectangle(200,100,200,400,outline="blue", width = 7)
        canvas.create_rectangle(300,100,300,400,outline="blue", width = 7)
        canvas.create_rectangle(100,200,400,200,outline="blue", width = 7)
        canvas.create_rectangle(100,300,400,400,outline="blue", width = 7)

    def draw_board(self, row, col):
        """Draw the player's symbol on the screen"""
        x = (col + 1) * 100
        y = (row + 1) * 100
        if player_symbol == 'O':
            canvas.create_oval(x+25, y+25, x+75, y+75, fill = "yellow")
        else:
            canvas.create_rectangle(x+25, y+25, x+75, y+75, fill = "blue")

    def display_winner(self):
        """Display who won the game"""
        canvas.unbind('<Button-1>')
        winner_text = f"'{player_symbol}' won the game"
        canvas.create_text(250,50, text=winner_text, font = ('Poppins 30 bold'))
        self.flash_win_pos()

    def display_tie(self):
        """Display that the game ended in a tie"""
        canvas.unbind('<Button-1>')
        tie_text = f"No luck. It's a tie."
        canvas.create_text(250,50, text=tie_text, font = ('Poppins 30 bold'))

    def __init__(self, master=None):
        global canvas
        super().__init__(master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        canvas = Canvas(self)
        self.draw_main_board()
        canvas.pack(fill=BOTH, expand = 1)
        canvas.update()

    def change_color_ovals(self, color):
        """Change the color of the ovals to flash"""
        global canvas
        canvas.create_oval(pos_x_1+25, pos_y_1+25, pos_x_1+75, pos_y_1+75, fill = color)
        canvas.create_oval(pos_x_2+25, pos_y_2+25, pos_x_2+75, pos_y_2+75, fill = color)
        canvas.create_oval(pos_x_3+25, pos_y_3+25, pos_x_3+75, pos_y_3+75, fill = color)
        canvas.update()

    def change_color_squares(self, color):
        """Change the color of squares to flash"""
        global canvas
        canvas.create_rectangle(pos_x_1+25, pos_y_1+25, pos_x_1+75, pos_y_1+75, fill = color)
        canvas.create_rectangle(pos_x_2+25, pos_y_2+25, pos_x_2+75, pos_y_2+75, fill = color)
        canvas.create_rectangle(pos_x_3+25, pos_y_3+25, pos_x_3+75, pos_y_3+75, fill = color)
        canvas.update()
        
    def flash_ovals(self):
        """Change the color of yellow ovals"""
        global canvas
        try:
            self.change_color_ovals(color = "red")
            time.sleep(0.10)
            self.change_color_ovals(color = "yellow")
        except:
            return


    def flash_sqaures(self):
        """Change the color of blue sqaures"""
        global canvas
        try:
            self.change_color_squares(color = "red")
            time.sleep(0.10)
            self.change_color_squares(color = "yellow")
        except:
            return

        
    def flash_on_screen(self):
        """Change the color of item in row and col according to who won the game"""
        for i in range(200):
            if player_symbol == 'O':
                self.flash_ovals()
            else:
                self.flash_sqaures()


    def flash_win_pos(self):
        """Flash the position of the row and col of the winner"""
        global pos_x_1, pos_x_2, pos_x_3, pos_y_1, pos_y_2, pos_y_3
        row_1, col_1 = win_pos_list[0][0], win_pos_list[0][1]
        row_2, col_2 = win_pos_list[1][0], win_pos_list[1][1]
        row_3, col_3 = win_pos_list[2][0], win_pos_list[2][1]
        pos_x_1, pos_y_1 = (int(col_1) + 1) * 100 , (int(row_1) + 1) * 100
        pos_x_2, pos_y_2 = (int(col_2) + 1) * 100 , (int(row_2) + 1) * 100
        pos_x_3, pos_y_3 = (int(col_3) + 1) * 100 , (int(row_3) + 1) * 100
        self.flash_on_screen()
        
        
          
"""Outer functions"""
def print_board():
    """Print the tic_tac_toe list on the console"""
    for row in tic_tac_toe:
        for col in row:
            print(col, end = ' ')
        print()
    print()


def check_rows():
    """Check the rows for if they won or not"""
    global win_pos_list
    count = 0
    for i in range(len(tic_tac_toe)):
        for j in range(len(tic_tac_toe)):
            if tic_tac_toe[i][j] == player_symbol:
                count+=1
        if count == 3:
            win_pos_list = [[i,j], [i,j-1], [i,j-2]]
            return True
        else:
            count = 0


def check_cols():
    """Check the cols for if they won or not"""
    global win_pos_list
    count = 0
    for i in range(len(tic_tac_toe)):
        for j in range(len(tic_tac_toe)):
            if tic_tac_toe[j][i] == player_symbol:
                count+=1
        if count == 3:
            win_pos_list = [[j,i], [j-1,i], [j-2,i]]
            return True
        else:
            count = 0


def check_down_diags():
    """Check the downwards diagonals to see if they won"""
    global win_pos_list
    j = 0
    count = 0
    for i in range(len(tic_tac_toe)):
        if tic_tac_toe[i][j] == player_symbol:
            count+= 1
        j+=1
    if count == 3:
        win_pos_list = [[i,j-1], [i-1,j-2], [i-2,j-3]]
        return True
    

def check_up_diags():
    """Check the upward diagons to see if they won"""
    global win_pos_list
    j = len(tic_tac_toe) - 1
    count = 0
    for i in range(len(tic_tac_toe)):
        if tic_tac_toe[i][j] == player_symbol:
            count+= 1
        j-=1
    if count == 3:
        win_pos_list = [[i,j+1], [i-1,j+2], [i-2,j+3]]
        return True

    
def check_diags():
    """Check the diagons for if they won or not"""
    down_diags_win = check_down_diags()
    up_diags_win = check_up_diags()
    if down_diags_win or up_diags_win:
        return True
    else:
        return False

def check_tie():
    """Check whether it's a tie or not"""
    tie = 0
    global tic_tac_toe
    for items in tic_tac_toe:
        if '?' not in items:
            tie+= 1
    if tie == 3:
        app.display_tie()

def check_win():
    """Call to check for rows, cols, and diag and check if either return True"""
    rows_win = check_rows()
    cols_win = check_cols()
    diags_win = check_diags()
    if rows_win or cols_win or diags_win:
        app.display_winner()
    else:
        check_tie()
        change_player()


def change_player():
    """Change to the next player from the current player"""
    global player_symbol
    if player_symbol == 'O':
        player_symbol = 'X'
    else:
        player_symbol = 'O'

def check_empty_space(row,col):
    """Check to see if the space already contains an element"""
    if tic_tac_toe[row][col] != "?":
        print("This space is already taken. Please try another")
    else:
        return True
  
def update_board(row, col):
    """Update the tic_tac_toe list according to the co-ordinates received"""
    global tic_tac_toe
    empty_space = check_empty_space(row,col)
    if empty_space:
        tic_tac_toe[row][col] = player_symbol
        app.draw_board(row, col)
        check_win()
    
    
def mouse_click_to_grid(pos_x, pos_y):
    """Convert the mouse click co-ordinates into row and col"""
    row = (pos_y // 100) - 1
    col = (pos_x // 100) - 1
    update_board(row,col)

    
def mouseClick(event):
    """Get the coordinates of the mouse click inside the board"""
    if 100 < event.x < 400 and 100 < event.y < 400:
        mouse_click_to_grid(event.x, event.y)
    else:
        print("Click on the board")


"""The main program"""     
app_frame = tk.Tk()
app_frame.geometry('500x500')
app = Application(master=app_frame)
canvas.bind("<Button-1>", mouseClick)
app.mainloop()
