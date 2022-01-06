# Import module to create GUI.
import tkinter as tk
import tkinter.font as font

def main():
    # Create GUI for the game.
    window = tk.Tk()
    x = 35
    y = 35
    window.title("Tic Tac Toe")
    window.geometry("300x300")
    

    # Establish button font size.
    space_font = font.Font(size=60)

    # Create grid.
    for row in range(0, 3):
        for column in range(0, 2):
            space = tk.Button(window, text="     ")
            space["font"] = space_font
            space.place(x=x, y=y)
            
            x += 80
        space = tk.Button(window, text="     ")
        space["font"] = space_font
        space.place(x=x, y=y)
        x = 35
        y += 85
    # Create window for gameplay
    window.mainloop()



main()