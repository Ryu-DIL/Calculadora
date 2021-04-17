import tkinter as tk
import tkinter.font as font
from fractions import Fraction

Igualado = True
Aguantar = 0

def Ultima_Operacion(Pantalla):
	actual = Lector_Estatico.get()
	abajo = Lector_Dinamico.get()

	if actual != "" and str(actual[len(actual)-1]) in ("+", "-", "/", "*") and str(abajo[0]) in ("+", "-", "/", "*"):
		Lector_Estatico.delete(0, "end")
		Lector_Estatico.insert(0, actual[:-1])

def Entero(Numero):
	if Numero%1 == 0:
		return int(Numero)
	return Numero

def Click(Pantalla, numero):
	global Igualado
	global Aguantar
	
	if Igualado:
		Lector_Dinamico.delete(0, "end")
		Lector_Estatico.delete(0, "end")
	
	if numero == "(":
		Aguantar += 1
	elif numero == ")":
		Aguantar -= 1
	actual = Lector_Dinamico.get()
	Lector_Dinamico.delete(0, "end")
	Lector_Dinamico.insert(0, str(actual)+str(numero))
	
	Igualado = False
	
def Subir(Pantalla, cadena):
	actual = Lector_Estatico.get()
	Lector_Estatico.delete(0, "end")
	Lector_Estatico.insert(0, str(actual)+cadena)

def Borrar(Pantalla):
	global Igualado

	if Igualado:
		Lector_Dinamico.delete(0, "end")
		Lector_Estatico.delete(0, "end")
		return
	actual = Lector_Dinamico.get()
	Lector_Dinamico.delete(0, "end")

	Lector_Dinamico.insert(0, actual[:-1])

	Igualado = False
	
def Limpiar(Pantalla):
	global Igualado
	Lector_Dinamico.delete(0, "end")
	Lector_Estatico.delete(0, "end")

	Igualado = False
	
def Operacion(Pantalla, operando):
	global Igualado
	global Aguantar
	
	if Igualado:
		Lector_Estatico.delete(0, "end")
	
	if Aguantar == 0:
		Ultima_Operacion(Pantalla)
		actual = Lector_Dinamico.get()
		Lector_Dinamico.delete(0, "end")
		Subir(Pantalla, str(actual)+operando)
		Igualado = False
		return
	
	Click(Pantalla, operando)

def Igual_Clasico(Pantalla):
	actual = Lector_Dinamico.get()
	Lector_Dinamico.delete(0, "end")

	Subir(Pantalla, str(actual))
	try:
		Resultado = eval(Lector_Estatico.get())
		Resultado = Entero(Resultado)
	except:
		Resultado = "Syntax Error 1"
	Lector_Dinamico.insert(0, str(Resultado))

def Igual(Pantalla):
	global Igualado
	try:
		if(str(eval(Lector_Estatico.get())) == str(Lector_Dinamico.get())):
			Lector_Estatico.delete(0, "end")
			Igual_Clasico(Pantalla)
		else:
			Lector_Estatico.delete(0, "end")
			Lector_Estatico.insert(0, "Syntax Error 2")
			Lector_Dinamico.delete(0, "end")
			Lector_Dinamico.insert(0, "Syntax Error 2")
	except:
		Igual_Clasico(Pantalla)

	Igualado = True

def S_D(Pantalla):
	global Igualado
	if Igualado == False:
		Igual(Pantalla)
	Dec = Lector_Dinamico.get()
	Lector_Dinamico.delete(0, "end")
	Lector_Estatico.delete(0, "end")
	Lector_Estatico.insert(0, Dec)
	try:
		Lector_Dinamico.insert(0, Fraction(float(Dec)).limit_denominator())
	except:
		Lector_Dinamico.insert(0, "")
	Igualado = True

if __name__ == "__main__":
	Pantalla = tk.Tk()
	Pantalla.title("Calculadora sencilla")
	Pantalla.configure(bg="black")
	Pantalla.geometry("400x420")
	

	#Definimos el grid para redimensionar la ventana para cada fila y columna
	for i in range(7):
		tk.Grid.rowconfigure(Pantalla,i,weight=1)
	
	tk.Grid.columnconfigure(Pantalla,0,weight=2)
	tk.Grid.columnconfigure(Pantalla,1,weight=2)
	tk.Grid.columnconfigure(Pantalla,2,weight=1)
	tk.Grid.columnconfigure(Pantalla,3,weight=1)
	tk.Grid.columnconfigure(Pantalla,4,weight=2)


	#Definimos los botones y el lector de texto superior
	Tamanio_Negrita = font.Font(size = 20, weight = "bold")
	Lector_Estatico = tk.Entry(Pantalla, width = 30, borderwidth = 5, fg='white', bg='black', font = Tamanio_Negrita)
	Lector_Dinamico = tk.Entry(Pantalla, width = 30, borderwidth = 5, fg='white', bg='black', font = Tamanio_Negrita)
	Lector_Estatico.bind("<Key>", lambda e: "break")
	Lector_Dinamico.bind("<Key>", lambda e: "break")

	
	Boton_1 = tk.Button(Pantalla, text = "1", command = lambda: Click(Pantalla, "1"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_2 = tk.Button(Pantalla, text = "2", command = lambda: Click(Pantalla, "2"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_3 = tk.Button(Pantalla, text = "3", command = lambda: Click(Pantalla, "3"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_4 = tk.Button(Pantalla, text = "4", command = lambda: Click(Pantalla, "4"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_5 = tk.Button(Pantalla, text = "5", command = lambda: Click(Pantalla, "5"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_6 = tk.Button(Pantalla, text = "6", command = lambda: Click(Pantalla, "6"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_7 = tk.Button(Pantalla, text = "7", command = lambda: Click(Pantalla, "7"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_8 = tk.Button(Pantalla, text = "8", command = lambda: Click(Pantalla, "8"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_9 = tk.Button(Pantalla, text = "9", command = lambda: Click(Pantalla, "9"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_0 = tk.Button(Pantalla, text = "0", command = lambda: Click(Pantalla, "0"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Punto = tk.Button(Pantalla, text = ".", command = lambda: Click(Pantalla, "."), fg="white", bg="black", font = Tamanio_Negrita)

	Boton_ParIzq = tk.Button(Pantalla, text = "(", command = lambda: Click(Pantalla, "("), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_ParDer = tk.Button(Pantalla, text = ")", command = lambda: Click(Pantalla, ")"), fg="white", bg="black", font = Tamanio_Negrita)

	Boton_Sumar = tk.Button(Pantalla, text = "+", command = lambda: Operacion(Pantalla, "+"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Resta = tk.Button(Pantalla, text = "-", command = lambda: Operacion(Pantalla, "-"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Multi = tk.Button(Pantalla, text = "/", command = lambda: Operacion(Pantalla, "/"), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Divis = tk.Button(Pantalla, text = "*", command = lambda: Operacion(Pantalla, "*"), fg="white", bg="black", font = Tamanio_Negrita)

	Boton_Limpiar = tk.Button(Pantalla, text = "C", command = lambda: Limpiar(Pantalla), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Borrar  = tk.Button(Pantalla, text = "<--", command = lambda: Borrar(Pantalla), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_Igual   = tk.Button(Pantalla, text = "=", command = lambda: Igual(Pantalla), fg="white", bg="black", font = Tamanio_Negrita)
	Boton_S_D	  = tk.Button(Pantalla, text = "S/D", command = lambda: S_D(Pantalla), fg="white", bg="black", font = Tamanio_Negrita)
	
	#Colocamos los botones y el lector de texto superior en un grid en la pantalla
	
	Lector_Estatico.grid(row = 0, column = 0, columnspan = 5, pady = 20, sticky = "nsew")
	Lector_Dinamico.grid(row = 1, column = 0, columnspan = 5	, pady = 20, sticky = "nsew")

	Boton_1.grid(row = 5, column = 0, sticky = "nsew")
	Boton_2.grid(row = 5, column = 1, sticky = "nsew")
	Boton_3.grid(row = 5, column = 2, columnspan = 2, sticky = "nsew")
	
	Boton_4.grid(row = 4, column = 0, sticky = "nsew")
	Boton_5.grid(row = 4, column = 1, sticky = "nsew")
	Boton_6.grid(row = 4, column = 2, columnspan = 2, sticky = "nsew")
	
	Boton_7.grid(row = 3, column = 0, sticky = "nsew")
	Boton_8.grid(row = 3, column = 1, sticky = "nsew")
	Boton_9.grid(row = 3, column = 2, columnspan = 2, sticky = "nsew")

	Boton_0.grid(row = 6, column = 0, sticky = "nsew")
	Boton_Punto.grid(row = 6, column = 1, sticky = "nsew")

	Boton_ParIzq.grid(row = 2, column = 2, sticky = "nsew")
	Boton_ParDer.grid(row = 2, column = 3, sticky = "nsew")

	Boton_Sumar.grid(row = 5, column = 4, sticky = "nsew")
	Boton_Resta.grid(row = 4, column = 4, sticky = "nsew")
	Boton_Multi.grid(row = 3, column = 4, sticky = "nsew")
	Boton_Divis.grid(row = 2, column = 4, sticky = "nsew")

	Boton_Limpiar.grid(row = 2, column = 0, sticky = "nsew")
	Boton_Borrar.grid(row = 2, column = 1, sticky = "nsew")
	Boton_Igual.grid(row = 6, column = 4, sticky = "nsew")
	Boton_S_D.grid(row = 6, column = 2, columnspan = 2, sticky = "nsew")

	Pantalla.mainloop()