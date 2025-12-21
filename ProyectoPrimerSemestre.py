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

   def Validacion(evento_nuevo:list):
       #La idea es que paso por cada lista del json, y tendra adentro una cantidad al menos 5 de trues en correspondencia con valores posibles
# Luego paso un nuevo evento, ese evento nuevo pasara por cada valor del json, y si me coinciden por ejemplo el tiempo y la clase, no pueden coincidir ni profes, ni aula, ni grupo
#Si coincide algo lo pone como false, menos en la fecha hora y evento, porque esos elementos pueden ser simultaneos, pero si esos lo son, los demas no
      lista_con_eventos =[]
      json = ExtraerJson.Extraer("EventosEjec.json")
      for i in range(len(json["Eventos en ejecucion"])):
         lista_con_eventos.append(json["Eventos en ejecucion"][i])    
      
      for eventos in lista_con_eventos:
         if len(eventos) == len(evento_nuevo):
          #Si coinciden estos valores con false, significa que tienen igual hora y mes, sigue revisando adentro, si no, el evento es valido con este evento     
          if (ManejoDeTiempo.Meses(eventos[2],evento_nuevo[2]))== False :
             if ManejoDeTiempo.Dias(eventos[1],evento_nuevo[1]) == False:
                if  ManejoDeTiempo.Hora(eventos[0],evento_nuevo[0]) == False:
                  
                      if eventos[4] == evento_nuevo[4] or eventos[5] == evento_nuevo[5] or eventos[6] == evento_nuevo[6]:
                        return False
                 
                else: continue
             else: continue
          else: continue  
           # Aqui debo anadir el caso con uno mayor que el otro, en ambos sentidos, la idea es que si uno es mayor
            # Digamos que A y B, Aevento , A>B, ahi comparo A los elementos iguales de A y los de B, osea los 7 primeros, lugo los otros
            # Como no chocan, no afectan
            # En el caso contrario, B>A
         elif (len(eventos) > len(evento_nuevo)):
            eventos_plus = eventos[7: len(eventos)]
            evento_nuevo_plus = evento_nuevo[7: len(evento_nuevo)]
            for items in evento_nuevo_plus:
               if items in eventos_plus:
                 val = False
                                   
class ManejoDeTiempo:

   def Hora(hora1, hora2):
    #Defino las horas en que ocurre el evento 1  
    hora_de_evento1 = hora1.split(" a ")
    hora_inicial_de_1 = datetime.datetime.strptime(hora_de_evento1[0], '%H:%M')
    hora_final_de_1 = datetime.datetime.strptime(hora_de_evento1[1], '%H:%M')

    hora_inicial_de_1 = hora_inicial_de_1.time()
    hora_final_de_1 = hora_final_de_1.time()
    #Defino las horas que ocuree el evento 2
    hora_de_evento2 = hora2.split(" a ")
    hora_inicial_de_2 = datetime.datetime.strptime(hora_de_evento2[0], '%H:%M')
    hora_final_de_2 = datetime.datetime.strptime(hora_de_evento2[1], '%H:%M')

    hora_inicial_de_2 = hora_inicial_de_2.time()
    hora_final_de_2 = hora_final_de_2.time()
    #Declara si una fecha es valida, revisando si el valor final 1 se encuentra entre el inicial o final de 2, o viceversa:
    if hora_final_de_1 <= hora_final_de_2 and hora_final_de_1 >= hora_inicial_de_1:
       return False
    elif hora_final_de_2 <= hora_final_de_1 and hora_final_de_2 >= hora_inicial_de_1:
     return False
    else: return True
    #La idea es que si me devuelve false, entonces las horas coinciden, sin importar que sean validas o no, eso lo valida la otra funcion 
    #cuando compare  hora, eventos, profe, aula, y grupo
      
   def Dias(dia1, dia2):
      if dia1 == dia2:
         return False     
      else: 
         return True
      
   def Meses(mes1, mes2):
      if mes1 == mes2:
         return False     
      else: 
         return True   
      #La funcion comparara si los dias y meses son iguales, si lo son devuelve True, sino Flase.

# ["9:00 a 10:30", "1", "4", "Clase Teorica Analisis", "Idania", "C121", "Aula 5"]
#horan = hora.ctime() #Me dice el dia, el mesy la hora del datetime
rooto = tk.Tk()
r1 = Visual1(rooto)
r2 = TrabajoDeEventos()
rooto.mainloop()
