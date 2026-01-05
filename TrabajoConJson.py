import json as js
class ExtraerJson:
   def Extraer(archivo:str): #Abre el json, archivo contiene el camino al json
     with open(archivo) as json_file: #Declara la variable json_file como un json a dict, dandole el valor del json
         json = js.load(json_file) #json sera igual al valor del json, traducido a diccionario
         
     return json
   
   def Escribir(archivo,json_nuevo):
      with open(archivo,"w") as json_file:
         js.dump(json_nuevo,json_file)
         