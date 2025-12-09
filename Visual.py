import datetime
import tkinter as tk
import json as js
from tkcalendar import Calendar
import calendar


class Visual1:

    def __init__(self, root):
        self.root = root
        self.Interfaz()

  

    def Interfaz(self):
        #////////////////////////////////////////////////////////////// Crear ventana principal //////////////////////////////////////////////////
        self.root.minsize(1200, 800)
        self.root.title("Gestor de Eventos")
        self.root.geometry("1200x700")
        
        
        self.root.protocol("WM_DELETE_WINDOW",self.Cerrar)
        #//////////////////////////////////////////////////// Ventana secundaria ////////////////////////////////////////////
        self.newroot = tk.Tk()
        self.newroot.config(bg="white")
        self.newroot.title("Condiciones de eventos")
        self.newroot.resizable(width=False, height=False)
        self.newroot.geometry("1000x498")
        self.newroot.protocol("WM_DELETE_WINDOW",lambda:None)
        self.newroot.withdraw()     
       
        #///////////////////////////////////////// Objetos ventana Principal ///////////////////////////////////////////////
        self.cal = Calendar(self.root, selectmode='day', year=2025, month=10, day=13)
        self.label2 = tk.Label(self.root, text="Aqui tienes los eventos del dia", font="Sans", bg="light grey")

      #  img = tk.PhotoImage(file="Fondo1.png")
        self.label1 = tk.Label(self.root, text=" Aqui estan los detalles de evento", font="Sans", bg="light grey",)

        self.text2 = tk.Text(self.root, wrap="word", height=15, bg="light grey")
        self.listbox = tk.Listbox(self.root, selectmode="single", bg="light grey", height=20)
        self.boton1 = tk.Button(self.root)
        self.boton2 = tk.Button(self.root)
        self.boton3 = tk.Button(self.root)
        self.boton4 = tk.Button(self.root)
        key = ExtraerJson.Extraer("Eventos.json")  
        self.key=  list(key["Eventos"].keys()) 
        self.lista = []
        
        
        #////////////////////////////// Elementos de la segunda interfaz ////////////////////////////////////////////////////////////////
        #Esto incluye lo visual de la segunda
        
        self.frame2 = tk.Frame(self.newroot)
        self.frame2.config(height=498,width=1000)
        self.image2 = tk.PhotoImage(file="Fondo2.png",width=1004,height=507,master=self.frame2)
        self.fondo2 = tk.Label(self.frame2,image= self.image2,height=498,width=1000)

        self.frame2.pack()
        self.fondo2.place(in_=self.frame2,x=0,y=0)
        
        self.meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
       # self.mesesDict = {0:"JANUARY",1:"FEBRUARY",2:"MARCH",3:"APRIL",4:"MAY",5:"JUNE",6:"JULY",7:"AUGUST",8:"SEPTEMBER",9:"OCTOBER",10:"NOVEMBER",11:"DECEMBER"}
        self.listbox2V1 = tk.Listbox(self.fondo2)
        self.listbox2V1.config(width=8,height=10,selectmode="multiple")
        self.listbox2V2 = tk.Listbox(self.fondo2)
        self.listbox2V2.config(width=12,height=4,selectmode="multiple")
        self.ListboxMeses()
        self.listbox2V3 = tk.Listbox(self.fondo2)
        self.listbox2V3.config(width=12,height=4,selectmode="single")
        self.MostrarTiposListBox()
        self.listbox2V4 = tk.Listbox(self.fondo2)
        self.listbox2V4.config(width=12,height=4,selectmode="single")
        self.listbox2V5 = tk.Listbox(self.fondo2)
        self.listbox2V5.config(width=12,height=4,selectmode="single")
        self.listbox2V6 = tk.Listbox(self.fondo2)
        self.listbox2V6.config(width=12,height=4,selectmode="single")
        self.listbox2V7 = tk.Listbox(self.fondo2)
        self.listbox2V7.config(width=12,height=4,selectmode="single")
       
        self.diasM = []
        self.diasN = []
        self.tipoDevento = ""
        self.asig = ""
        self.profes = []
        self.profe =""
        self.grupo = ""
        self.grupos =[]
        self.aula = ""
        self.aulas = []
        self.year = ""

        self.listbox2V2.bind("<<ListboxSelect>>", self.EscogerMesesListbox)
      
        self.listbox2V1.bind("<<ListboxSelect>>", self.EscogerDiasListbox)
        self.listbox2V1.bind("<Enter>",self.MostrarDiasListBox)

        self.listbox2V3.bind("<<ListboxSelect>>", self.EscogerTipoListBox)

        self.listbox2V4.bind("<<ListboxSelect>>", self.EscogerAsig)
       # self.listbox2V4.bind("<Enter>",self.MostrarDiasListBox)

        self.listbox2V5.bind("<<ListboxSelect>>", self.EscogerProfe)
        self.listbox2V5.bind("<Enter>",self.MostrarProfe)

        self.listbox2V6.bind("<<ListboxSelect>>", self.EscogerGrupo)
        self.listbox2V6.bind("<Enter>",self.MostrarGrupo)

        self.listbox2V7.bind("<<ListboxSelect>>", self.EscogerAula)
        self.MostrarAula()
      

      

        self.botonCrear = tk.Button(self.fondo2,text="Crear Evento/s",command=self.Generador)
        self.botonR = tk.Button(self.fondo2,command=self.Esconder,height=2,width=5,text="Salir")

        self.text1B = tk.Text(self.fondo2,height=1,width=8)    
        self.text2B = tk.Text(self.fondo2,height=1,width=8)
        self.text3B = tk.Text(self.fondo2,height=1,width=8)

        self.Label1b = tk.Label(self.fondo2,height=2,width=13,text="Introduzca\nla Hora inicial"); self.Label1b.place(in_=self.fondo2,x=15,y=150)
        self.Label2b = tk.Label(self.fondo2,height=2,width=13,text="Introduzca\nla Hora final"); self.Label2b.place( in_=self.fondo2,x=115,y=150)
        self.Label3b = tk.Label(self.fondo2,height=2,width=11,text="Introduzca\n el Ano"); self.Label3b.place( in_=self.fondo2,x=214,y=150)
        self.Label4b = tk.Label(self.fondo2,height=2,width=13,text="Seleccione el\n Mes deseado"); self.Label4b.place( in_=self.fondo2,x=300,y=150)
        self.Label6b = tk.Label(self.fondo2,height=2,width=13,text="Seleccione el\nDia deseado"); self.Label6b.place( in_=self.fondo2,x=399,y=150)
        self.Label7b = tk.Label(self.fondo2,height=2,width=13,text="Seleccione el\ntipo de Clase"); self.Label7b.place( in_=self.fondo2,x=499,y=150)
        self.Label8b = tk.Label(self.fondo2,height=2,width=13,text="Seleccione\nla Asignatura"); self.Label8b.place( in_=self.fondo2,x=598,y=150)
        self.Label9b = tk.Label(self.fondo2,height=2,width=13,text="Seleccione\nel Profe deseado"); self.Label9b.place( in_=self.fondo2,x=698,y=150)
        self.Label10b = tk.Label(self.fondo2,height=2,width=12,text="Seleccione\nel Grupo"); self.Label10b.place( in_=self.fondo2,x=798,y=150)
        self.Label11b = tk.Label(self.fondo2,height=2,width=12,text="Seleccione\nel Aula"); self.Label11b.place( in_=self.fondo2,x=890,y=150)
        
        
        self.text1B.place(in_=self.fondo2,x=30,y=200)
        self.text2B.place( in_=self.fondo2,x=125,y=200)
        self.text3B.place( in_=self.fondo2,x=223,y=200)
        self.botonR.place(in_=self.fondo2,x=900,y=400)
        self.botonCrear.place(in_=self.fondo2,x=450,y=450)
        self.listbox2V2.place(in_=self.fondo2,x=310,y=200)
        self.listbox2V1.place(in_=self.fondo2,x=420,y=200)
        self.listbox2V3.place(in_=self.fondo2,x=510,y=200)
        self.listbox2V4.place(in_=self.fondo2,x=610,y=200)
        self.listbox2V5.place(in_=self.fondo2,x=710,y=200)
        self.listbox2V6.place(in_=self.fondo2,x=805,y=200)
        self.listbox2V7.place(in_=self.fondo2,x=895,y=200)
 
       
        

        #///////////////////////////////////////////////////////////////////// En la principal Configurar el grid /////////////////////////////////////////////////////////////
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=1)

        #///////////////////////////////////////////////// Calendario en la celda (0, 0) ///////////////////////////////////////////////////////////
        self.cal.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        #////////////////////////////////////////////////// Label para decir que son los eventos en ese dia ///////////////////////////////////////////////////
        self.label2.grid(row=0, column=1, sticky="n", padx=10, pady=10)

        #//////////////////////////////////////////////////////////// Label para decir que son la descripcion de eventos /////////////////////////////////////////
        self.label1.grid(row=1, column=1, sticky="n")

        #//////////////////////////////////////////////////////// Bloque de texto 2 en la celda (1, 1)  /////////////////////////////////////////////////////////
        self.text2.insert("1.0", " ")
        self.text2.grid(row=1, column=1, columnspan=1, sticky="")

        #////////////////////////////////////////////////////// Listbox //////////////////////////////////////////////////////////////////////////////////////////
        self.listbox.grid(row=0, column=1, padx=10, pady=10, sticky="sew")
        self.listbox.bind("<<ListboxSelect>>", self.HallarPosicion)
        self.cal.bind("<<CalendarSelected>>", self.HallarDiayMes)

        #/////////////////////////////////////////////// Botones De Salir, Agregar Evento, Eliminar Evento ////////////////////////////////////////////////////////////////
        self.boton1.grid(row=1, column=0, sticky="w")
        self.boton1.config(text="Salir", height=2, width=5, command=lambda: self.root.destroy())
        self.boton2.config(text="Salir")
        self.boton2.config(command=self.Interfaz2 )
        self.boton2.grid(row=1, column=0, sticky="e")

        

    #////////////////////////////////// Metodos del listbox Principal /////////////////////////////////////////////////////////////////////////
    def HallarDiayMes(self, event):
        self.text2.delete(1.0,tk.END)
        self.listbox.delete(0, tk.END)
        self.ListarEventos()

    def HallarPosicion(self, event):
        seleccion = self.listbox.curselection()
        # Aprovecho y ajusto en la misma posicion los detalles de evento
       
        self.text2.delete(1.0, tk.END)
        if len(self.lista)>0:
         self.text2.insert("1.0", f"Evento: {self.lista[seleccion[0]][3]}"
                                 f"\nHora: {self.lista[seleccion[0]][0]} "
                                 f"\nDia: {self.lista[seleccion[0]][1]} / {self.lista[seleccion[0]][2]}"
                                 f"\nProfesor: {self.lista[seleccion[0]][4]}"
                                 f"\nGrupo: {self.lista[seleccion[0]][5]}\nAula: {self.lista[seleccion[0]][6]}")
        
    def ListarEventos(self):

        json = ExtraerJson.Extraer("EventosEjec.json")
        date = datetime.datetime.strptime(self.cal.get_date(), "%m/%d/%y")
        self.lista = []
        for x in range(len(json["Eventos en ejecucion"])):
            if (str(date.month) == json["Eventos en ejecucion"][x][2]) and (
                    str(date.day) == json["Eventos en ejecucion"][x][1]):

                self.listbox.insert(x, f"  {json["Eventos en ejecucion"][x][3]}: {json["Eventos en ejecucion"][x][0]}")
                self.lista += [list(json["Eventos en ejecucion"][x])]

    #///////////////////////////////////////////////////// Metodos de Botones ///////////////////////////////////////////////////////////
    def Esconder(self):
            self.newroot.withdraw()

    def Cerrar(self):
        self.newroot.destroy()
        self.root.destroy()
        
    #////////////////////////////////////   Visual2 ////////////////////////////////////////////////////////////////////////////////// 
    def ListboxMeses(self,event=None):
        for x in range(12):
            self.listbox2V2.insert(x,self.meses[ x])
        self.text2.delete(1.0,tk.END)    

    def DevolverMes(self,event):
        print(self.opciones_meses.get())    
       
    def EscogerMesesListbox(self,event):
         sel = self.listbox2V2.curselection()
         if len(sel)>0:
          l = []
          for x in list(sel):
              l.append(x+1)
          self.diasM = l[:]
         
    def EscogerDiasListbox(self,event):
         sel = self.listbox2V1.curselection()
         if len(sel)>0:
          l =[]
          for x in list(sel):
              l.append(x+1)
          self.diasN = l[:]  
               
    def MostrarDiasListBox(self,event):
        self.listbox2V1.delete(0,tk.END)
        lista = self.diasM[:]
        l = []
        if len(self.text3B.get("1.0","1.end")) == 4 and self.text3B.get("1.0","1.end").isdigit() and int(self.text3B.get("1.0","1.end"))>=2025:
            yearn = int(self.text3B.get("1.0","1.end"))
            self.year = yearn
       # year = datetime.datetime.strptime(self.cal.get_date(),"%m/%d/%y").year[1] 
            for x in range(0,len(lista)):
                l.append(calendar.monthrange(month=lista[x],year=yearn)[1])   
            if len(l)>0:
                   self.diasN = l[:]
                   for x in range(0,min(l)):
                     self.listbox2V1.insert(x,x+1)
    
              

    def MostrarTiposListBox(self):
        json = ExtraerJson.Extraer("Eventos.json")
        for x in json["Eventos"]:
           self.listbox2V3.insert(1,x)

    def EscogerTipoListBox(self,event):
        tipo = self.listbox2V3.curselection()
        if len(tipo) >0:
         self.tipoDevento = self.key[tipo[0]]
         self.listbox2V4.delete(0,tk.END)
         self.MostrarAsig()
        
    def MostrarAsig(self):
          json = ExtraerJson.Extraer("Eventos.json")
          lista = list(json["Eventos"][self.tipoDevento].keys())
          for x in range( len(lista)):
              self.listbox2V4.insert(x,lista[x])
          

    def EscogerAsig(self,event):
         if len(self.listbox2V4.curselection())>0:
           tipo = self.listbox2V4.curselection()[0]
           key = ExtraerJson.Extraer("Eventos.json")  
           key = list(key["Eventos"][self.tipoDevento].keys())
           self.asig = key[tipo] 

    def EscogerProfe(self,event):
         tipo = self.listbox2V5.curselection()
         if len(tipo) >0:
           self.profe = self.profes[tipo[0]]
           self.listbox2V5.delete(0,tk.END)
           self.MostrarProfe()
           
    def MostrarProfe(self,event=None):
           json = ExtraerJson.Extraer("Eventos.json")
           if self.asig and self.tipoDevento != "":
            lista = json["Eventos"][self.tipoDevento][self.asig]['Profes']
            self.profes = lista
            for x in range(len(lista)):
                 self.listbox2V5.insert(x,lista[x])
        

    def EscogerGrupo(self,event):
         tipo = self.listbox2V6.curselection()
         if len(tipo) >0:
           self.grupo = self.grupos[tipo[0]]
           self.listbox2V6.delete(0,tk.END)
           self.MostrarGrupo()

    def MostrarGrupo(self,event=None):
         json = ExtraerJson.Extraer("Eventos.json")
         if self.asig and self.tipoDevento != "":
            lista = json["Eventos"][self.tipoDevento][self.asig]['Grupos']
            self.grupos = lista
            for x in range(len(lista)):
                 self.listbox2V6.insert(x,lista[x])

    def EscogerAula(self,event):
         tipo = self.listbox2V7.curselection()
         if len(tipo) >0:
           self.aula = self.aulas[tipo[0]]
          
    def MostrarAula(self):
         json = ExtraerJson.Extraer("Eventos.json")
         lista = json["Aulas"]
         self.aulas = lista
         for x in range(len(lista)):
                 self.listbox2V7.insert(x,lista[x])             
          
    def ValoresGrid(self):
        for x in range(len(self.meses)):
            self.listbox.insert(x+1,self.meses[x+1]) 

    def Interfaz2(self):
        self.newroot.deiconify()
        self.newroot.mainloop()

    def Generador(self):
        evento = f"{self.tipoDevento} {self.asig}"
        dias = self.diasN[:]
        meses = self.diasM[:]
        year = self.year
        aula = self.aula
        profe = self.profe
        print(year,meses,dias,evento,aula,profe)





class ExtraerJson:
    def Extraer(archivo: str):  # Abre el json, archivo contiene el camino al json
        with open(archivo) as json_file:  # Declara la variable json_file como un json a dict, dandole el valor del json
            json = js.load(json_file)  # json sera igual al valor del json, traducido a diccionario
        return json

    def Escribir(archivo: str, json_nuevo):
        with open(archivo, "w") as json_file:
            js.dump(json_nuevo, json_file)

