import tkinter as tk
from random import randint
from tkinter import PhotoImage
import random

def check_die(current_score, die_value):
    return current_score + die_value

names = ['Godofredo', 'Waddles', 'Porcuello', 'Bacon']
comp_name = random.choice(names)

def display_scoreboard():
    scoreboard.config(state=tk.NORMAL)
    scoreboard.delete('1.0', tk.END)
    scoreboard.insert(tk.END, f"\n{'#' * 20}\n")
    scoreboard.insert(tk.END, f"Pontuação total de {username.get()}: {player_score}\n")
    scoreboard.insert(tk.END, f"Pontuação total do {comp_name}: {computer_score}\n")
    scoreboard.insert(tk.END, f"Rounds jogados: {rounds_played}\n")
    scoreboard.insert(tk.END, f"{'#' * 20}\n")
    scoreboard.config(state=tk.DISABLED)

def roll_dice():
    global player_score, computer_score, rounds_played

    player_die_value = randint(1, 6)
    computer_die_value = randint(1, 6)
    
    player_roll_label.config(text=f"{username.get()} rolou {player_die_value}")
    computer_roll_label.config(text=f"{comp_name} rolou {computer_die_value}")

    rounds_played += 1

    player_score = check_die(player_score, player_die_value)
    computer_score = check_die(computer_score, computer_die_value)

    display_scoreboard()

    if player_score >= 30:
        result_label.config(text=f"{username.get()} ganhou com uma pontuação total de {player_score}!")
        show_winner_window(username.get().upper())
        roll_button.config(state=tk.DISABLED)
    elif computer_score >= 30:
        result_label.config(text=f"{comp_name} ganhou com uma pontuação total de {computer_score}!")
        show_winner_window(comp_name.upper())
        roll_button.config(state=tk.DISABLED)

def show_winner_window(winner_name):
    winner_window = tk.Toplevel(root)
    winner_window.title("Vencedor!")
    winner_label = tk.Label(winner_window, text=f"O vencedor é {winner_name}!", font=("Arial", 18))
    winner_label.pack(padx=20, pady=20)

# Inicialização da janela principal
root = tk.Tk()
root.title("Pig Dice Game")
root.configure(bg="pink")

image=tk.PhotoImage(file="piggie.png")
image=image.subsample(1,1)

label_image=tk.Label(image=image)
label_image.place(x=0, y=0, relheight=1, relwidth=1)

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x_coordinate = (screen_width / 2) - (width / 2)
    y_coordinate = (screen_height / 2) - (height / 2)
    window.geometry("%dx%d+%d+%d" % (width, height, x_coordinate, y_coordinate))

# Definir a geometria da janela
window_width = 600
window_height = 600
center_window(root, window_width, window_height)

welcome_message = (f"""
        Bem-vindo ao 'Pig', um jogo de dados!

    Neste jogo, um usuário e seu oponente Sr. {comp_name} 
    jogam um dado de 6 faces a cada rodada. A pontuação de cada 
    jogador é a soma de todos os dados lançados até agora. O 
    o primeiro jogador a atingir uma pontuação de 30 ou mais ganha!!! 
    O número total de rodadas jogadas também é rastreado.
""")

welcome_label = tk.Label(root, text=welcome_message, justify=tk.LEFT, bg="pink")
welcome_label.pack(pady=10)

username_label = tk.Label(root, text="Qual o seu nome?", bg="pink")
username_label.pack()

username = tk.Entry(root)
username.pack(pady=5)

roll_button = tk.Button(root, text="Role o dado!", command=roll_dice)
roll_button.pack(pady=10)

player_roll_label = tk.Label(root, text="", bg="pink")
player_roll_label.pack()

computer_roll_label = tk.Label(root, text="", bg="pink")
computer_roll_label.pack()

result_label = tk.Label(root, text="", bg="pink")
result_label.pack(pady=10)

scoreboard = tk.Text(root, height=10, width=30, state=tk.DISABLED, font=(1))
scoreboard.pack()

player_score = 0
computer_score = 0
rounds_played = 0

root.mainloop()
