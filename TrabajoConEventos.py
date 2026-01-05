from TrabajoConJson import ExtraerJson, js
from TrabajoConDateTime import ManejoDeTiempo

class TrabajoDeEventos:
   #["Clase Teorica Analisis","1", "4", "9:00 a 10:30", "Idania", "C121", "Aula 5"], ["Clase Teorica Analisis","1", "4", "9:00 a 10:30", "Idania", "C121", "Aula 5"] 
    def EliminarEventos(self, numero_a_eliminar): #Este proyecto
     diccionario_nuevo_a_remplazar = ExtraerJson.Extraer("EventosEjec.json") 
     del diccionario_nuevo_a_remplazar["Eventos en ejecucion"][numero_a_eliminar]
     with open("EventosEjec.json","w") as file:
      js.dump(diccionario_nuevo_a_remplazar, file)
    
    def AgregarEvento(self,caracteristicas):#Puedo tirar *args para recibir una lista, que cumpla tales caracterisitcas
        json_viejo = ExtraerJson.Extraer("EventosEjec.json") #Crea un dict con el valor del json en ese camino
        evento_nuevo = caracteristicas #Es el evento nuevo, quitare *
        condicion = RequisitosDeEventos.Validacion(evento_nuevo)
      
        if(condicion == None):
         json_viejo["Eventos en ejecucion"].append(evento_nuevo) # LLamo a la posicion 0 del json esey le anado el evento nuevo
       
         ExtraerJson.Escribir("EventosEjec.json", json_viejo) #LLamo a la clase que llama al metodo, al dict que tiene el ditc viejo y el nuevo, reemplazara al json viejo
        else:
           print('NO se puede anadir')   


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