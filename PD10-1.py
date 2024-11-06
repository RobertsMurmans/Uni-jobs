import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Dambrete")
window.geometry("720x720")
window.configure(background="gray")

canva = tk.Canvas(window, height=512, width= 512)
canva.place(x=103, y=103)

#Izveido kaulinu
def kaulins(x,y,krasa):
    canva.create_oval(x*64+8,y*64+8,x*64+56,y*64+56, fill=krasa)
    canva.create_oval(x*64+16,y*64+16,x*64+48,y*64+48, outline="gray")
    canva.create_oval(x*64+22,y*64+22,x*64+42,y*64+42, outline="gray")

#Izveido bambretes galdu
for x in range(0,8,1):
    for y in range(0,8,1):
        if (x+y)%2:
            square = canva.create_rectangle(64*x, 64*y, 64*(x+1),64*(y+1), fill="gray")
            if y < 3:
                kaulins(x,y,"red")
            if y > 4:
                kaulins(x,y,"white")

window.mainloop()