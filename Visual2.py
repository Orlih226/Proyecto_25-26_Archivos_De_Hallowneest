import datetime
import customtkinter as ctk
import calendar

class SegundaVentana:
     def __init__(self, root:ctk.CTk):
        self.root = root
        self.Interfaz()
     def Interfaz(self):
         self.root.maxsize(1200,700)
         self.root.minsize(1200,700)


            
r1 = ctk.CTk()
r2 = SegundaVentana(r1)
r1.mainloop()