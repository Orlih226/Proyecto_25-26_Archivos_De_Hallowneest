import json as js
from tkcalendar import Calendar
import tkinter as tk
import sys

class Visual:
  root = tk.Tk()
  cal = Calendar(root, selectmode='day', year=2025, month=10, day=13)
  label2 = tk.Label(root, text= "Aqui tienes los eventos del dia", font="Sans", bg="light grey")
  label1 = tk.Label(root, text=" Aqui estan los detalles de evento", font="Sans", bg = "light grey")
  text1 = tk.Text(root, wrap="word", height=10, bg="light grey")
  text2 = tk.Text(root, wrap="word", height=15,bg="light grey")

  def MostrarGrafica(self): 
   # Crear ventana principal
   self.root.config(bg="grey")
   self.root.title("Gestor de Eventos")
   self.root.geometry("1200x800")
   # Configurar el grid
   self.root.columnconfigure(0, weight=1)
   self.root.columnconfigure(1, weight=1)
   self.root.rowconfigure(0, weight=1)
   self.root.rowconfigure(1, weight=1)
   # Calendario en la celda (0, 0)
   self.cal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
   #Label para decir que son los eventos en ese dia
   self.label2.grid(row = 0, column=1, sticky="n")
   # Bloque de texto 1 en la celda (0, 1)
   self.text1.insert("1.0", "")
   self.text1.config(height= 20)
   self.text1.grid(row=0, column=1,sticky="")
   #Label para decir que son la descripcion de eventos
   self.label1.grid(row = 1, column=1, sticky="n")
   # Bloque de texto 2 en la celda (1, 0) con colspan
   self.text2.insert("1.0", " ")
   self.text2.grid(row=1, column=1, columnspan=1, sticky="")
   # Ejecutar la aplicación
   self.root.mainloop()

  def ListarEventos(self,json):
        for x in range(len(json["Eventos en ejecucion"])):
           self.text1.insert("1.0",f"{json["Eventos en ejecucion"][x]}\n")
  def VerDetallesEvento(self,json, numero):
           self.text2.insert("1.0",f"El evento es:{json["Eventos en ejecucion"][numero][0]}\n Es de: {json["Eventos en ejecucion"][numero][3]} \n Con la profe:{json["Eventos en ejecucion"][numero][4]} \n El grupo: {json["Eventos en ejecucion"][numero][5]} \n En el aula: {json["Eventos en ejecucion"][numero][6]}")

class TrabajoDeEventos:
   
    def EliminarEvento(evento):
        pass
    def AgregarEvento(evento):
        pass
   
class ExtraerJson:
   def Extraer(archivo):
     with open(archivo) as json_file:
         json = js.load(json_file)
     return json

class RequisitosDeEventos:
    def algo():
        pass

#ri = ExtraerJson()
#profes = ri.ExtraerProfes("Profesores.json")
#print(profes['Profesores'][1])
eventosej = ExtraerJson.Extraer("EventosEjec.json")
r1 = Visual()
r1.VerDetallesEvento(eventosej,1)
r1.MostrarGrafica()

