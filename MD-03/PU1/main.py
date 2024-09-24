import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("Eur<=>USD")
window.geometry("720x420")



in1 = ttk.Entry(window)
in1.place(x=20,y=20)

st1 = ttk.Label(window, text="Eur")
st1.place(x=150,y=20)

out1 = ttk.Label(window, text="")
out1.place(x=240,y=20)

st2 = ttk.Label(window, text="USD")
st2.place(x=210,y=20)

def convertEur():
    try:
        eur = float(in1.get())
        usd = eur * 1.12
        out1.config(text=str(usd))

    except:
        print("error")
        out1.config(text=str(""))

btn1 = ttk.Button(window, text = "=", width = 1, command=convertEur)
btn1.place(x=180,y=20)



in2 = ttk.Entry(window)
in2.place(x=20,y=50)

st3 = ttk.Label(window, text="USD")
st3.place(x=150,y=50)

out2 = ttk.Label(window, text="")
out2.place(x=240,y=50)

st4 = ttk.Label(window, text="Eur")
st4.place(x=210,y=50)

def convertUSD():
    try:
        usd = float(in2.get())
        eur = usd * 0.9
        out2.config(text=str(eur))

    except:
        print("error")
        out2.config(text=str(""))

btn2 = ttk.Button(window, text = "=", width = 1, command=convertUSD)
btn2.place(x=180,y=50)



btn3 = ttk.Button(window, text = "Beigt darbu", command=window.quit)
btn3.place(x=620,y=380)

window.mainloop()