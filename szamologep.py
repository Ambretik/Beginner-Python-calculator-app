import tkinter as tk
from tkinter import ttk

eredmeny = None
jel = ""
elsoszam= ""
masodszam = ""
utsogombnyomas = False  
ablak = tk.Tk()

#muveletek definialva vannak majd meghivasra kerulnek a gombnyomasoknal, a "jelek" dict segitsegevel
def osszead(a, b):
    return a + b

def kivon(a, b):
    return a - b

def szoroz(a, b):
    return a * b

def oszt(a, b):
    return a / b

def hatvanyoz(a, b):
    if a < 0 and not b.is_integer():
        raise ValueError("Negativ szamot nem lehet nem egesz hatvanyra emelni!")
    return a ** b 

jelek = {"+": osszead, "-": kivon, "*": szoroz, "/": oszt, "**": hatvanyoz}

def beir(szam):
    global utsogombnyomas
    if kijelzo.cget("text") == "Error!" or utsogombnyomas == True:
        kijelzo.configure(text="")
    old = kijelzo.cget("text")
    kijelzo.configure(text=str(old) + szam)
    utsogombnyomas = False


#ha van beriva szam, akkor a jelado fuggveny elmenti az elso szamot es a muveletet, majd torli a kijelzo tartalmat
def jelado(feladat):
    try:
        if kijelzo.cget("text") != "" and kijelzo.cget("text") != "Error!":
            global elsoszam
            global utsogombnyomas
            global jel  
            utsogombnyomas = False
            jel = feladat
            elsoszam = kijelzo.cget("text")
            return elsoszam and kijelzo.configure(text="") and jel
    except TypeError:kijelzo.configure(text="Error!")    
  
#argumentumkent fogadja a jelado altal visszaadott jel valtozot es jelek dict segitsegevel kiszamolja az eredmenyt, majd a kijelzo-n megjeleniti
def kiszamolas(jel):
    try:
        if elsoszam != 0:    
            if jel in jelek:
                global utsogombnyomas
                global eredmeny
                global masodszam
                if utsogombnyomas == False:
                    eredmeny = jelek[jel](float(elsoszam), float(kijelzo.cget("text")))
                    masodszam = kijelzo.cget("text")
                    utsogombnyomas = True
                    return kijelzo.configure(text=int(eredmeny) if eredmeny.is_integer() else round(eredmeny,3))
                else:
                    eredmeny = jelek[jel](float(eredmeny), float(masodszam))
                    return kijelzo.configure(text=int(eredmeny) if eredmeny.is_integer() else round(eredmeny, 3))
    except (ValueError, ZeroDivisionError, OverflowError):kijelzo.configure(text="Error!")
     

#kitolti a kijelzo tartalmat es az elsoszam valtozot is
def clear():
    kijelzo.configure(text="")
    global elsoszam
    global masodszam
    global jel
    global eredmeny
    global utsogombnyomas
    eredmeny = ""
    elsoszam = ""
    masodszam = ""
    jel = ""
    utsogombnyomas = False
     
szam0 = ttk.Button(text="0", command=lambda: beir("0"))
kijelzo = ttk.Label(text="", font=("Arial", 20))
szam1 = ttk.Button(text="1", command=lambda: beir("1"))
szam2 = ttk.Button(text="2", command=lambda: beir("2"))
szam3 = ttk.Button(text="3", command = lambda:beir("3"))
szam4 = ttk.Button(text="4", command = lambda:beir("4"))
szam5 = ttk.Button(text="5", command = lambda:beir("5"))
szam6 = ttk.Button(text="6", command = lambda:beir("6"))
szam7 = ttk.Button(text="7", command = lambda:beir("7"))
szam8 = ttk.Button(text="8", command = lambda:beir("8"))
szam9 = ttk.Button(text="9", command = lambda:beir("9"))
c = ttk.Button (text="C", command= lambda: clear())
osszeadg = ttk.Button(text="+", command= lambda:jelado("+"))
kivonas = ttk.Button(text="-", command=lambda: jelado("-"))
osztas = ttk.Button(text="%", command=lambda: jelado("/"))
szorzas = ttk.Button(text="*", command=lambda: jelado("*"))
egyenlo = ttk.Button(text="=", command = lambda: kiszamolas(jel))

kijelzo.grid(row=0,column=0, columnspan=4 )
szam0.grid(row=4, column=0)
szam1.grid(row=1, column=0)
szam2.grid(row=1, column=1) 
szam3.grid(row=1, column=2)
szam4.grid(row=2, column=0)
szam5.grid(row=2, column=1)
szam6.grid(row=2, column=2)
szam7.grid(row=3, column=0)
szam8.grid(row=3, column=1)
szam9.grid(row=3, column=2)
c.grid    (row=1, column=3)
osszeadg.grid(row=2, column=3)
kivonas.grid(row=3, column=3)
osztas.grid(row=4, column=2)
szorzas.grid(row=4, column=1)
egyenlo.grid(row=4, column=3)

style = ttk.Style()
style.configure("TButton", font=("Arial", 20), padding=5)

ablak.mainloop()