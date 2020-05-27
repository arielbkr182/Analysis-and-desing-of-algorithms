from tkinter import *
raiz= Tk()
miframe=Frame(raiz, width=1200, height=600)
miframe.pack()

minombre=StringVar()
cuadroNombre=Entry(miframe, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadropass=Entry(miframe)
cuadropass.grid(row=1, column=1, padx=10)
cuadropass.config(show="?")

cuadroApellido=Entry(miframe)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroDireccion=Entry(miframe)
cuadroDireccion.grid(row=3, column=1, padx=10, pady=10)

textocomentario=Text(miframe, width=16, height=5)
textocomentario.grid(row=4, column=1, padx=10, pady=10)

scrollVert=Scrollbar(miframe, command=textocomentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

textocomentario.config(yscrollcommand=scrollVert.set)

nombreLabel=Label(miframe, text="Nombre: ")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miframe, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)


direccionLabel=Label(miframe, text="Direccion: ")
direccionLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miframe, text="password: ")
passLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

comentarioslabel=Label(miframe, text="comentarios: ")
comentarioslabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

def codigoBoton():
    minombre.set("juan")
botonenvio=Button(raiz, text="Enviar", command=codigoBoton)

raiz.mainloop()