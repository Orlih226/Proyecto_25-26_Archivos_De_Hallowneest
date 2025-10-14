import tkinter as tk
from tkcalendar import Calendar

class Visual:
  def MostrarGrafica(): 
   # Crear ventana principal
   root = tk.Tk()
   root.config(bg="grey")
   root.title("Gestor de Eventos")
   root.geometry("1200x800")
   # Configurar el grid
   root.columnconfigure(0, weight=1)
   root.columnconfigure(1, weight=1)
   root.rowconfigure(0, weight=1)
   root.rowconfigure(1, weight=1)
   # Calendario en la celda (0, 0)
   cal = Calendar(root, selectmode='day', year=2025, month=10, day=13)
   cal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
   #Label para decir que son los eventos en ese dia
   label2 = tk.Label(root, text= "Aqui tienes los eventos del dia", font="Sans", bg="light grey")
   label2.grid(row = 0, column=1, sticky="n")
   # Bloque de texto 1 en la celda (0, 1)
   text1 = tk.Text(root, wrap="word", height=10, bg="light grey")
   text1.insert("1.0", "")
   text1.config(height= 20)
   text1.grid(row=0, column=1,sticky="")
   #Label para decir que son la descripcion de eventos
   label1 = tk.Label(root, text=" Aqui estan los detalles de evento", font="Sans", bg = "light grey")
   label1.grid(row = 1, column=1, sticky="n")
   # Bloque de texto 2 en la celda (1, 0) con colspan
   text2 = tk.Text(root, wrap="word", height=15,bg="light grey")
   text2.insert("1.0", " ")
   text2.grid(row=1, column=1, columnspan=1, sticky="")
   # Ejecutar la aplicación
   root.mainloop()



