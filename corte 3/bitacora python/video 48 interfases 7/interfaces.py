from tkinter import *
raiz=Tk()
miframe=Frame(raiz)
miframe.pack()
#-----------------------pantalla---------------
numeropantalla=StringVar()
pantalla=Entry(miframe, textvariable=numeropantalla)
pantalla.grid(row=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="black", fg="#03f943", justify="right")
#---------------pulsaciones-----------------------
def numeropulsado(num):
    numeropantalla.set(numeropantalla.get() + num)
#--------------------fila 1--------------------
boton7=Button(miframe, text="7", width=3, command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=1)
boton8=Button(miframe, text="8", width=3, command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=2)
boton9=Button(miframe, text="9", width=3, command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=3)
botondiv=Button(miframe, text="/", width=3)
botondiv.grid(row=2, column=4)

#--------------------fila 2--------------------
boton4=Button(miframe, text="4", width=3, command=lambda:numeropulsado("4"))
boton4.grid(row=3, column=1)
boton5=Button(miframe, text="5", width=3, command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=2)
boton6=Button(miframe, text="6", width=3, command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=3)
botonmulti=Button(miframe, text="x", width=3)
botonmulti.grid(row=3, column=4)

#--------------------fila 3--------------------
boton1=Button(miframe, text="1", width=3, command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=1)
boton2=Button(miframe, text="2", width=3, command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=2)
boton3=Button(miframe, text="3", width=3, command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=3)
botonrest=Button(miframe, text="-", width=3)
botonrest.grid(row=4, column=4)

#--------------------fila 4--------------------
boton0=Button(miframe, text="0", width=3, command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=1)
botoncoma=Button(miframe, text=",", width=3, command=lambda:numeropulsado(","))
botoncoma.grid(row=5, column=2)
botonigual=Button(miframe, text="=", width=3, command=lambda:numeropulsado("="))
botonigual.grid(row=5, column=3)
botonsum=Button(miframe, text="+", width=3)
botonsum.grid(row=5, column=4)
raiz.mainloop()
