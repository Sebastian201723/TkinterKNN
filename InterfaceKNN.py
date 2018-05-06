#------------------------------------------
#Author: Sebastian Cajas Ordonez
#------------------------------------------
try: #Python 3
    from Tkinter import*
except ImportError: #Python2
    from tkinter import*
import tkMessageBox
from scipy.io import arff
import pandas as pd
import math
import operator
from Funcion_Knn import lectura
raiz = Tk()

raiz.title("KNN Method")
raiz.iconbitmap("selfi.ico")
raiz.geometry("700x700")
raiz.config(bg="blue")

Frame1 = Frame(raiz, width=480, height=1000)
Frame1.pack()

RtaLabel= Label(Frame1,text="Distancia Vecino Mas cercano es: ").place(x=100,y=600)
distanciaPantalla=StringVar(value="0")
distancia = Entry(Frame1,textvariable=distanciaPantalla)
distancia.place(x=100,y=650)
distancia.config(background="black",fg="#03f943", justify=CENTER)

#--------Funciones-----------------------
def help():
    tkMessageBox.showinfo("Help","Na: 0-1; K= 0-0.4")
def Guardar(Edad,Sexo, BP,Ch,Na,K,Vecinos):
    VEdad = int(Edad.get())
    VSexo = float(Sexo.get())
    VBP = float(BP.get())
    VCh = float(Ch.get())
    VNa = float(Na.get())
    VK = float(K.get())
    ValorVecinos = int(Vecinos.get())
    TestingData = [(VEdad-15)/59, VSexo, VBP, VCh,abs((VNa-0.5)/(0.5-0.896)) ,abs((VK-0.08)/(0.2-0.08))]
    Listas = lectura(Vecinos,TestingData)
    d = Listas[8]
    #Drug
    distanciaPantalla.set(str(d[0][1]))
    #print(d)
   
#---------Interaccion con usuario---------
Titulo = Label(Frame1,text="KNN Algorithm \n Sebastian Andres Cajas Ordonez \n Universidad del Cauca",font=("Arial",20),fg="brown",justify = CENTER).place(x=50,y=20)


EdadLabel = Label(Frame1,text="Edad:").place(x=100, y=200)
Edad = StringVar()
jtxtEdad = Entry(Frame1,textvariable=Edad).place(x=150,y=200)

SexoLabel = Label(Frame1,text="Sexo:").place(x=100, y=250)
Sexo = StringVar()
jtxtSexo = Entry(Frame1,textvariable=Sexo).place(x=150,y=250)

BPLabel = Label(Frame1,text="BP:").place(x=100, y=300)
BP = StringVar()
jtxtBP = Entry(Frame1,textvariable=BP).place(x=150,y=300)

ChLabel = Label(Frame1,text="Ch:").place(x=100, y=350)
Ch = StringVar()
jtxtCh = Entry(Frame1,textvariable=Ch).place(x=150,y=350)

NaLabel = Label(Frame1,text="Na:").place(x=100, y=400)
Na = StringVar()
jtxtNa = Entry(Frame1,textvariable=Na).place(x=150,y=400)

KLabel = Label(Frame1,text="K:").place(x=100, y=450)
K = StringVar()
jtxtK = Entry(Frame1,textvariable=K).place(x=150,y=450)

VecinosLabel = Label(Frame1,text="Vecinos:").place(x=100, y=500)
Vecinos =StringVar()
jtxtVecinos = Entry(Frame1,textvariable=Vecinos).place(x=150,y=500)
#jtxtVecinos.config(fg="brown",justify=CENTER,show="*")

Button(raiz,text="Guardar",command=lambda:Guardar(Edad,Sexo,BP,Ch,Na,K,Vecinos)).place(x=250,y=550)
Button(raiz,text="Ayuda",command=help).place(x=350,y=550)
Button(raiz,text="Salir",command=Frame1.quit).place(x=450,y=550)


raiz.mainloop()