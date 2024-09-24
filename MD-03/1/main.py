import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Functions between 2 numbers")
window.geometry("720x420")

st1 = ttk.Label(window, text="x= ")
st1.place(x=20,y=20)
st1 = ttk.Label(window, text="y= ")
st1.place(x=20,y=50)

in1 = ttk.Entry(window)
in1.place(x=50,y=20)
in2 = ttk.Entry(window)
in2.place(x=50,y=50)


st3 = ttk.Label(window, text="Summa= ")
st3.place(x=20,y=110)
st4 = ttk.Label(window, text="Starpība= ")
st4.place(x=20,y=140)
st5 = ttk.Label(window, text="Reizinājums= ")
st5.place(x=20,y=170)
st6 = ttk.Label(window, text="Dalījums= ")
st6.place(x=20,y=200)
st7 = ttk.Label(window, text="Veselais dalījums= ")
st7.place(x=20,y=230)
st8 = ttk.Label(window, text="Dalīšanas atlikums= ")
st8.place(x=20,y=260)

outSum = ttk.Label(window, text="")
outSum.place(x=150,y=110)
outDif = ttk.Label(window, text="")
outDif.place(x=150,y=140)
outMult = ttk.Label(window, text="")
outMult.place(x=150,y=170)
outDiv = ttk.Label(window, text="")
outDiv.place(x=150,y=200)
outWDiv = ttk.Label(window, text="")
outWDiv.place(x=150,y=230)
outRem = ttk.Label(window, text="")
outRem.place(x=150,y=260)

def showRezults():
    try:
        x = float(in1.get())
        y = float(in2.get())

        outSum.config(text = str(x+y))
        outDif.config(text = str(x-y))
        outMult.config(text = str(x*y))
        if y != 0:
            outDiv.config(text = str(x/y))
            outWDiv.config(text = str(x//y))
            outRem.config(text = str(x%y))
        else:
            outDiv.config(text = "NaN")
            outWDiv.config(text = "NaN")
            outRem.config(text = "NaN")

    except ValueError:
        print("netika ievadīti skaitļi")
    
    in1.delete(0, "end")
    in2.delete(0, "end")

btn1 = ttk.Button(window, text = "Rezultāts", width = 10, command=showRezults)
btn1.place(x=50,y=80)

btn2 = ttk.Button(window, text = "Beigt darbu", command=window.quit)
btn2.place(x=620,y=380)

window.mainloop()