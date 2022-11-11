from tkinter import *
from tkinter import messagebox

def ejecutar():
    x=-int((m.get())*(m.get()+1))/2
    print("x="+str(X))      
    
    t_resultados.insert(INSERT, "El valor de es X = "+str(l)+"\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    m.set("")
    t_resultados.delete("1.0","end")

def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrara...")
    ventana_principal.destroy()

ventana_principal= Tk()
ventana_principal.title("sistema operativo")
ventana_principal.geometry("600x700")
ventana_principal.resizable(0,0)
ventana_principal.config(bg="white")

m = StringVar()

#grafica 
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="black",width=580, height=680)
frame_entrada.place(x=10,y=10)
frame_entrada1=Frame(ventana_principal)
frame_entrada1.config(bg="green2",width=570, height=180)
frame_entrada1.place(x=15,y=15)
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="black",width=570, height=10)
frame_entrada.place(x=15,y=190)

frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="green2",width=570, height=300)
frame_entrada.place(x=15,y=191)
frame_entrada=Frame(ventana_principal)
frame_entrada.config(bg="black",width=570, height=10)
frame_entrada.place(x=15,y=190)

titulo= Label (frame_entrada1, text= "Escriba m numero el hasta el cual")
titulo.config(bg="green2", fg="black", font=("Arial",16))
titulo.place(x=200,y=20)
titulo= Label (frame_entrada1, text= "se desea sumar")
titulo.config(bg="green2", fg="black", font=("Arial",16))
titulo.place(x=270,y=55)

logo = PhotoImage(file="dad/uis.png")
lb_logo = Label(frame_entrada1, image=logo)
lb_logo.place(x=15,y=15)

# Etiqueta para x
lb_m = Label(frame_entrada1, text = "m = ")
lb_m.config(bg="green2", fg="white", font=("Arial",16))
lb_m.place(x=250, y=100, width=115, height=30)

# Entry para x
entry_x = Entry(frame_entrada1, textvariable=m)
entry_x.config(font=("Arial",20), justify=LEFT,fg="black")
entry_x.focus_set()
entry_x.place(x=335, y=100, width=115, height=30)

#frame operaciones

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "green", width = 550 , height = 270)
frame_operaciones.place(x = 25, y = 210)

# Boton para ejecutar
bt_ejecutar = Button(frame_operaciones, text="Ejecutar", command=ejecutar)
bt_ejecutar.place(x=65, y=105, width=100, height=30)

#Boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar",command=borrar)
bt_borrar.place(x=225, y=105, width=100, height=30)

# Boton salir
bt_salir = Button(frame_operaciones, text="Salir",command=salir)
bt_salir.place(x=380, y=105, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=570, height=182)
frame_resultados.place(x=15, y = 500)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=550, height= 160)

# se ejecuta el metoo mainloop() de la clase Tk a traves de la instancia ventana_principal. este metodo despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc) cada accion del usuario se conoce cono un evento. El metodo mailooop  () es un bucle infinito.
ventana_principal.mainloop()
