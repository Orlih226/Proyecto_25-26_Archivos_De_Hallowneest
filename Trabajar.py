from TrabajoConJson import ExtraerJson, js
from TrabajoConDateTime import ManejoDeTiempo
import datetime
import calendar

class RequisitosDeEventos:

   def Entrada( lista_con_eventos:list[list],json:dict):
      validos = []
      invalidos = []
      p =[]
      if type(lista_con_eventos)==list:
         for x in lista_con_eventos:
            for y in x[2]: 
               model= x[:]
               model[2] = y
               condicion = RequisitosDeEventos.Validacion(model,json)
               if type(condicion) == list:
                  validos.append(model)
               elif len(condicion)==1:
                  if model not in validos:
                   validos.append(model)
               elif type(condicion[0])==tuple:
                   invalidos.append([model,condicion[0][1]]) 
                   p.append(x)
      
      lista = invalidos[:]  
      validados = []          
      if len(lista)>0:
         for x in lista:
       #     print(condicion[1])
            b= RequisitosDeEventos.Validar(x,condicion[1])  
            if type(b) == list:
                validados.append(b[0]) 
      return(validos,p,validados),json
   
   def Validar(eventos_inv:list,json:dict):
      evento = eventos_inv[0]
      if type(eventos_inv)==list:
         b= eventos_inv[:]
       
        
         horaA1 = eventos_inv[0][1];dateB1 = (eventos_inv[0][2],eventos_inv[0][3],eventos_inv[0][4])
         horaB1 = eventos_inv[1][1];dateB1 = (eventos_inv[1][2],eventos_inv[1][3],eventos_inv[1][4])
         hora= ManejoDeTiempo.Hora(horaA1,horaB1,0)
         
         duracion = hora[1]-hora[0]
         p =duracion+hora[2]
         eventoR =[]
       
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

             hora= hora_final.hour
             minu = hora_final.minute  
             if len(f"{hora_final.hour}")==1:
                hora= f"0{hora}"
             horita = "03:00 a "+ f"{hora}:0{minu}" if len(f"{minu}")==1 else "03:00 a "+ f"{hora}:{minu}"
             b[0][1] = horita
             condicion = RequisitosDeEventos.Validacion(b[0],json)
             if type(condicion)==list:
               eventoR = condicion
             elif len(condicion) == 1:
               evento = b[0]
             else:
              b= RequisitosDeEventos.Validar([b[0],condicion[0][1]],condicion[1])   
              if type(b)==list:
                 eventoR=b
        
     
         else: 
            hora_final =f"{p.hour}"
            if len(f"{p.hour}")==1:
                hora_final = f"0{p.hour}" 
            horita = f"{horaB1[8:]} a "+ f"{hora_final}:0{p.minute}" if len(f"{p.minute}")==1 else f"{horaB1[8:]} a "+f"{hora_final}:{p.minute}"
            b[0][1] = horita
           
            condicion = RequisitosDeEventos.Validacion(b[0],json)
            if type(condicion)==list:
               eventoR = condicion
            elif len(condicion) == 1:
              evento = b[0] 
            else:
               b= RequisitosDeEventos.Validar([b[0],condicion[0][1]],condicion[1])      
               if type(b)==list:
                 eventoR=b   
         return eventoR   
      
   def Validacion(evento_nuevo:list,eventos_ocurriendo:dict):
       eventos_ocurriendoL = eventos_ocurriendo["Eventos en ejecucion"]
       if type(evento_nuevo)==list:
         x = evento_nuevo
        
         if str(x[4]) in eventos_ocurriendoL :
            if str(x[3]) in eventos_ocurriendoL[str(x[4])]:
              listaComparar=[ eventos_ocurriendoL[str(x[4])][str(x[3])]]
              if RequisitosDeEventos.Comparador(x,listaComparar) == None:
            
               if x in eventos_ocurriendoL[str(x[4])][str(x[3])]:
                 return ((False,x),eventos_ocurriendo)
               else:
                  eventos_ocurriendoL[str(x[4])][str(x[3])].append(x)
                  eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
                  return [x,eventos_ocurriendo]
                  
              else:return (RequisitosDeEventos.Comparador(x,listaComparar),eventos_ocurriendo)
                
            else:
             eventos_ocurriendoL[str(x[4])][str(x[3])]=[x]
             eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
             return [x,eventos_ocurriendo]
            
           
            
          #   ExtraerJson.Escribir("EventosEjec.json",eventos_ocurriendo)    
         else:
            eventos_ocurriendoL[str(x[4])]={}  
            eventos_ocurriendoL[str(x[4])][str(x[3])]=[x] 
            eventos_ocurriendo["Eventos en ejecucion"] = eventos_ocurriendoL
            return [x,eventos_ocurriendo]
           

          #  ExtraerJson.Escribir("EventosEjec.json",eventos_ocurriendo)    
       return eventos_ocurriendo    

   def Comparador(listaRevisar ,listaComparar):
       x = listaRevisar
       if len(listaComparar[0])>0:
        for y in listaComparar[0]: 
            if  y[-1]!=False:
                 a1 = x[2];a2 = y[2]
                 if a1==a2:
                     if ManejoDeTiempo.Hora(hora1=x[1],hora2=y[1],y=None) == False:           
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
            else:
               pass                                 


#json ={'Eventos en ejecucion': {'2025': {'1': [['asdda', '12:00 a 13:00', 1, 1, 2025, 'Construccion', 'Cruces Olvidados', ['Brigada de Construccion']]]}}}
#evento=[['asdda', '12:00 a 14:00', [1], 1, 2026, 'Construccion', 'Cruces Olvidados', ['Brigada de Construccion']],['asdda', '12:00 a 14:00', [1], 2, 2025, 'Construccion', 'Cruces Olvidados', ['Brigada de Construccion']]] 
#b=RequisitosDeEventos.Entrada(evento,json)
#print(b[1])  