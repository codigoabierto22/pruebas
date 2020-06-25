from tkinter import *


raiz=Tk()
raiz.title(" Calculadora de Eventos Greenticket")
raiz.resizable(0,0)   #para redimencionar la raiz  ancho y despues alto tipo booleano
raiz.geometry("450x600")  #tamaño por defecto
raiz.config(bg="gray")    #color de la raiz

def tarifa():
	monto=Label(miframe,text="Resultados:\n"+ cuadrodetexto.get())
	monto.grid(row=9, column=0,sticky="w", padx=20, pady=190)


miframe=Frame()
miframe.pack(fill="both", expand="true")
miframe.config(width="850", height="1200")
miframe.config(bg="white")


label=Label(miframe,text="Tarifa:")
label.grid(row=2, column=0,sticky="w", padx=20, pady=20)              #sticky  dentro del parametro .grid situa los label de texto con puntos cardinales ej:  n,s e,w en ingles

label2=Label(miframe,text="Porcentaje:")               # padx distancia izquierda    pady distancia arriba abajo igual poner en grid.
label2.grid(row=3, column=0, sticky="w",padx=20, pady=20)             #row y colum crea columnas empeizan desde cero ej: row 0.1.2  column 0,1,2

label3=Label(miframe,text="Total de asistentes:")
label3.grid(row=4, column=0,sticky="w",padx=20, pady=20)

#label4=Label(miframe,text="Contraseña:")
#label4.grid(row=3, column=0,sticky="w",padx=20, pady=20)



cuadrodetexto=Entry(miframe)
cuadrodetexto.grid(row=2, column=1,padx=10, pady=20)

cuadrodetexto2=Entry(miframe)
cuadrodetexto2.grid(row=3, column=1,padx=10, pady=20)

cuadrodetexto3=Entry(miframe)
cuadrodetexto3.grid(row=4, column=1,padx=10, pady=20)

#cuadrodetexto4=Entry(miframe)
#cuadrodetexto4.grid(row=3, column=1)
#cuadrodetexto4.config(show="*")

miimagen=PhotoImage(file="ggt44.png")
Label(miframe, image=miimagen).place(x=190, y=220)


boton=Button(text="Enviar", command = tarifa).place(x=220,y=350)



tarifa = cuadrodetexto
porcentaje = tarifa * input("Ingresa un porcentaje:")

print ("La comision de Greenticket es de: $"), porcentaje





raiz.mainloop()
