from TrabajoConJson import ExtraerJson, js
from TrabajoConDateTime import ManejoDeTiempo
import datetime
import calendar

class RequisitosDeEventos:

   def Entrada( lista_con_eventos:list[list]):
      validos = []
      invalidos = []
      if type(lista_con_eventos)==list:
         for x in lista_con_eventos:
            print(x)
            for y in x[2]: 
               model= x[:]
               model[2] = y
               condicion = RequisitosDeEventos.Validacion(model)
               if condicion==None:
                  validos.append(model)
               else:
                  invalidos.append([model,condicion[1]])   

         for x in invalidos:
            RequisitosDeEventos.Validar(x)
      return(f"{validos}\n\n{invalidos}")


   def Validar(eventos_inv:list):
      evento = eventos_inv[0]
      if type(eventos_inv)==list:
         b= eventos_inv[:]
         horaA1 = eventos_inv[0][1];dateB1 = (eventos_inv[0][2],eventos_inv[0][3],eventos_inv[0][4])
         horaB1 = eventos_inv[1][1];dateB1 = (eventos_inv[1][2],eventos_inv[1][3],eventos_inv[1][4])
         
         hora= ManejoDeTiempo.Hora(horaA1,horaB1,0)
         
         duracion = hora[1]-hora[0]
         p =duracion+hora[2]
       
         if(p).time() <= hora[1].time():
             new_day = b[0][2]
             new_month = b[0][3]
             new_year = b[0][4]
             limite = calendar.monthrange(month=new_month,year=new_year)[1]
             if new_day == limite:
                if new_month == 12:
                   new_day = 1; new_month = 1; new_year+=1
                else:
                   new_day= 1; new_month+=1
             else: new_day+=1      
             b[0][2]= new_day;b[0][3]=new_month;b[0][4]=new_year
             hora_final = datetime.datetime.strptime("03:00", '%H:%M')
             hora_final=(hora_final+duracion).time()
             hora_final = "03:00 a "+ f"{hora_final.hour}:0{hora_final.minute}" if hora_final.minute==0 else f"{hora_final.hour}:{hora_final.minute}"
             b[0][1] = hora_final
             condicion = RequisitosDeEventos.Validacion(b[0])
             
             if condicion == None:
              
               evento = b[0]

             else:
               RequisitosDeEventos.Validar([b[0],condicion[1]])   
        
     
         else: 
            horita = f"{horaB1[8:]} a "+ f"{p.hour}:0{p.minute}" if p.minute==0 else f"{p.hour}:{p.minute}"
            b[0][1] = horita
            condicion = RequisitosDeEventos.Validacion(b[0])
      
            if condicion == None:
            
              evento = b[0]
             
            else:
               RequisitosDeEventos.Validar([b[0],condicion[1]])   
      


   def Validacion(evento_nuevo:list):
       eventos_ocurriendo = ExtraerJson.Extraer("EventosEjec.json")
       eventos_ocurriendoL = eventos_ocurriendo["Eventos en ejecucion"]
       if type(evento_nuevo)==list:
         x = evento_nuevo
        
         if str(x[4]) in eventos_ocurriendoL :
            if str(x[3]) in eventos_ocurriendoL[str(x[4])]:
              listaComparar=[ eventos_ocurriendoL[str(x[4])][str(x[3])]]
         
              if RequisitosDeEventos.Comparador(x,listaComparar) == None:
               if x in eventos_ocurriendoL[str(x[4])][str(x[3])]:
                 return (False,x)
               else:
                  print(f"LLEGO {x} ")
                  eventos_ocurriendoL[str(x[4])][str(x[3])].append(x)
                  eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
                  ExtraerJson.Escribir("EventosEjec.json",eventos_ocurriendo)    
                      
              else:return RequisitosDeEventos.Comparador(x,listaComparar)
                
            else:
             eventos_ocurriendoL[str(x[4])][str(x[3])]=x
             eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
             ExtraerJson.Escribir("EventosEjec.json",eventos_ocurriendo)    
         else:
            eventos_ocurriendoL[str(x[4])][str(x[3])]=x      
            eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
            ExtraerJson.Escribir("EventosEjec.json",eventos_ocurriendo)    

   def Comparador(listaRevisar ,listaComparar):
       x = listaRevisar
         
       for y in listaComparar: 
                 a1 = x[2];a2 = y[2]
                 print(a1,a2)
                 if a1==a2:
                     if ManejoDeTiempo.Hora(x[1],y[1]) == False:           
                           if x[6] == y[6]:
                                 return (False,y)
                           a3 = x[7];a4 = y[7]
                           if a3>=a4:
                                 for i in a4:
                                      if i in a3:
                                        return (False,y)
                                      else: continue
                           elif  a3<a4:
                                  for j in a3:
                                    if j in a4:
                                      return (False,y)
                                    else: continue                         

