import tkinter as tk
import sys
import os

def resource_path(filename):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, filename)
    return filename

#window settings
window = tk.Tk()
window.title("Chess score tracker")
icon = tk.PhotoImage(file=resource_path("chess_icon_app.png"))
window.iconphoto(True, icon)
window.geometry("390x370")
window.resizable(False, False)
window.config()

wins = 0
draws = 0
losses = 0

def update_title_win():
    gameresult.config(text="You won!")
def update_title_lost():
    gameresult.config(text="You lost.")

def buttons_off():
    w_button.config(state="disabled", cursor="X_cursor")
    d_button.config(state="disabled", cursor="X_cursor")
    l_button.config(state="disabled", cursor="X_cursor")

def win_click():
    global wins
    wins+=1
    if wins == 3:
        update_title_win()
        buttons_off()
    update_win()

def draw_click():
    global draws
    draws+=1
    update_draw()

def lost_click():
    global losses
    losses+=1
    if losses == 3:
        update_title_lost()
        buttons_off()
    update_lost()

def update_win():
    win.config(text=f"Win: {wins}")
def update_draw():
    draw.config(text=f"Draw: {draws}")
def update_lost():
    lost.config(text=f"Lost: {losses}")

def buttons_on(): #for future updates/activates buttons/doing nothing right now
    w_button.config(state="normal")
    d_button.config(state="normal")
    l_button.config(state="normal")

def restart_setting(): #logic of restart button
    global wins, draws, losses
    if wins  > 0:
        wins = 0
    if draws > 0:
        draws = 0
    if losses > 0:
        losses = 0
    w_button.config(state="normal", cursor="arrow")
    d_button.config(state="normal", cursor="arrow")
    l_button.config(state="normal", cursor="arrow")
    gameresult.config(text="—")
    win.config(text="Win: 0")
    draw.config(text="Draw: 0")
    lost.config(text="Lost: 0")
#Lables
title = tk.Label(window, 
                 text="Score tracker",
                 font=("Impact", 25, ""))
title.pack()

title_2 = tk.Label(window, 
                   text="Please, choose the result of the game: ",
                   font=("Arial", 15, "bold"))
title_2.pack(padx=10)

restart_button = tk.Button(window,
                           text="Restart",
                           font=("Arial", 15, "bold"),
                           command=restart_setting)
restart_button.pack(side="bottom", pady=10)

gameresult = tk.Label(window,
                      text="—",
                      font=("Arial", 15, "bold"))
gameresult.pack(side="bottom")

title_result = tk.Label(window,
                      text="Result of the match:",
                      font=("Arial", 15, "bold"))
title_result.pack(side="bottom")

lost = tk.Label(window,
               text="Lost: 0",
               font=("Arial", 15, "bold"))
lost.pack(side="bottom", anchor="w", padx=10)

draw = tk.Label(window,
               text="Draw: 0",
               font=("Arial", 15, "bold"))
draw.pack(side="bottom", anchor="w", padx=10)

win = tk.Label(window,
               text="Win: 0",
               font=("Arial", 15, "bold"))
win.pack(side="bottom", anchor="w", padx=10)

#Buttons
w_button = tk.Button(window,
                     text="Win",
                     font=("Arial", 15, "bold"),
                     bg="#6eff68",
                     fg="#333333",
                     activebackground="#a0f99d",
                     activeforeground="#333333",
                     command= win_click)
w_button.config()
w_button.pack(side="left", padx=30, pady=10)

d_button = tk.Button(window,
                     text="Draw",
                     font=("Arial", 15, "bold"),
                     bg="#bfbfbf",
                     fg="#333333",
                     activebackground="#dddddd",
                     activeforeground="#333333",
                     command=draw_click)
d_button.pack(side="left", padx=30, pady=10)

l_button = tk.Button(window,
                     text="Lost",
                     font=("Arial", 15, "bold"),
                     bg="#ff3a3a",
                     fg="#333333",
                     activebackground="#ff7474",
                     activeforeground="#333333",
                     command=lost_click)
l_button.pack(side="left", padx=30, pady=10)
window.mainloop()