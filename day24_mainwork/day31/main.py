from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=800)
card_front_img= PhotoImage(file="images/card_front.png")
canvas.create_image(400,283,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0,column=0)

window.mainloop()