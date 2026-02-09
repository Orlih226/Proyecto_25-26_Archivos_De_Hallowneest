import customtkinter as tk
import calendar 
from TrabajoConJson import ExtraerJson
from tkcalendar import Calendar
import math
import copy
import datetime
from Trabajar import *

class SegundaVentana:
     def __init__(self, root:tk.CTk):
        self.root = root
        self.Interfaz()
     def Interfaz(self):
         #////////////////////////////////////////////////////////////// Crear ventana  //////////////////////////////////////////////////
        self.root.minsize(1200, 675)
        self.root.title("Gestor de Eventos")
        self.root.maxsize(1200,675)
 #///////////////////////////////////////// Objetos ventana Principal ///////////////////////////////////////////////
        self.eventosOcurriendo =[""]
        self.opciones=[]
        self.seleccion=[]
        self.eliminados =[]
        self.jsonEcj = ExtraerJson.Extraer("EventosEjec.json")
        self.interfaz1 = tk.CTkFrame(self.root) 
        self.interfaz2 = tk.CTkFrame(self.root) 
        self.interfaz3 = tk.CTkFrame(self.root)
        self.interfaz4 = tk.CTkFrame(self.root)
        self.frameM = tk.CTkFrame(self.interfaz1,width=405,height=660)
        self.label3 = tk.CTkLabel(self.interfaz1, text="Seleccione un fecha:",bg_color="transparent")
        self.frameCal = tk.CTkFrame(self.frameM,width=320,height=320)
        self.cal = Calendar(self.frameCal, selectmode='day', year=2025, month=10, day=13)
        self.label2 = tk.CTkLabel(self.interfaz1, text="Aquí tienes los eventos del dia")
        self.label1 = tk.CTkLabel(self.interfaz1, text="Aquí estan los detalles de evento",font=tk.CTkFont(family="bold",size=20))
        self.boton1 = tk.CTkButton(self.frameM,text="Crear evento",command=self.Crear)
        self.boton2 = tk.CTkButton(self.frameM,text="Salir",command=self.salir)
        self.com = tk.CTkOptionMenu(self.interfaz1,width=120,height=20,values=self.eventosOcurriendo,command=self.HallarPosicion)
        self.com.set("Eventos")
        self.text = tk.CTkTextbox(self.interfaz1,width=555,height=150,font=tk.CTkFont(family="bold",size=15),text_color="white")
        self.text.bind("<Key>",self.bloquear_Escritura)
        self.text.bind("<Key>",self.bloquear_borrado)
       
        self.boton3Primera =tk.CTkButton(self.interfaz1,text="Borrar evento",command=self.borrar_dia)
        self.boton4Primera =tk.CTkButton(self.interfaz1,text="Borrar todos los eventos del mes",command=self.borrar_mes)
        self.boton5Primera =tk.CTkButton(self.interfaz1,text="Borrar todos los eventos del año",command=self.borrar_ano)
      
        #//////////////////////////////// Eventos ///////////////////////////////////////////////////
        self.cal.bind("<<CalendarSelected>>", self.HallarDiayMes)
        self.root.protocol("WM_DELETE_WINDOW",self.cerrar)
        
        #////////////////////////////////////////////////////////// Posiciones primera interfaz ///////////////////////////////////////
        self.interfaz1.place(x=0,y=0,relheight=1,relwidth=1)
        self.frameM.place(x=5,y=5)
        self.frameCal.place(x=35,y=145)
        self.cal.place(x=15,y=15,relheight=0.9,relwidth=0.9)
        self.com.place(x=520,y=80)
        self.label2.place(x=520,y=50)
        self.label1.place(x=520,y=480)
        self.label3.place(x=100,y=110)
        self.text.place(x=420,y= 510)
        self.boton1.place(x=15,y=625)
        self.boton2.place(x=240,y=625)
        self.boton3Primera.place(x=985,y=545)
        self.boton4Primera.place(x=985,y=585)
        self.boton5Primera.place(x=985,y=625)
       # self.boton4.place(x=35,y=580)
      

#///////////////////////////////////////////////////////////////////////////// SEGUNDA INTERFAZ: CREAR EVENTO //////////////////////////////////////////////////////////
        #/////////////////////////////////////////////////////////   Recursos //////////////////////////////// 
        self.inventario = ExtraerJson.Extraer("Inventario.json")
        self.recursos = [] 
        self.lugares = []
        self.tipo =[]
        self.year = ""
        self.FuenteBase = tk.CTkFont(size=19,family="Perpetua")
        self.errores =[]
        self.menu_errores = tk.CTkOptionMenu(self.interfaz2,width=120,height=30,values=self.errores,command=self.mostrar_errores)
        self.menu_errores.place(x=1000,y=50)
        self.menu_errores.set("No hay errores")
        #////////////////////////////////////////////////////// Labels ///////////////////////////////////////// 
        self.Label1b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca\nla Hora inicial"); self.Label1b.place(x=220,y=30)
        self.Label2b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca\nla Hora final"); self.Label2b.place( in_=self.interfaz2,x=320,y=30)
        self.Label3b = tk.CTkLabel(self.interfaz2,height=2,width=11,text="Introduzca\n el Año"); self.Label3b.place( in_=self.interfaz2,x=423,y=30)
        self.Label4b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Seleccione el\n Mes deseado"); self.Label4b.place( in_=self.interfaz2,x=625,y=30)
        self.Label6b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Seleccione el\nDia deseado"); self.Label6b.place( in_=self.interfaz2,x=770,y=30)

        self.botonAyuda = tk.CTkButton(self.interfaz2,height=40,width=40,text="Ayuda Y RESTRICCIONES",bg_color="transparent",command=self.Hint);self.botonAyuda.place(x=30,y=35)
        self.text1FI = tk.CTkTextbox(self.interfaz2,width=75,height=23); self.text1FI.place(x=220,y= 70)
        self.text2FF = tk.CTkTextbox(self.interfaz2,width=75,height=23,); self.text2FF.place(x=320,y= 70)
        self.text3A = tk.CTkTextbox(self.interfaz2,width=75,height=23,); self.text3A.place(x=420,y= 70)
        self.text4M = tk.CTkTextbox(self.interfaz2,width=130,height=50,); self.text4M.place(x=600,y= 70)
        self.text5D = tk.CTkTextbox(self.interfaz2,width=130,height=50,); self.text5D.place(x=750,y= 70)
        self.Label7b = tk.CTkLabel(self.interfaz2,height=2,width=13,text="Introduzca el nombre del Evento"); self.Label7b.place( in_=self.interfaz2,x=480,y=140)
        self.nombreEvento = tk.CTkTextbox(self.interfaz2,width=700,height=40,); self.nombreEvento.place(x=230,y= 170)
        #///////////////////////////////////////////////// Seleccionable Tipos ////////////////////////////////////////////////
        self.tipo1 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Mineria"); self.tipo1.place(x=100,y=250)
        self.tipo2 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Mantenimiento",checkmark_color=None); self.tipo2.place(x=210,y=250)
        self.tipo3 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Construccion"); self.tipo3.place(x=350,y=250)  
        self.tipo4 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Exploracion"); self.tipo4.place(x=500,y=250)
        self.tipo5 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Combate"); self.tipo5.place(x=630,y=250)
        self.tipo6 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Guardia"); self.tipo6.place(x=750,y=250)
        self.tipo7 = tk.CTkCheckBox(self.interfaz2, width=40, height=20, text="Relaciones"); self.tipo7.place(x=860,y=250)
      
        self.tipo1.configure(command=lambda:self.Botones(self.tipo1,self.tipo)) 
        self.tipo2.configure(command=lambda:self.Botones(self.tipo2,self.tipo)) 
        self.tipo3.configure(command=lambda:self.Botones(self.tipo3,self.tipo)) 
        self.tipo4.configure(command=lambda:self.Botones(self.tipo4,self.tipo)) 
        self.tipo5.configure(command=lambda:self.Botones(self.tipo5,self.tipo)) 
        self.tipo6.configure(command=lambda:self.Botones(self.tipo6,self.tipo)) 
        self.tipo7.configure(command=lambda:self.Botones(self.tipo7,self.tipo)) 
 
        #////////////////////////////////////////////// Seleccionables Personajes ////////////////////////////////////////////////////////////////  
        self.framePersonajes = tk.CTkFrame(self.interfaz2,width=480,height=280);self.framePersonajes.place(x=10,y=380)
        self.labelPersonajes = tk.CTkLabel(self.framePersonajes,font=self.FuenteBase,height=2,width=13,text="Brigadas y Caballeros Reales"); self.labelPersonajes.place(x=110,y=20)
        self.opcion1 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Ogrim"); self.opcion1.place(x=30,y=65)
        self.opcion2 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Isma"); self.opcion2.place(x=30,y=110)
        self.opcion3 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Doliente Gris"); self.opcion3.place(x=30,y=155)
        self.opcion4 = tk.CTkCheckBox(self.framePersonajes, font=self.FuenteBase,width=40, height=20, text="Hegemol"); self.opcion4.place(x=30,y=200)
        self.opcion5 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Hornet"); self.opcion5.place(x=30,y=245)
        self.opcion6 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Cornifer"); self.opcion6.place(x=270,y=65)
        self.opcion7 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Brigada de Construccion"); self.opcion7.place(x=270,y=110)
        self.opcion8 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Brigada de Mineria"); self.opcion8.place(x=270,y=155)
        self.opcion9 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Hollow Knight"); self.opcion9.place(x=270,y=200)
        self.opcion10 = tk.CTkCheckBox(self.framePersonajes,font=self.FuenteBase, width=40, height=20, text="Rey Palido"); self.opcion10.place(x=270,y=245)
      
        self.opcion1.configure(command=lambda:self.Botones(self.opcion1,self.recursos))
        self.opcion2.configure(command=lambda:self.Botones(self.opcion2,self.recursos))
        self.opcion3.configure(command=lambda:self.Botones(self.opcion3,self.recursos))
        self.opcion4.configure(command=lambda:self.Botones(self.opcion4,self.recursos))
        self.opcion5.configure(command=lambda:self.Botones(self.opcion5,self.recursos))
        self.opcion6.configure(command=lambda:self.Botones(self.opcion6,self.recursos))
        self.opcion7.configure(command=lambda:self.Botones(self.opcion7,self.recursos))
        self.opcion8.configure(command=lambda:self.Botones(self.opcion8,self.recursos))
        self.opcion9.configure(command=lambda:self.Botones(self.opcion9,self.recursos))
        self.opcion10.configure(command=lambda:self.Botones(self.opcion10,self.recursos))
        #////////////////////////////////////////////// Seleccionables 2 ////////////////////////////////////////////////////////////////
        self.frameLocalizaciones = tk.CTkFrame(self.interfaz2,width=540,height=280);self.frameLocalizaciones.place(x=640,y=380)
        self.labelLocalizaciones = tk.CTkLabel(self.frameLocalizaciones,font=self.FuenteBase,height=2,width=13,text="Rutas de Hallownest"); self.labelLocalizaciones.place(x=170,y=20)
        self.opcion11 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="BocaSucia");self.opcion11.place(x=390,y=65)
        self.opcion12 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Cruces Olvidados"); self.opcion12.place(x=30,y=110)
        self.opcion13 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Sendero Verde"); self.opcion13.place(x=30,y=155)
        self.opcion14 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text= "Ciudad de Lagrimas"); self.opcion14.place(x=30,y=200)
        self.opcion15 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text=  "Jardines de la Reina") ; self.opcion15.place(x=30,y=245)
        self.opcion16 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text= "Nido Profundo" ); self.opcion16.place(x=220,y=65)
        self.opcion17 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Paramos Fungicos" ); self.opcion17.place(x=220,y=110)
        self.opcion18 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text=  "La Colmena"); self.opcion18.place(x=220,y=155)
        self.opcion19 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Canales Reales" ); self.opcion19.place(x=220,y=200)
        self.opcion20 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Tierras de reposo"); self.opcion20.place(x=220,y=245)
        self.opcion21 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Cumbre de Cristal" ); self.opcion21.place(x=30,y=65)
        self.opcion22 = tk.CTkCheckBox(self.frameLocalizaciones, width=40, height=20,font=self.FuenteBase, text="Palacio Blanco"); self.opcion22.place(x=390,y=245)

        self.confirmacion = tk.CTkButton(self.interfaz2,text="Sus eventos han sido cargados al segundo plano",command=lambda:self.confirmacion.place_forget(),fg_color="green",hover_color="green")
       
        self.opcion11.configure(command=lambda:self.Botones(self.opcion11,self.lugares))
        self.opcion12.configure(command=lambda:self.Botones(self.opcion12,self.lugares))
        self.opcion13.configure(command=lambda:self.Botones(self.opcion13,self.lugares))
        self.opcion14.configure(command=lambda:self.Botones(self.opcion14,self.lugares))
        self.opcion15.configure(command=lambda:self.Botones(self.opcion15,self.lugares))
        self.opcion16.configure(command=lambda:self.Botones(self.opcion16,self.lugares))
        self.opcion17.configure(command=lambda:self.Botones(self.opcion17,self.lugares))
        self.opcion18.configure(command=lambda:self.Botones(self.opcion18,self.lugares))
        self.opcion19.configure(command=lambda:self.Botones(self.opcion19,self.lugares))
        self.opcion20.configure(command=lambda:self.Botones(self.opcion20,self.lugares))
        self.opcion21.configure(command=lambda:self.Botones(self.opcion21,self.lugares))
        self.opcion22.configure(command=lambda:self.Botones(self.opcion22,self.lugares))
        #////////////////////////////////////////////// Botones segunda interfaz /////////////////////////////////////
        self.int2bot1 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Crear",command= self.crear_eventos);self.int2bot1.place(x=505,y=500)
        self.int2bot2 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Salir",command=self.salir) ;self.int2bot2.place(x=505,y=550)
        self.int2bot4 = tk.CTkButton(self.interfaz2,height=25,width=100,text="Menu",command=self.Menu);self.int2bot4.place(x=505,y=600)




#//////////////////////////////////////////////////////////////////// TERCERA INTERFAZ ////////////////////////////////////////////////////////////////////////////////////////////////
        #////////////////////////////////////////////////////////////// ELEMENTOS /////////////////////////////////////
        self.boton1Tercera = tk.CTkButton(self.interfaz3,text="Seleccionar los validados",command=self.seleccionar_validos);self.boton1Tercera.place(x=50,y=630)
        self.boton2Tercera = tk.CTkButton(self.interfaz3,text="Ignorar los fallos y usar solo las validas",command=self.usar_solo_validas);self.boton2Tercera.place(x=320,y=630)
        self.boton3Tercera = tk.CTkButton(self.interfaz3,text="Negar operacion y borrar borrador",command=self.negar_eventos_y_borrador);self.boton3Tercera.place(x=640,y=630)
        self.boton4Tercera = tk.CTkButton(self.interfaz3,text="Negar operacion y mantener borrador",command=lambda: self.interfaz2.lift());self.boton4Tercera.place(x=925,y=630)

        texto ="Lamento informarle, que dicho/s eventos que deseo introducir al sistema no son posibles\n No debido a errores, debido a que otros colisionan \nSuerte para usted el programa le brinda a continuacion una lista con los que si entraron, los que no entraron y unos cambios de horarios a estos"
        fuente = tk.CTkFont(family="Bold",size=17)
        self.label1Tercera = tk.CTkLabel(self.interfaz3,text=texto,font=fuente);self.label1Tercera.place(x=50,y=20)
      
        frame1Tercera = tk.CTkFrame(self.interfaz3,width=1100,height=250);frame1Tercera.place(x=50, y=90) 
        frame2Tercera = tk.CTkFrame(self.interfaz3,width=1100,height=250);frame2Tercera.place(x=50, y=360) 
        texto2 ="Los eventos aquí presentados pasaron sin ningun problema:"
        label1Tercera = tk.CTkLabel(frame1Tercera,text=texto2,font=fuente);label1Tercera.place(x=10,y=0)
        self.cajaTexto1Tercera = tk.CTkTextbox(frame1Tercera,width=610,height=240,fg_color="gray22");self.cajaTexto1Tercera.place(x=480,y=5)
        self.cajaTexto1Tercera.bind("<Key>",self.bloquear_Escritura)
        self.cajaTexto1Tercera.bind("<Key>",self.bloquear_borrado)

        texto2 ="Los eventos aquí presentados no pasaron:"
        label2Tercera = tk.CTkLabel(frame2Tercera,text=texto2,font=fuente);label2Tercera.place(x=10,y=0)
        self.cajaTexto2Tercera = tk.CTkTextbox(frame2Tercera,width=500,height=220,fg_color="gray22",text_color="red");self.cajaTexto2Tercera.place(x=10,y=25)
        self.cajaTexto2Tercera.bind("<Key>",self.bloquear_Escritura)
        self.cajaTexto2Tercera.bind("<Key>",self.bloquear_borrado)

        texto2 ="Los eventos aquí presentados son el reajuste de los aledaños:"
        label3Tercera = tk.CTkLabel(frame2Tercera,text=texto2,font=fuente);label3Tercera.place(x=600,y=0)
        self.cajaTexto3Tercera = tk.CTkTextbox(frame2Tercera,width=500,height=220,fg_color="gray22");self.cajaTexto3Tercera.place(x=590,y=25)
        self.cajaTexto3Tercera.bind("<Key>",self.bloquear_Escritura)
        self.cajaTexto3Tercera.bind("<Key>",self.bloquear_borrado)
       
        self.canvas1Tercera = tk.CTkCanvas(frame1Tercera,width=550,height=260,bg="gray20");self.canvas1Tercera.place(x=15,y=35)

      #///////////////////////////////////////////////////     CUARTA INTERFAZ        ////////////////////////////////////////
        frame1Cuarta = tk.CTkFrame(self.interfaz4,width=520,height=650);frame1Cuarta.place(x=10,y=10)
        frame2Cuarta = tk.CTkFrame(self.interfaz4,width=650,height=650);frame2Cuarta.place(x=540,y=10)


        fuente = tk.CTkFont(family="Bold",size=18) 
        texto2 ="Los eventos aquí presentados son el reajuste:"
        label1Cuarta = tk.CTkLabel(frame1Cuarta,text=texto2,font=fuente);label1Cuarta.place(x=10,y=10)
        self.cajaTexto1Cuarta = tk.CTkTextbox(frame1Cuarta,width=500,height=585,fg_color="gray22");self.cajaTexto1Cuarta.place(x=10,y=50)
        self.cajaTexto1Cuarta.bind("<Key>",self.bloquear_Escritura)
        self.cajaTexto1Cuarta.bind("<Key>",self.bloquear_borrado)
       
        fuente = tk.CTkFont(family="Bold",size=19) 
        texto2 ="Seleccione, escribiendo, el indice del evento que desea inscribir a la base\n de datos. Las entradas validas son numeros separados\n por comas o uno debajo del otro\nSi un numero no esta se ignora tambien incluye cualquier letra"
        label2Cuarta = tk.CTkLabel(frame2Cuarta,text=texto2,font=fuente);label2Cuarta.place(x=10,y=10)
        self.cajaTexto2Cuarta = tk.CTkTextbox(frame2Cuarta,width=630,height=400,fg_color="gray22");self.cajaTexto2Cuarta.place(x=10,y=130)

        boton1Cuarta =tk.CTkButton(frame2Cuarta,text="Inscribir seleccionados",command=lambda:self.inscribir_seleccionados(self.cajaTexto2Cuarta,self.cajaTexto1Cuarta));boton1Cuarta.place(x=30,y=590)
        boton2Cuarta =tk.CTkButton(frame2Cuarta,text="Inscribir todos",command=self.inscribir_todas);boton2Cuarta.place(x=245,y=590)
        boton3Cuarta =tk.CTkButton(frame2Cuarta,text="No Inscribir eventos",command=self.no_inscribir);boton3Cuarta.place(x=450,y=590)

  #////////////////////////////////////////////////////////////////////Interfaces //////////////////////////////////////////////
       # self.frameInv = tk.CTkScrollableFrame(self.interfaz3); self.frameInv.place(x=0,y=0,relheight=1.0,relwidth=1.0)
        self.interfaz2.place(x=0,y=0,relheight=1,relwidth=1) 
        self.interfaz3.place(x=0,y=0,relheight=1,relwidth=1) 
        self.interfaz4.place(x=0,y=0,relheight=1,relwidth=1)      
        self.interfaz1.lift()

     def bloquear_borrado(self,event=None):
         if event.keysym =="Delete" or event.keysym=="BackSpace":
           return "break"
      

     def cerrar(self,event=None):
        ExtraerJson.Escribir(json_nuevo=self.jsonEcj,archivo="EventosEjec.json"); self.root.destroy()
        
     def bloquear_Escritura(self,event):   
        teclas = ["Up","Down","Left","Right","Prior","Next","Home","End"]
        if event.keysym not in teclas and len(event.keysym)==1:
           return "break"
      
     def actualizar_dict(self,x,eventos):
         if str(x[4]) in eventos["Eventos en ejecucion"]:
                if str(x[3]) in eventos["Eventos en ejecucion"][str(x[4])]:
                   if x not in eventos["Eventos en ejecucion"][str(x[4])][str(x[3])]:
                    eventos["Eventos en ejecucion"][str(x[4])][str(x[3])].append(x)
                else:
                    eventos["Eventos en ejecucion"][str(x[4])][str(x[3])] =[x]
         else:
                    eventos["Eventos en ejecucion"][str(x[4])][str(x[3])] =[x]           
        

    #///////////////////////////////////////////////////////// Eventos Primera Interfaz: MENU /////////////////////////////////////////////////////////////////
     def HallarDiayMes(self, event):
        self.eventosOcurriendo=[]
        self.text.delete(1.0,tk.END)
        self.ListarEventos()

     def HallarPosicion(self, event):
        self.text.delete(1.0, tk.END)
        if len(self.opciones)>0 and len(self.eventosOcurriendo)>0:
           # Aprovecho y ajusto en la misma posicion los detalles de evento
           self.seleccion = self.eventosOcurriendo[int(event[0])]
           if len(self.seleccion)>0:
            self.text.insert("1.0", f"Evento: {self.seleccion[0]}"
                                 f"\n🕐Hora: {self.seleccion[1]} "
                                 f"\n🗓Dia: {self.seleccion[2]} / {self.seleccion[3]}"
                                 f"\n🐝Recursos: {self.seleccion[7]}"
                                 f"\nLugar: {self.seleccion[6]}\nTipo: {self.seleccion[5]}")
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
             self.com.set("aquí estan los eventos este dia") 
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

     def borrar_ano(self):
         year = self.cal.get_displayed_month()
         year= year[1]
         year = str(year)
         try:
          del self.jsonEcj["Eventos en ejecucion"][year]
         except:
            pass

     def borrar_mes(self):
         mes = self.cal.get_displayed_month()
         year= mes[1]
         year = str(year)
         mes= mes[0]
         mes = str(mes)
         try:
          del self.jsonEcj["Eventos en ejecucion"][year][mes]    
         except:
            pass 

     def borrar_dia(self):
       evento =copy.deepcopy(self.seleccion)
       if evento!=[]:
        self.eliminados=[]
        year = str(evento[4])
        mes = str(evento[3])
        index:list = self.jsonEcj["Eventos en ejecucion"][year][mes]
        index = index.index(evento)
        self.eliminados = self.jsonEcj["Eventos en ejecucion"][year][mes].pop(index)
        
     def Crear(self,event=None):
        ExtraerJson.Escribir(archivo="EventosEjec.json",json_nuevo=self.jsonEcj)
        self.interfaz2.lift()

     def Menu(self):
        ExtraerJson.Escribir(archivo="EventosEjec.json",json_nuevo=self.jsonEcj)
        self.interfaz1.lift()
      
     #///////////////////////////////////////// Objetos Interfaz Crear EVENTOS ///////////////////////////////////////////////  
     #/////////////// Locales //////////////////
     def mostrar_errores(self):
           valores = self.errores
           if len(valores)>0:
             self.menu_errores.set("Presencia de errores") 
             self.menu_errores.configure(values=valores) 
             self.menu_errores.configure(fg_color="red")

           else:
             self.menu_errores.set("No hay errores") 
             self.menu_errores.configure(fg_color="green")

     def salir(self):
             ExtraerJson.Escribir(archivo="EventosEjec.json",json_nuevo=self.jsonEcj) 
             self.root.destroy()   

     def Hint(self,event=None):
           ventana = tk.CTk();ventana.minsize(height=400,width=1200);ventana.maxsize(width=1200,height=600)
           frame = tk.CTkFrame(ventana)
           fuente = tk.CTkFont(family="Bold",size=19)
           texto= "Consejos para la creación de eventos:\n1- Los meses deben introducirse uno debajo del otro separado por líneas\n2- Los dias deben estar separados por coma"\
           "\n5- Los meses y dias deben ser solo números"\
           "\n4- Al tener múltiples líneas tanto de dias como de meses, se hara la correspondencia de la n línea del mes, con la n línea del día "\
           "\n5- Si hay más líneas de mes que de dias, entonces a todos los meses en que se acabe la correspondencia anterior, se le asignara la última línea de dias" \
           "\n6- Si hay más líneas de dias que de mes, entonces a el ultimo mes se le otorgan toda las líneas de dias que vienen después de que acabe la correspondencia" \
           "\n7- Si introduce espacios en las líneas, se considerará inválido" \
           "\n8- Si introduce letras en las líneas, se considerará inválido" \
           "\n9- Hay ciertos errores que el programa depura automáticamente, esto ocurre siempre que al menos haya algún evento válido, se seguirá marcando errores" \
           "\n10- La hora se recibe en formato 24h, intente no poner espacios" \
           "\n11- No puede ocupar ni 00:00, ni 24:00, por convención" \
           "\n12- Solo puede tener un tipo a la vez" \
           "\n13 Solo puede ser un lugar a la vez" \
           "\n\nEntre los objetos existen restricciones, aquí les dejo una lista básica:" \
           "\n|Lugares             |    Capacidad" \
           "\n|Cruces Olvidados    |Hornet, Hegemol, Cornifer, Brigada de Construcción, Doliente Gris, Ogrim, Isma, Rey Pálido, Hollow Knight" \
           "\n|BocaSucia           |Hornet, Hegemol, Cornifer, Brigada de Construcción, Doliente Gris, Ogrim, Isma, Rey Pálido" \
           "\n|Sendero Verde       |Hornet, Ogrim, Isma, Cornifer, Doliente Gris, Rey Pálido" \
           "\n|Ciudad de Lagrimas  |Hornet, Hegemol, Cornifer, Brigada de Construcción, Doliente Gris, Rey Pálido, Hollow Knight" \
           "\n|Jardines de la Reina|Hornet, Hegemol, Cornifer, Brigada de Construcción, Doliente Gris, Ogrim, Isma, Rey Pálido, Hollow Knight" \
           "\n|Nido Profundo       |Hornet, Rey Pálido" \
           "\n|Paramos Fungicos    |Hornet, Rey Pálido, Ogrim, Isma, Cornifer" \
           "\n|La Colmena          |Hornet, Rey Pálido" \
           "\n|Canales Reales      |Ogrim, Isma, Cornifer" \
           "\n|Tierras de reposo   |Hornet, Rey Pálido, Doliente Gris, Hollow Knight, Cornifer" \
           "\n|Cumbre de Cristal   |Hornet, Rey Pálido, Cornifer, Brigada de Minería" \
           "\n|Palacio Blanco      |Hornet, Hegemol, Cornifer, Doliente Gris, Ogrim, Isma, Rey Pálido, Hollow Knight" \
           "\n\nEntre los personajes existen sinergias, asuma las que no aparezcan como sin sinergia:(1:AND,2:OR)" \
           "\n1-Isma: 1: Ogrim" \
           "\n2-Ogrim: 1: Isma" \
           "\n3-Cornifer: 0: Hornet, Doliente Gris, Hegemol, Isma, Ogrim" \
           "\n4-Hollow Knight: 0: Hornet, Rey Pálido" \
           "\n5-Rey Pálido: 0: Hornet, Doliente Gris, Hegemol, Isma, Ogrim, Hollow Knight" \
           "\n\nLos personajes también tiene  incapacidades:" \
           "\n1-Ogrim: Minería" \
           "\n2-Isma: Minería" \
           "\n3-Hegemol: Mantenimiento, Exploracion, Minería, Recolección" \
           "\n4-Doliente Gris: Mantenimiento, Minería, Construcción" \
           "\n5-Brigada de Construccion: Minería, Recolección, Exploración, Guardia, Combate, Relaciones" \
           "\n6-Brigada de Mineria: Recolección, Exploración, Guardia, Combate, Relaciones" \
           "\n7-Cornifer: Combate, Guardia , Relaciones" \
           "\n8-Hornet: Mineria, Mantenimiento, Construcción" \
           "\n9-Hollow Knight: Minería, Mantenimiento, Construcción" \
           "\n10-Rey Palido: Mantenimiento, Exploración, Recolección, Guardia, Minería, Construcción"            
           mensaje = tk.CTkTextbox(frame,font=fuente)
           mensaje.bind("<Key>",self.bloquear_Escritura)
           mensaje.insert("1.0",texto)
           mensaje.place(x=0,y=0,relheight=1,relwidth=1)
           frame.place(x=0,y=0,relheight=1,relwidth=1)
           ventana.mainloop()

     #/////////////// Creacion de Eventos //////////////////////
     def crear_eventos(self):
   
        self.errores = []
        eventos = self.Hora()
        try:
         self.mostrar_errores()
        except:
            pass
        self.elementos_producidos = []
        ejecucion=copy.deepcopy(self.jsonEcj)
        if type(eventos)==list:
          self.elementos_producidos =  RequisitosDeEventos.Entrada(eventos,ejecucion)
          errores = self.errores[:]
          if len(errores)==0:
           if len(self.elementos_producidos[0][1])>0:
             self.LevantarTercera(self.elementos_producidos[0])
             self.hacer_Grafico_Pastel(len(self.elementos_producidos[0][0]),len(self.elementos_producidos[0][1]))
           else:
        
            for x in self.elementos_producidos[0][0]:
             self.actualizar_dict(x,ejecucion)
            self.jsonEcj.update(ejecucion) 
            self.confirmacion.place(x=420,y=320)
          else: 
             pass
     
     def ExtraerDatos(self,textblock:tk.CTkTextbox):
        lista=[]
        contenido = textblock.get("1.0",tk.END)
        linea = contenido.splitlines() 
        for x in linea:
           b:list[str] = x.split(",")
           lista1 =[]
           for j in b:
              if j.isdigit() and int(j)>=0 :
                 lista1.append(int(j))
              if not j.isdigit() and textblock ==self.text4M:
                 self.errores.append(f"El supuesto mes {j} es incorrecto, el código ignorara este valor") 
              elif not j.isdigit() and textblock ==self.text5D:
                 self.errores.append(f"El supuesto dia {j} es incorrecto, el código ignorara este valor") 

                 
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
            if len(mes[x])>0:
             if mes[x][0] <=12 and mes[x][0]>0:
                 l2.append(mes[x][0])
             else: self.errores.append(f"El mes {mes[x][0]} es incorrecto")    
            l.append(l2)            
      return mes    

     def Fecha(self):      
        try:
         dias = self.Dias()[:]
        except:
            self.menu_errores.set("Presencia de errores") 
            self.menu_errores.configure(fg_color="red")
            self.errores.append("El dia establecido es incorrecto")
            
        try:
         meses = self.Meses()
        except:
            self.menu_errores.set("Presencia de errores") 
            self.menu_errores.configure(fg_color="red")
            self.errores.append("El mes establecido es incorrecto")   
        try: 
         year = self.Year()
        except:
             self.menu_errores.set("Presencia de errores") 
             self.menu_errores.configure(fg_color="red")
             self.errores.append("El año establecido es incorrecto")       
        if dias==[[]] or dias == [] or len(dias)==0 or meses==[[]] or meses==[]or len(meses)==0 or year == 0:
            if dias==[[]] or len(dias)==0:
                 self.errores.append("El dia establecido es incorrecto")
            if  year == None or year ==0: 
                 self.errores.append("El año establecido es incorrecto")   
            if  meses == None or meses ==0: 
                 self.errores.append("El mes establecido es incorrecto")         
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
               if len(meses[y])>0:   
                  j = [fechas[len(fechas)-1][0],meses[y][0],year]
                  fechas.append(j)
               else:  self.errores.append(f"El mes es incorrecto")
           b=self.ValidarFecha(fechas)   
           for x in b:
            if x[0]==[] or x[1]==[]or x[1]==None or x[2]==None:
              if x[0]==[]:
                  self.errores.append(f"El dia establecido es incorrecto")
              if x[1]== None or x[1]==None:
                  self.errores.append(f"El mes establecido incorrecto")        
                 
           else:   
            return b  

     def ValidarFecha(self,fecha:list):  
       try:
        f = fecha          
        for x in range(len(fecha)):
           mes = fecha[x][1]; year = fecha[x][2];
           diasM = calendar.monthrange(month=mes,year=year)[1]
           b=[]
           for y in range(len(fecha[x][0])):
              if fecha[x][0][y] <= diasM:
                 b.append(fecha[x][0][y])
              if fecha[x][0][y] > diasM:
                 self.errores.append(f"El dia {fecha[x][0][y]} es mayor que el limite del mes")
           f[x][0]=b  
        return f     
       except:
          self.errores.append(f"La fecha que ingreso no es posible de añadir")    
                                  
     def Year(self):
         year = 0
         contenido = self.text3A.get("1.0","1.end")
         if len(contenido)==4 and contenido.isdigit() and int(contenido)>=2025:
           year = int(contenido)
         return year 
     
     def Recursos(self):
      eventos:list = self.Places()
      if type(eventos)==list:
        lista = self.recursos[:]
        recursosP = self.inventario["Brigada"]
        recursosL = self.inventario["Lugares"]
        condicion = True
        condicion2 = False
        x= eventos[0]
        if len(lista)>0:
           for y in lista:
              if x[3] in recursosP[y]["Incapacidad"]:
                  condicion = False
                  self.errores.append(f"El evento es invalido, {y} y {x[3]} por convencion no pueden realizarse juntos")
                  break
           for z in lista:
              if z not in recursosL[x[4]]:  
                 condicion = False
                 self.errores.append(f"El evento es invalido, {z} no puede estar en {x[4]}")
                 break  
           if condicion:
             for x in eventos:
                x.append(lista)

           for x in lista:
               inv = recursosP[x]["Dependencia"]
               if inv ==[]:
                  pass
               elif inv[0][0]==1:
                  flag = True
                  for y in inv[0][1]:
                     if y not in lista:
                        flag = False
                        break
                  if flag == False:
                     break   

               elif inv[0][0]==0:     
                    listaR =[]
                    for y in inv[0][1]:
                       if y in lista:
                          listaR.append(True)     
                    if True not in listaR:
                       break
           else:      
                 condicion2 = True
           if condicion and condicion2:    
                   return eventos
           if condicion2 == False:
              self.errores.append(f"El evento es invalido, no contiene todas las dependencias entre objetos")   
        else:
            self.errores.append("Introduzca un personaje")  
                     
     def Places(self):
        lugares = self.lugares[:]
        if len(lugares)==0 or len(lugares) >1:
           if len(lugares)==0:
             self.errores.append("Introduzca un lugar")
           elif len(lugares)>1:
               self.errores.append("No pueden ser dos lugares a la vez ..") 
        elif len(lugares)==1:
           b = self.TipoEvento()
           
           if type(b)==list:
              for x in b:
                x.append(self.lugares[0])
              return b
                            
     def TipoEvento(self):  
         tipo = self.tipo[:]
         if len(tipo)==0 or len(tipo) >1:
           if len(tipo)==0:
             self.errores.append("Introduzca un tipo")
           elif len(tipo)>1:
               self.errores.append("No pueden ser dos tipos a la vez ..")  
         elif len(tipo)==1:
               b=None
               try:
                b=self.Fecha()
               except:
                  self.errores.append("Ha cometido un error en el momento de introducir los datos, revise si hay espacios, entre líneas")

               if type(b)==list:
                for x in b:
                  x.append(tipo[0])
                return b
               elif b ==None:
                  pass
               
     def Hora(self): 
        horaI = self.text1FI.get("1.0","1.end")
        horaF = self.text2FF.get("1.0","1.end")
        b = len(horaF); c = len(horaI)
       
        if b>0 and b<6 and c>0 and c<6 :
           try :
             horaI= datetime.datetime.strptime(horaI,"%H:%M")
             horaI= datetime.datetime.strftime(horaI,"%H:%M")
             horaF= datetime.datetime.strptime(horaF,"%H:%M")
             horaF= datetime.datetime.strftime(horaF,"%H:%M")

           except: 
             try:
              horaI= datetime.datetime.strptime(horaI,"%H:%M")
              horaI= datetime.datetime.strftime(horaI,"%H:%M")
             except:  
                self.errores.append("Error en la hora inicial, recuerde es formato 00:00 a 24:00")
             try:
              horaF= datetime.datetime.strptime(horaF,"%H:%M")
              horaF= datetime.datetime.strftime(horaF,"%H:%M")
             except:  
                self.errores.append("Error en la hora final, recuerde es formato 00:00 a 24:00")   
                
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
                     self.errores.append("Introduzca un nombre valido")
                else: self.errores.append("Error en la hora")
             else:
               self.errores.append("La hora final no puede ser menor que la inicial")
        else:
          if b == 0:
              self.errores.append("Rellene el espacio hora final")
          elif b>6:
              self.errores.append("La hora final es invalida")     

          if c == 0:
              self.errores.append("Rellene el espacio hora inicial")    
          elif c>6:
              self.errores.append("La hora inicial es invalida")  
          try:
             horaI= datetime.datetime.strptime(horaI,"%H:%M")
             horaI= datetime.datetime.strftime(horaI,"%H:%M")
          except: 
              self.errores.append("Error en la hora inicial, recuerde es formato 00:00 a 24:00")
          try:
                horaF= datetime.datetime.strptime(horaF,"%H:%M")
                horaF= datetime.datetime.strftime(horaF,"%H:%M")
          except:
              self.errores.append("Error en la hora final, recuerde es formato 00:00 a 24:00")


                
                 
       #   self.errores.append("Formato de fecha invalido, recuerde es formato 00:00 a 24:00")  

     def Botones(self,boton:tk.CTkCheckBox,lista):
        nombre = boton._text
        valor = boton._check_state
        if  nombre not in lista :
            lista.append(nombre) 
        else: lista.remove(nombre) 

#///////////////////////////////////////////////// Tercera Interfaz //////////////////////////////////////////////////////////////                           
     def LevantarTercera(self,elementos):
            self.rellenar_checkbox_eventos(self.cajaTexto1Tercera,elementos[0]) 
            self.rellenar_checkbox_eventos(self.cajaTexto2Tercera,elementos[1])
            self.rellenar_checkbox_eventos(self.cajaTexto3Tercera,elementos[2])
            self.interfaz3.lift()  
   
     def hacer_Grafico_Pastel(self,validos,invalidos):
       x=120;y=125;radio=90
       lista =[[validos,"dodger blue"],[invalidos,"deep sky blue"]]
       if validos>0 and invalidos>0:
       
        total = (validos+invalidos)   
        angulo=0
        for j in lista:
           prop = j[0]/total
           angulo_sectorial = prop*360

           inicio_rad = math.radians(angulo)
           fin_rad = math.radians(angulo + angulo_sectorial)
            
           # Coordenadas del arco
           x1 = x - radio
           y1 = y - radio
           x2 = x + radio
           y2 = y + radio
          
           self.canvas1Tercera.create_arc(
                x1, y1, x2, y2,
                start=angulo,
                extent=angulo_sectorial,
                fill=j[1],
                outline="white",
                width=2
            )
           angulo += angulo_sectorial
           texto="" 

       elif validos ==0:
        self.canvas1Tercera.create_aa_circle(x_pos=x,y_pos=y,radius=radio,fill=lista[0][1])
 
       Label= tk.CTkLabel(self.canvas1Tercera,text="");Label.place(x=250,y=75)
       boton1= tk.CTkButton(self.canvas1Tercera,text="Validos",fg_color="dodger blue",command=lambda:Label.configure(text=f"Los validos ({validos}) constituyen\n un {(validos/total)*100}%\n aproximadamente"));boton1.place(x=270,y=20)
       boton2= tk.CTkButton(self.canvas1Tercera,text="Invalidos",fg_color="deep sky blue",command=lambda:Label.configure(text=f"Los invalidos ({invalidos}) constituyen\n un {(invalidos/total)*100}%\n aproximadamente"));boton2.place(x=270,y=160) 
        
     def rellenar_checkbox_eventos(self,caja_texto:tk.CTkTextbox,elementos:list):
        caja_texto.delete("1.0",tk.END)
        texto = ""    
        for x in range(len(elementos)):
           texto += f"{x+1}- {elementos[x]}\n"
        caja_texto.insert("1.0",texto)

     def seleccionar_validos(self):
        text=  self.cajaTexto3Tercera.get("1.0",tk.END)
        self.cajaTexto1Cuarta.insert("1.0",text)
        self.interfaz4.lift()

     def usar_solo_validas(self):
       eventos = {}
       lista = self.elementos_producidos[0][0][:]
       if type(self.jsonEcj) == dict:
          eventos =copy.deepcopy(self.jsonEcj)
          for x in lista:
             if str(x[4]) in eventos["Eventos en ejecucion"]:
                if str(x[3]) in eventos["Eventos en ejecucion"][str(x[4])]:
                  if x not in eventos["Eventos en ejecucion"][str(x[4])][str(x[3])]: 
                   eventos["Eventos en ejecucion"][str(x[4])][str(x[3])].append(x)
                else:
                    eventos["Eventos en ejecucion"][str(x[4])][str(x[3])] =[x]
             else:
                    eventos["Eventos en ejecucion"][str(x[4])][str(x[3])] =[x]           
          self.jsonEcj.update(eventos)   
       self.interfaz2.lift()           
          
     def negar_eventos_y_borrador(self):
        self.nombreEvento.delete("1.0",tk.END)   
        self.text1FI.delete("1.0",tk.END)   
        self.text2FF.delete("1.0",tk.END)   
        self.text3A.delete("1.0",tk.END)   
        self.text4M.delete("1.0",tk.END)   
        self.text5D.delete("1.0",tk.END)   
        self.interfaz2.lift() 
        
#/////////////////////////////////////////////// Cuarta Interfaz ///////////////////////////////////////////////////////               
     def inscribir_seleccionados(self,caja_de_textoN:tk.CTkTextbox,caja_de_textoE:tk.CTkTextbox):
        caja_de_textoN = caja_de_textoN.get("0.0",tk.END)
        linea = caja_de_textoN.splitlines()
        listaN=[]
        for x in linea:
           if x !="":
            text= x.split(",")
            texto=[]
            for x in text:
             if (x.isdigit()) and (int(x)>0 and int(x)<=len(self.elementos_producidos[0][2])):
              texto.append(int(x))
            listaN+=texto
        

        caja_de_textoE= caja_de_textoE.get("1.0",tk.END)     
        linea = caja_de_textoE.splitlines()
        listaE=[]
        for x in linea:
           if x!="":
            text= x.split("- ")
            texto= (int(text[0]),eval(text[1]))
            listaE.append(texto) 
        listaL=[]
       
        for x in listaN:
           n = self.BusquedaBinaria4(x,0,len(listaE),listaE)
           if n == -1:
            pass
           else:
              listaL.append(list(n))
        if type(self.jsonEcj) == dict:
          eventos =copy.deepcopy(self.jsonEcj)
          for x in listaL:
            self.actualizar_dict(x,eventos)  
          self.jsonEcj.update(eventos)   
          lista=self.elementos_producidos[0][0][:]
          json = copy.deepcopy(self.jsonEcj)
          for y in lista:
           self.actualizar_dict(y,json)
          self.jsonEcj.update(json)  
          self.negar_eventos_y_borrador()
                   
     def BusquedaBinaria4(self,num,izquierda,derecha,lista):
           medio = (derecha+izquierda)//2
           if num == lista[medio][0]:
             return lista[medio][1]
           elif derecha<=izquierda:
             return -1
           if num < lista[medio][0]:
             return self.BusquedaBinaria4(num,izquierda,medio-1,lista)
           elif num > lista[medio][0]:
             return self.BusquedaBinaria4(num,medio+1,derecha,lista)  
           
     def inscribir_todas(self):
       eventos = {}
       if type(self.jsonEcj) == dict:      
          self.jsonEcj.update(self.elementos_producidos[1])  
        #  self.usar_solo_validas() 
          self.negar_eventos_y_borrador()  

     def no_inscribir(self):
        self.cajaTexto1Cuarta.delete("1.0",tk.END)      
        self.cajaTexto2Cuarta.delete("1.0",tk.END) 
        self.interfaz2.lift()

r1 = tk.CTk()
r2 = SegundaVentana(r1)
r1.mainloop()
