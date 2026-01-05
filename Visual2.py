
import customtkinter as tk
import calendar
import tkinter 
from TrabajoConJson import ExtraerJson
from tkcalendar import Calendar
import datetime
from Trabajar import *

class SegundaVentana:
     def __init__(self, root:tk.CTk):
        self.root = root
        self.Interfaz()
     def Interfaz(self):
         #////////////////////////////////////////////////////////////// Crear ventana  //////////////////////////////////////////////////
        self.root.minsize(1200, 700)
        self.root.title("Gestor de Eventos")
        self.root.maxsize(1200,700)
 #///////////////////////////////////////// Objetos ventana Principal ///////////////////////////////////////////////
        self.eventosOcurriendo =[""]
        self.opciones=[]
        self.jsonEcj = ExtraerJson.Extraer("EventosEjec.json")
        self.interfaz1 = tk.CTkFrame(self.root)
        self.interfaz4 = tk.CTkFrame(self.root)
        self.interfaz3 = tk.CTkFrame(self.root)
        self.interfaz2 = tk.CTkFrame(self.root)
        self.frameM = tk.CTkFrame(self.interfaz1,width=405,height=660)
        self.label3 = tk.CTkLabel(self.interfaz1, text="Seleccione un fecha:",font=tk.CTkFont(family="bold",size=20),text_color="white",bg_color="transparent")
        self.frameCal = tk.CTkFrame(self.frameM,width=320,height=320)
        self.cal = Calendar(self.frameCal, selectmode='day', year=2025, month=10, day=13)
        self.label2 = tk.CTkLabel(self.interfaz1, text="Aqui tienes los eventos del dia")
        self.label1 = tk.CTkLabel(self.interfaz1, text=" Aqui estan los detalles de evento",font=tk.CTkFont(family="bold",size=20),text_color="lightblue")
        self.boton1 = tk.CTkButton(self.frameM,text="Crear evento",command=self.Crear)
        self.boton2 = tk.CTkButton(self.interfaz1,text="Salir", command= lambda: self.root.destroy())
        self.boton3 = tk.CTkButton(self.frameM,text="Configuracion")
        self.boton4 = tk.CTkButton(self.frameM,text="Inventario",command=self.Crear3)
        self.boton5 = tk.CTkButton(self.frameM,text="Restricciones")
        self.com = tk.CTkOptionMenu(self.interfaz1,width=120,height=20,values=self.eventosOcurriendo,command=self.HallarPosicion)
        self.com.set("Eventos")
        self.text = tk.CTkTextbox(self.interfaz1,width=585,height=150,font=tk.CTkFont(family="bold",size=15),text_color="white")
      
        #//////////////////////////////// Eventos ///////////////////////////////////////////////////
        self.cal.bind("<<CalendarSelected>>", self.HallarDiayMes)
        
        #////////////////////////////////////////////////////////// Posiciones primera interfaz ///////////////////////////////////////
        self.interfaz1.place(x=14,y=12,relheight=0.96,relwidth=0.975)
        self.frameM.place(x=5,y=5)
        self.frameCal.place(x=35,y=145)
        self.cal.place(x=15,y=15,relheight=0.9,relwidth=0.9)
        self.com.place(x=520,y=80)
        self.label2.place(x=520,y=50)
        self.label1.place(x=520,y=480)
        self.label3.place(x=100,y=110)
        self.text.place(x=420,y= 510)
        self.boton1.place(x=15,y=625)
        self.boton2.place(x=128,y=540)
        self.boton3.place(x=240,y=625)
        self.boton4.place(x=35,y=580)
        self.boton5.place(x=220,y=580)

#///////////////////////////////////////////////////////////////////////////// SEGUNDA INTERFAZ: CREAR EVENTO //////////////////////////////////////////////////////////
        self.inventario = ExtraerJson.Extraer("Inventario.json")
        self.recursos = [] 
        self.lugares = []
        self.tipo =[]
        self.year = ""
        self.FuenteBase = tk.CTkFont(size=19,family="Perpetua")
        self.errores =[]
        self.menu_errores = tk.CTkOptionMenu(self.interfaz2,width=120,height=20,values=self.errores,command=self.MostrarErrores)
        self.menu_errores.place(x=1000,y=50)
        self.menu_errores.set("No hay errores")

        self.Label1b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca\nla Hora inicial"); self.Label1b.place(x=220,y=30)
        self.Label2b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca\nla Hora final"); self.Label2b.place( in_=self.interfaz2,x=320,y=30)
        self.Label3b = tk.CTkLabel(self.interfaz2,height=2,width=11,text="Introduzca\n el Ano"); self.Label3b.place( in_=self.interfaz2,x=423,y=30)
        self.Label4b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Seleccione el\n Mes deseado"); self.Label4b.place( in_=self.interfaz2,x=625,y=30)
        self.Label6b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Seleccione el\nDia deseado"); self.Label6b.place( in_=self.interfaz2,x=770,y=30)
        self.botonAyuda = tk.CTkButton(self.interfaz2,height=40,width=40,text="?",bg_color="transparent",command=self.Hint);self.botonAyuda.place(x=530,y=35)
        self.text1FI = tk.CTkTextbox(self.interfaz2,width=75,height=23,text_color="red"); self.text1FI.place(x=220,y= 70)
        self.text2FF = tk.CTkTextbox(self.interfaz2,width=75,height=23,); self.text2FF.place(x=320,y= 70)
        self.text3A = tk.CTkTextbox(self.interfaz2,width=75,height=23,); self.text3A.place(x=420,y= 70)
        self.text4M = tk.CTkTextbox(self.interfaz2,width=130,height=50,); self.text4M.place(x=600,y= 70)
        self.text5D = tk.CTkTextbox(self.interfaz2,width=130,height=50,); self.text5D.place(x=750,y= 70)
        self.Label7b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca el nombre del Evento"); self.Label7b.place( in_=self.interfaz2,x=480,y=140)
        self.nombreEvento = tk.CTkTextbox(self.interfaz2,width=700,height=40,); self.nombreEvento.place(x=230,y= 170)

        self.tipo1 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Mineria",command= lambda:self.tipo.append("Mineria") if "Mineria" not in self.tipo else self.tipo.remove("Mineria")); self.tipo1.place(x=100,y=250)
        self.tipo2 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Mantenimiento",command= lambda:self.tipo.append("Mantenimiento") if "Mantenimiento" not in self.tipo else self.tipo.remove("Mantenimiento") ); self.tipo2.place(x=210,y=250)
        self.tipo3 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Construccion",command= lambda:self.tipo.append("Construccion") if "Construccion" not in self.tipo else self.tipo.remove("Construccion") ); self.tipo3.place(x=350,y=250)  
        self.tipo4 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Exploracion",command= lambda:self.tipo.append("Exploracion") if "Exploracion" not in self.tipo else self.tipo.remove("Exploracion") ); self.tipo4.place(x=500,y=250)
        self.tipo5 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Combate",command= lambda:self.tipo.append("Combate") if "Combate" not in self.tipo else self.tipo.remove("Combate") ); self.tipo5.place(x=630,y=250)
        self.tipo6 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Guardia",command= lambda:self.tipo.append("Guardia") if "Guardia" not in self.tipo else self.tipo.remove("Guardia") ); self.tipo6.place(x=750,y=250)
        self.tipo7 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Relaciones",command= lambda:self.tipo.append("Relaciones") if "Relaciones" not in self.tipo else self.tipo.remove("Relaciones") ); self.tipo7.place(x=860,y=250)
        #////////////////////////////////////////////// Seleccionables 1 ////////////////////////////////////////////////////////////////  
        self.framePersonajes = tk.CTkFrame(self.interfaz2,width=480,height=280);self.framePersonajes.place(x=10,y=380)
        self.labelPersonajes = tk.CTkLabel(self.framePersonajes,font=self.FuenteBase,height=2,width=13,text="Brigadas y Caballeros Reales"); self.labelPersonajes.place(x=110,y=20)
        self.opcion1 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Ogrim",command= lambda:self.recursos.append("Ogrim") if "Ogrim" not in self.recursos else self.recursos.remove("Ogrim")); self.opcion1.place(x=30,y=65)
        self.opcion2 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Isma",command= lambda:self.recursos.append("Isma") if "Isma" not in self.recursos else self.recursos.remove("Isma") ); self.opcion2.place(x=30,y=110)
        self.opcion3 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Doliente Gris",command= lambda:self.recursos.append("Doliente Gris") if "Doliente Gris" not in self.recursos else self.recursos.remove("Doliente Gris") ); self.opcion3.place(x=30,y=155)
        self.opcion4 = tk.CTkCheckBox(self.framePersonajes, font=self.FuenteBase,width=40, height=20, text="Hegemol",command= lambda:self.recursos.append("Hegemol") if "Hegemol" not in self.recursos else self.recursos.remove("Hegemol") ); self.opcion4.place(x=30,y=200)
        self.opcion5 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Hornet",command= lambda:self.recursos.append("Hornet") if "Hornet" not in self.recursos else self.recursos.remove("Hornet") ); self.opcion5.place(x=30,y=245)
        self.opcion6 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Cornifer",command= lambda:self.recursos.append("Cornifer") if "Cornifer" not in self.recursos else self.recursos.remove("Cornifer") ); self.opcion6.place(x=270,y=65)
        self.opcion7 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Brigada de Construccion",command= lambda:self.recursos.append("Brigada de Construccion") if "Brigada de Construccion" not in self.recursos else self.recursos.remove("Brigada de Construccion") ); self.opcion7.place(x=270,y=110)
        self.opcion8 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Brigada de Mineria",command= lambda:self.recursos.append("Brigada de Mineria") if "Brigada de Mineria" not in self.recursos else self.recursos.remove("Brigada de Mineria") ); self.opcion8.place(x=270,y=155)
        self.opcion9 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Hollow Knight",command=lambda: self.recursos.append("Hollow Knight") if "Hollow Knight" not in self.recursos else self.recursos.remove("Hollow Knight") ); self.opcion9.place(x=270,y=200)
        self.opcion10 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Rey Palido",command=lambda: self.recursos.append("Rey Palido") if "Rey Palido" not in self.recursos else self.recursos.remove("Rey Palido") ); self.opcion10.place(x=270,y=245)
        #////////////////////////////////////////////// Seleccionables 2 ////////////////////////////////////////////////////////////////
        self.frameLocalizaciones = tk.CTkFrame(self.interfaz2,width=540,height=280);self.frameLocalizaciones.place(x=620,y=380)
        self.labelLocalizaciones = tk.CTkLabel(self.frameLocalizaciones,font=self.FuenteBase,height=2,width=13,text="Rutas de Hallownest"); self.labelLocalizaciones.place(x=170,y=20)
        self.opcion11 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="BocaSucia",command=lambda: self.lugares.append("BocaSucia") if "BocaSucia" not in self.lugares else self.lugares.remove("BocaSucia") ); self.opcion11.place(x=390,y=65)
        self.opcion12 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Cruces Olvidados",command=lambda: self.lugares.append("Cruces Olvidados") if "Cruces Olvidados" not in self.lugares else self.lugares.remove("Cruces Olvidados") ); self.opcion12.place(x=30,y=110)
        self.opcion13 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Sendero Verde",command=lambda: self.lugares.append("Sendero Verde") if 'Sendero Verde' not in self.lugares else self.lugares.remove("Sendero Verde") ); self.opcion13.place(x=30,y=155)
        self.opcion14 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text= "Ciudad de Lagrimas",command=lambda: self.lugares.append("Ciudad de Lagrimas") if "Ciudad de Lagrimas" not in self.lugares else self.lugares.remove("Ciudad de Lagrimas") ); self.opcion14.place(x=30,y=200)
        self.opcion15 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text=  "Jardines de la Reina",command=lambda: self.lugares.append("Jardines de la Reina") if "Jardines de la Reina" not in self.lugares else self.lugares.remove("Jardines de la Reina") ); self.opcion15.place(x=30,y=245)
        self.opcion16 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text= "Nido Profundo",command=lambda: self.lugares.append("Nido Profundo") if "Nido Profundo" not in self.lugares else self.lugares.remove("Nido Profundo") ); self.opcion16.place(x=220,y=65)
        self.opcion17 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Paramos Fungicos",command=lambda: self.lugares.append("Paramos Fungicos") if "Paramos Fungicos" not in self.lugares else self.lugares.remove("Paramos Fungicos") ); self.opcion17.place(x=220,y=110)
        self.opcion18 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text=  "La Colmena",command=lambda: self.lugares.append("La Colmena") if "La Colmena" not in self.lugares else self.lugares.remove("La Colmena") ); self.opcion18.place(x=220,y=155)
        self.opcion19 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Canales Reales",command=lambda: self.lugares.append("Canales Reales") if "Canales Reales" not in self.lugares else self.lugares.remove("Canales Rea;es") ); self.opcion19.place(x=220,y=200)
        self.opcion20 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Tierras de reposo",command=lambda: self.lugares.append("Tierras de Reposo") if "Tierras de Reposo" not in self.lugares else self.lugares.remove("Tierras de Reposo") ); self.opcion20.place(x=220,y=245)
        self.opcion21 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Cumbre de Cristal",command=lambda: self.lugares.append("Cumbre de Cristal") if "Cumbres de Cristal" not in self.lugares else self.lugares.remove("Cumbres de Cristal") ); self.opcion21.place(x=30,y=65)
        self.opcion22 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Palacio Blanco",command=lambda: self.lugares.append("Palacio Blanco") if "Palacio Blanco" not in self.lugares else self.lugares.remove("Palacio Blanco") ); self.opcion22.place(x=390,y=245)
        #////////////////////////////////////////////// Botones segunda interfaz /////////////////////////////////////
        self.int2bot1 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Crear",bg_color="transparent",command= self.Crear2);self.int2bot1.place(x=505,y=450)
        self.int2bot2 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Salir",bg_color="transparent",command= lambda: self.root.destroy()) ;self.int2bot2.place(x=505,y=500)
        self.int2bot3 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Inventario",bg_color="transparent");self.int2bot3.place(x=505,y=550)
        self.int2bot4 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Restricciones",bg_color="transparent",);self.int2bot4.place(x=505,y=600)

  #/////////////////////////////////////////////////////////////////////// TERCERA INTERFAZ /////////////////////////////////////////////////////
        self.frameInv = tk.CTkScrollableFrame(self.interfaz3); self.frameInv.place(x=0,y=0,relheight=1.0,relwidth=1.0)

    
     def HallarDiayMes(self, event):
        self.eventosOcurriendo=[]
        self.text.delete(1.0,tk.END)
        self.ListarEventos()

     def HallarPosicion(self, event):
        self.text.delete(1.0, tk.END)
        if len(self.opciones)>0 and len(self.eventosOcurriendo)>0:
           # Aprovecho y ajusto en la misma posicion los detalles de evento
           seleccion = self.eventosOcurriendo[int(event[0])]
           if len(seleccion)>0:
            self.text.insert("1.0", f"Evento: {seleccion[0]}"
                                 f"\n🕐Hora: {seleccion[1]} "
                                 f"\n🗓Dia: {seleccion[2]} / {seleccion[3]}"
                                 f"\n🐝Recursos: {seleccion[7]}"
                                 f"\nLugar: {seleccion[6]}\nTipo: {seleccion[5]}")
        else : 
            self.com.set("Escoja otro dia") 
            self.opciones=[]
        
     def ListarEventos(self,event=None):
           date = datetime.datetime.strptime(self.cal.get_date(), "%m/%d/%y")
           ano = str(date.year)
           mes = str(date.month)
           dia =date.day
          
           if ano in  self.jsonEcj["Eventos en ejecucion"]:
              if mes in  self.jsonEcj["Eventos en ejecucion"][ano]:
                for x in self.jsonEcj["Eventos en ejecucion"][ano][mes]:
                   if (dia == x[2]):
                    self.eventosOcurriendo=[]
                    self.opciones=[]
                    self.eventosOcurriendo.append(x)
                    
           valores =self.eventosOcurriendo
       
           if len(valores)>0:
             self.com.set("Aqui estan los eventos este dia") 
             cont = 0
             for x in valores:
                self.opciones.append(f"{cont}-{x[0]} {x[1]}")
                cont+=1
             self.com.configure(values=self.opciones) 

           else:
             self.com.set("No hay eventos este dia") 
             self.eventosOcurriendo=[]
             self.opciones=[]
             self.com.configure(values=[])
            
     def Crear(self,event=None):
        self.interfaz1.place_forget()
        self.interfaz2.place(x=14,y=12,relheight=0.96,relwidth=0.975)        
     #///////////////////////////////////////// Objetos Interfaz Crear EVENTOS ///////////////////////////////////////////////  
       
     def Hint(self,event=None):
           ventana = tkinter.Tk();ventana.minsize(500,200)
           mensaje = tkinter.Label(ventana,text="La entrada de las horas es en hora militar, si no desea usarla de este modo, toque el checbox a la izquierda.\nLos meses son uno debajo del otro y los dias son continuos por comas,si escribio un dia incorrecto, se le dira. El prgrama solo leera los datos corrctos, los otros los desechara")
           mensaje.pack()


     def Crear2(self):
        eventos = self.Hora()
        if type(eventos)==list:
            RequisitosDeEventos.Entrada(eventos)
          
         #  print(f"Validos:{b[0]}\nInvalidos:{b[1]}")

     def ExtraerDatos(self,textblock:tk.CTkTextbox):
        lista=[]
        contenido = textblock.get("1.0",tk.END)
        linea = contenido.splitlines()
        for x in linea:
           b = x.split(",")
           lista1 =[]
           for j in b:
              if j.isdigit() and int(j)>=0 :
                 lista1.append(int(j))
           lista = lista + [lista1]
        return lista   
               
     def Dias(self):
         dias = self.ExtraerDatos(self.text5D)
         l =[]
         for x in range(len(dias)):
            l2=[]
            for i in range(len(dias[x])):
               if dias[x][i] <=31:
                  l2.append(dias[x][i])
            l.append(l2)      
         return dias
        
     def Meses(self):
        mes  = self.ExtraerDatos(self.text4M)
        l =[]
        for x in range(len(mes)):
            l2=[]
            for i in range(len(mes[x])):
               if mes[x][i] <=12:
                  l2.append(mes[x][i])
            l.append(l2)      
        return mes    

     def Fecha(self):      
        dias = self.Dias()
        meses = self.Meses()
        year = self.Year()
        if dias==[[]] or len(dias)==0 or meses==[[]] or len(meses)==0 or year == 0:
            if dias==[[]] or len(dias)==0:
                print("DIA MAL")
            if  meses==[[]] or len(meses)==0:
               print("MES MAL")
            if  year == None or year ==0: 
                print("ANO MALO")   
        else:
           fechas = []
           if len(dias)==len(meses):
              for x in range(len(dias)):
                 b = [list(set(dias[x])),meses[x][0],year]
                 fechas.append(b)

           elif len(dias)>len(meses):
              contador = 0
              for x in range(len(meses)):
                 b = [list(set(dias[x])),meses[x][0],year]
                 fechas.append(b)   
                 contador+=1
              b=[]
              for y in range(contador,len(dias)):
                 b = b +dias[y]
              fechas[len(fechas)-1][0] =  list(set(fechas[len(fechas)-1][0] +b))

           elif len(dias)<len(meses):  
             contador =0
             for x in range(len(dias)):
                 b = [list(set(dias[x])),meses[x][0],year]
                 fechas.append(b)   
                 contador+=1
             for y in range(contador,len(meses)):
                  j = [fechas[len(fechas)-1][0],meses[y][0],year]
                  fechas.append(j)
           b=self.ValidarFecha(fechas)   
           return b  

     def ValidarFecha(self,fecha:list):  
        f = fecha          
        for x in range(len(fecha)):
           mes = fecha[x][1]; year = fecha[x][2];
           diasM = calendar.monthrange(month=mes,year=year)[1]
           b=[]
           for y in range(len(fecha[x][0])):
              if fecha[x][0][y] <= diasM:
                 b.append(fecha[x][0][y])
           f[x][0]=b  
        return f      
                 

         
     def Year(self):
         year = 0
         contenido = self.text3A.get("1.0","1.end")
         if len(contenido)==4 and contenido.isdigit() and int(contenido)>=2025:
           year = int(contenido)
         return year 
     
     def Recursos(self):
      eventos:list = self.Places()
      if type(eventos)==list:
        lista = self.recursos
        recursosP = self.inventario["Brigada"]
        recursosL = self.inventario["Lugares"]
        condicion = True
        x= eventos[0]
        if len(lista)>0:
          if len(lista)>0:
           for y in lista:
              if x[3] in recursosP[y]["Incapacidad"]:
                  condicion = False
                  print(f"El evento es invalido, {y} y {x[3]} por convencion no pueden realizarse juntos")
                  break
           for z in lista:
              if z not in recursosL[x[4]]:  
                 condicion = False
                 print(f"El evento es invalido, {y} no puede estar en {x[4]}")
                 break  
           if condicion:
             for x in eventos:
                x.append(lista)
             return eventos
        else:
           print("Introduzca un personaje")  
           
        
           
     def Places(self):
        if len(self.lugares)==0 or len(self.lugares) >1:
           if len(self.lugares)==0:
            print("Introduzca un lugar")
           elif len(self.lugares)>1:
              print("No pueden ser dos a la vez ..") 
        elif len(self.lugares)==1:
           b = self.TipoEvento()
           
           if type(b)==list:
              for x in b:
                x.append(self.lugares[0])
              return b
                 
             
              
     def TipoEvento(self):  
         if len(self.tipo)==0 or len(self.tipo) >1:
           if len(self.tipo)==0:
            print("Introduzca un tipo")
           elif len(self.tipo)>1:
              print("No pueden ser dos a la vez ..")  
         elif len(self.tipo)==1:
               b=self.Fecha()
               if type(b)==list:
                for x in b:
                  x.append(self.tipo[0])
                return b
               
     def Hora(self):         
        horaI = self.text1FI.get("1.0","1.end")
        horaF = self.text2FF.get("1.0","1.end")
        b = len(horaF); c = len(horaI)
       
        if b>0 and b<6 and c>0 and b<6 :
           try :
             horaI= datetime.datetime.strptime(horaI,"%H:%M")
             horaI= datetime.datetime.strftime(horaI,"%H:%M")
             horaF= datetime.datetime.strptime(horaF,"%H:%M")
             horaF= datetime.datetime.strftime(horaF,"%H:%M")

           except: 
              print("Formato de fecha invalido, recuerde es formato 00:00 a 24:00")
           else:
             if horaF>horaI:
              eventos:list[list]= self.Recursos()
              if type(eventos)==list:
                if horaI < horaF:           
                  hora = f"{horaI} a {horaF}"
                  if type(eventos)==list :
                    for x in eventos:
                      x.insert(0,hora)
                    contenido = self.nombreEvento.get("1.0","1.end") 
                    if len(contenido)>0:
                      for x in eventos:
                        x.insert(0,contenido) 
                      return eventos  
                    else:
                     print("Introduzca un nombre valido")
                else: print("Mamon pusiste mal la hora")
        else:
          print("Formato de fecha invalido, recuerde es formato 00:00 a 24:00")  


     def MostrarErrores(self):
        pass

#///////////////////////////////////////////////// Tercera Ventana //////////////////////////////////////////////////////////////                           
     def Crear3(self,event=None):
        self.interfaz1.place_forget()
        self.interfaz3.place(x=14,y=12,relheight=0.96,relwidth=0.975)   
           
                   
        
            
r1 = tk.CTk()
r2 = SegundaVentana(r1)
r1.mainloop()
