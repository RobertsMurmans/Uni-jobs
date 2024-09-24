import tkinter as tk
from tkinter import ttk
import math

window = tk.Tk()
window.title("Triangle calck")
window.geometry("720x720")

st1x = ttk.Label(window, text="AB= ")
st1x.place(x=20,y=20)
st2x = ttk.Label(window, text="BC= ")
st2x.place(x=20,y=50)
st3x = ttk.Label(window, text="AC= ")
st3x.place(x=20,y=80)

in1 = ttk.Entry(window)
in1.place(x=100,y=20)
in2 = ttk.Entry(window)
in2.place(x=100,y=50)
in3 = ttk.Entry(window)
in3.place(x=100,y=80)

rez1st = ttk.Label(window, text="Perimetrs= ")
rez1st.place(x=20,y=110)
rez2st = ttk.Label(window, text="Laukums= ")
rez2st.place(x=20,y=140)
rez3st = ttk.Label(window, text="Apvilktais r= ")
rez3st.place(x=20,y=170)
rez3st = ttk.Label(window, text="Ievilktais r= ")
rez3st.place(x=20,y=200)


rez1 = ttk.Label(window, text="")
rez1.place(x=100,y=110)
rez2 = ttk.Label(window, text="")
rez2.place(x=100,y=140)
rez3 = ttk.Label(window, text="")
rez3.place(x=100,y=170)
rez4 = ttk.Label(window, text="")
rez4.place(x=100,y=200)


def showRezults():
    try:
        ab = float(in1.get())
        bc = float(in2.get())
        ac = float(in3.get())

        if ab + bc > ac or ab + ac > bc or bc + ac > ab:
            perim = ab+bc+ac
            semi = perim/2
            area = math.sqrt(semi * (semi - ab) * (semi - bc) * (semi - ac))
            outr = ab*bc*ac/(4*area)
            inr = area/semi
            rez1.config(text=str(perim))
            rez2.config(text=str(area))
            rez3.config(text=str(outr))
            rez4.config(text=str(inr))
        else:
            rez1.config(text=str("Nav trijsturis"))
            rez2.config(text=str(""))
            rez3.config(text=str(""))
            rez4.config(text=str(""))

    except:
        print()
        print("netika ievadti skaitli")
        rez1.config(text=str("Nav skaitli"))
        rez2.config(text=str(""))
        rez3.config(text=str(""))
        rez4.config(text=str(""))

btn1 = ttk.Button(window, text = "Rezultāts", width = 10, command=showRezults)
btn1.place(x=20,y=230)

btn2 = ttk.Button(window, text = "Beigt darbu", command=window.quit)
btn2.place(x=620,y=680)

window.mainloop()