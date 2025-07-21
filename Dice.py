import tkinter as tk
import random

root = tk.Tk()
root.geometry("350x420")
root.title("Rollify")
root.config(background="#C58047")

canvas = tk.Canvas(root, width=350, height=420, highlightthickness=0, bg="#C58047")
canvas.pack(fill="both", expand=True)

pip_positions = {
    "TL": (0.25, 0.25), "TR": (0.75, 0.25),
    "ML": (0.25, 0.50), "MR": (0.75, 0.50),
    "BL": (0.25, 0.75), "BR": (0.75, 0.75),
    "C": (0.50, 0.50)
}

dice_map = {
    1: ("C",),
    2: ("TL", "BR"),
    3: ("TL", "C", "BR"),
    4: ("TL", "TR", "BL", "BR"),
    5: ("TL", "TR", "C", "BL", "BR"),
    6: ("TL", "TR", "ML", "MR", "BL", "BR")
}

def draw_die(value):
    canvas.delete("dice")
    x0, y0, size = (105, 180, 140)
    x1, y1 = x0 + size, y0 + size
    canvas.create_rectangle(x0, y0, x1, y1, fill="white", outline="black", width=3, tags="dice")
    for key in dice_map[value]:
        fx, fy = pip_positions[key]
        cx, cy = x0 + fx * size, y0 + fy * size
        canvas.create_oval(cx - 10, cy - 10, cx + 10, cy + 10, fill="black", outline="black", tags="dice")

def roll():
    draw_die(random.randint(1, 6))

btn = tk.Button(root, text="Roll the dice", font=("Arial", 17), command=roll)
canvas.create_window(175, 83, window=btn)

root.mainloop()
