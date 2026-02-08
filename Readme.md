# Archivos de Hallowneest: Organizador de Eventos
## Descripcion
Aplicacion desarrollada en python con una interfaz grafica desarrollada en tkinter para una gestion de eventos. Este proyecto permite crear, revisar eventos en el tiempo y buscar el tiempo más eficiente para un evento

## Dominio:
El dominio se basa en la gestion administrativa de un Reino que se recupera de una crisis. Este dominio fue escogido debido a la amplia posibilidad de creacion de eventos, pudiendo planificar guardias, construcciones y visitas sociales por parte de los funcionarios del Reino. Brindando un acercamiento a la idea de organizacion de recursos a nivel institucional

##  Interfaces Principales:
- Menu de Inicio: Pagina de bienvenida que te permite visualizar los eventos del dia deseado, incluido la capacidad de eliminarlos
- Primer Menu de Creacion: Menu que te permite creaar los eventos
- Segundo Menu de Creacion: Menu que aparece al ocurrir choques de recursos entre eventos, permitiendote elegir que hacer con dichos eventos

## Funcionalidades principales:
- Creacion de Eventos
- Eliminacion de Eventos
- Visualizacion de un calendario con los eventos de un dia
- Total Libertad a la hora del manejo de colisiones de recuros
- Posibilidad de eventos recurrentes
- Posibilidad de crear hasta 365 eventos en diferentes dias y meses con un solo click

## Estructura
- EventosEjec.json : Base de datos de eventos activa, cualquier base de datos que se cargue, debe cumplir los requerimientos en requisitos
- Inventario.json : Base de datos de inventario activa, esta base de datos no debe cambiarse
- Main.py : Contiene el grueso del proyecto. Constituye la interfaz visual, y las funcionalidades de los botones. El proyecto se inicia aquí
- TrabajoConDateTime.py : Contiene una clase con diferentes funciones, su funcion es la validacion de fechas y devolucion de formatos fecha
- TrabajoConJson.py : Contiene una clase para extraer y escribir en la base de datos
- Trabajar.py : Segunda archivo más importante del proyecto, contiene la logica de colision de eventos, esta se divide en revisar si el evento puede ocurrir sin colision de eventos, si no es posible devolverle al usuario que eventos no lo permitieron y buscar un hueco donde el evento pueda ocurrir

## Dependencias
- Python 3.8 o mayor
- CustomTkinter: interfaz grafica
- Json
- datetime
- Calendar
- copy
- tkcalendar
- math

## Restricciones Implementadas
Estos ocurren entre recursos del tipo Personajes:
- Restricciones del tipo "AND":
Si esta un personaje, entonces debe estar otro, obligatoriamente. Ejemplo: Si un recurso tiene a Ogrim, debe tener a Isma, en este caso pasa tambien pero no neceariamente es doble via, osea las restricciones "And" son en un solo sentido
- Restricciones del tipo "OR":
Si esta un personaje, entonces tiene una lista de personajes, si este personaje participa en un evento,entonces debe participar minimo uno de su lista. Ejemplo: Si Hollow Kight participa en un evento, entonces o Hornet o el Rey Palido deben estar
- Restriccion del tipo "NAND":
Este ocurre entre personajes, recursos y tipos. Si un objeto, sea personaje, tipo o recurso, esta presente, otro no. Ejemplo: Ogrim no puede realizar eventos en Ciudad de Lagrimas

