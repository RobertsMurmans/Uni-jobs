import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.title("Function, with 2 inputs")
window.geometry("720x420")

st1 = ttk.Label(window, text="x= ")
st1.place(x=20,y=20)
st2 = ttk.Label(window, text="y= ")
st2.place(x=20,y=50)

in1 = ttk.Entry(window)
in1.place(x=50,y=20)
in2 = ttk.Entry(window)
in2.place(x=50,y=50)

st3 = ttk.Label(window, text="F(x,y)= ")
st3.place(x=20,y=110)
rez = ttk.Label(window, text="")
rez.place(x=50,y=110)

def showRezults():
    try:
        x = float(in1.get())
        y = float(in2.get())

        z = math.log2(1+math.cbrt(x**2)+math.sin(y))/(abs(x-y)+1)

        rez.config(text=str(z))

    except:
        print("netika ievadti skaitli")
        rez.config(text="Nav ievadits skaitlis")

btn1 = ttk.Button(window, text = "Rezultāts", width = 10, command=showRezults)
btn1.place(x=50,y=80)

btn2 = ttk.Button(window, text = "Beigt darbu", command=window.quit)
btn2.place(x=620,y=380)

window.mainloop()