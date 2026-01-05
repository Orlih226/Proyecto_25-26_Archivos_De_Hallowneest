import datetime       

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
