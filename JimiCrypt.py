import tkinter as tk
import random
norm = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "Ä", "Ö", "Å", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "ä", "ö", "å", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " ", ".", ",", "!", "?", "=", "+", "-", "*", ":", ";", "#", "(", ")", "[", "]", "{", "}", "{", "£", "$", "€", "&", "%", "¤", "@", "/", "_"]

top = tk.Tk()
top.geometry("400x250")
def tulostasekoitettu(seed, message):
    random.seed(seed)
    lause = ""
    sekoitettu = random.sample(norm, len(norm))
    for i in range(len(message)):
        lause += sekoitettu[norm.index(message[i])]
    E2.delete(0, tk.END)
    E2.insert(tk.END,lause)
def tulostaselvitetty(seed, message):
    random.seed(seed)
    lause = ""
    sekoitettu = random.sample(norm, len(norm))
    for i in range(len(message)):
        lause += norm[sekoitettu.index(message[i])]
    E1.delete(0, tk.END)
    E1.insert(tk.END,lause)
def tyhjenna():
    E1.delete(0, tk.END)
    E1.insert(tk.END,"Sekoitettava")
    E2.delete(0, tk.END)
    E2.insert(tk.END,"Sekoitettu")
    E3.delete(0, tk.END)
    E3.insert(tk.END,"Seed (salasana)")
def vie(a, b):
    vie = open(a,"w")
    vie.write(b)
def hae(a, b):
    hae = open(a,"r")
    tulos = hae.readlines()
    if b == 1:
        E1.delete(0, tk.END)
        E1.insert(tk.END, tulos[0])
    if b == 2:
        E2.delete(0, tk.END)
        E2.insert(tk.END, tulos[0])

E1 = tk.Entry(top, bd = 5,width = 50)
E1.place(x = 70, y = 10)
E1.insert(tk.END,"Sekoitettava")

E2 = tk.Entry(top, bd = 5, width = 50)
E2.place(x = 70, y = 110)
E2.insert(tk.END,"Sekoitettu")

E3 = tk.Entry(top, bd = 5, width = 50)
E3.place(x = 70, y = 60)
E3.insert(tk.END,"Seed (salasana)")

E4 = tk.Entry(top, bd = 5, width = 28)
E4.place(x = 10, y = 210)
E4.insert(tk.END,"Vietävän tiedoston nimi (.txt)")

E5 = tk.Entry(top, bd = 5, width = 28)
E5.place(x = 200, y = 210)
E5.insert(tk.END,"Haettavan tiedoston nimi (.txt)")

B1 = tk.Button(top, width = 5, text="Sekoita", command = lambda: tulostasekoitettu(E3.get(),E1.get()))
B1.place(x = 10, y = 10)

B2 = tk.Button(top, width = 5, text="Selvitä", command = lambda: tulostaselvitetty(E3.get(),E2.get()))
B2.place(x = 10, y = 110)

B3 = tk.Button(top, width = 5, text="Reset", command = tyhjenna())
B3.place(x = 10, y = 60)

B4 = tk.Button(top, width = 10, text="Vie 1", command = lambda: vie(E4.get(),E1.get()))
B4.place(x = 10, y = 160)

B5 = tk.Button(top, width = 10, text="Vie 2", command = lambda: vie(E4.get(),E2.get()))
B5.place(x = 105, y = 160)

B6 = tk.Button(top, width = 10, text="Hae 1", command = lambda: hae(E5.get(),1))
B6.place(x = 205, y = 160)

B7 = tk.Button(top, width = 10, text="Hae 2", command = lambda: hae(E5.get(),2))
B7.place(x = 300, y = 160)
    
tk.mainloop()