import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Dambrete")
window.geometry("720x920")

canva = tk.Canvas(window, height=512, width= 512, highlightthickness=5, highlightbackground="gray")
canva.place(x=103, y=103)

#Izveido kaulinu
def kaulins(x,y,krasa):
    canva.create_oval(x*64+8+5,y*64+8+5,x*64+56+5,y*64+56+5, fill=krasa)
    canva.create_oval(x*64+16+5,y*64+16+5,x*64+48+5,y*64+48+5, outline="gray")
    canva.create_oval(x*64+22+5,y*64+22+5,x*64+42+5,y*64+42+5, outline="gray")

#Izveido bambretes galdu
def galds():
    for x in range(0,8,1):
        for y in range(0,8,1):
            if (x+y)%2:
                canva.create_rectangle(64*x+5, 64*y+5, 64*(x+1)+5,64*(y+1)+5, fill="gray")
                if y < 3:
                    kaulins(x,y,"red")
                if y > 4:
                    kaulins(x,y,"white")

for x in range(1,9):
    text = tk.Label(text=str(x), font=("Times", "24", "bold"))
    text.place(x=x*64+63, y=43)

for y in range(1,9):
    text = tk.Label(text=str(y), font=("Times", "24", "bold"))
    text.place(x=53, y=y*64+53)

def move(x1,y1,x2,y2):
    canva.create_rectangle(64*x1+5, 64*y1+5, 64*(x1+1)+5,64*(y1+1)+5, fill="gray")
    kaulins(x2,y2,"white")

def show():
    galds()
    a = no.get()
    b = uz.get()
    print(a[1] , b[1])
    if a[1] == "6" and b[1] == "5":
        match a[0]:
            case "1":
                if b[0] == "2":
                    move(0,5,1,4)
                    error.config(text="")
                else:
                    error.config(text="Nepareizi ievadits gajiens")
            case "3":
                if b[0] == "2":
                    move(2,5,1,4)
                    error.config(text="")
                elif b[0] == "4":
                    move(2,5,3,4)
                    error.config(text="")
                else:
                    error.config(text="Nepareizi ievadits gajiens")
            case "5":
                if b[0] == "6":
                    move(4,5,5,4)
                    error.config(text="")
                elif b[0] == "4":
                    move(4,5,3,4)
                    error.config(text="")
                else:
                    error.config(text="Nepareizi ievadits gajiens")
            case "7":
                if b[0] == "6":
                    move(6,5,5,4)
                    error.config(text="")
                elif b[0] == "8":
                    move(6,5,7,4)
                    error.config(text="")
                else:
                    error.config(text="Nepareizi ievadits gajiens")
            case _:
                error.config(text="Nepareizi ievadits gajiens")
    else:
        error.config(text="Nepareizi ievadits gajiens")


no = tk.Entry(width=4)
uz = tk.Entry(width=4)

no.place(x=120,y=720)
tk.Label(text="uz").place(x=170,y=720)
uz.place(x=200,y=720)

tk.Button(text="Paradit", command=show).place(x=250,y=720)

error = tk.Label(text="")
error.place(x=120,y=820)

window.mainloop()