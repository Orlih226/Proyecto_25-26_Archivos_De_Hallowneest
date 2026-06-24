## Eventos:
- Los eventos estan conformados de la siguiente forma:
["Nombre","Hora","Mes","Día",Año,["Recursos de Personal"],["Recrusos de Lugar"]]
Osea se decidió que cada evento fuera tratado como una lista, se prefirió hacerlo directamente como una lista, ya que es un tipo de dato primitivo de python, en vez que definir una clase y su constructor para definirlo

## Validacion 
- La validación de un evento tiene varias capas:
1- Validación de Datos
2- Validación de Restricciones
3- Validación de Entrada

### Validacion de Datos:
- Esta se encuentra en el archivo Main, se basa en recibir los datos de manera correcta, osea que cada elemento introducido en la lista esté en el formato correcto
#### Procesos de Validacion de Datos
- Nombre: Todo nombre es válido, en el código no es tomado en cuenta, solo se usa para que el usuario encuentre el eveno deseado cuando lo busque
- Hora: El usuario introduce una hora inicial y una hora final, estos deben estar en formato 24h. Ejemplo: 11:00, 22:23. (No es válido el 00:00 ni 24:00). Estos se almacenan en un string de forma: "horaInicial a horaFinal'
- Mes: La entrada del mes es especial, los datos deben introducirse en uno debajo del otro, separados por Enter, si hay un espacio vacío entre estos o despues de estos, se ignorará
- Días: La entrada del día es especial, los datos deben introducirse separados por comas sin espacios
- *Sinergia del Día-Mes:
Aquí ocurre algo curioso, se pueden introducir tantas líneas de días como desee el usuario. El proceso base es el siguiente
Línea del Mes -> Línea del Día
Ejemplo:
1 -> 1,2,3,4,5
2 -> 4,5
Aquí se crearan 5 eventos individuales en enero, con los mismos recursos, en esos días y dos eventos en los días 4 y 5
El programa hara eso con cada línea del mes con cada línea del día, mientras haya igual cantidad
- Si hay más LM que LD:
El programa hara la operacion base, hasta quedarse acabarse las líneas de días, luego las demás líneas de meses estaran relacionadas con la ultima línea de días
- Si hay más LD que LM:
Si hay más líneas de días que de meses, el programa hara la operacion base, y luego le otorgara todas las líneas de disa que sobran al ultimo mes

#### Procesos de Validacion de Restricciones
- La validacion de Restricciones ocurre en el archivo Main, donde se reciben los datos, por las funciónes que revisan la entrada de los propios archivos
- Estas revisan las restricciones que tiene el json inventario, y solo ocurre entre los lugares y los recursos
- Reglas:
- Dos lugares no pueden ser asignados al mismo evento
- Entre los personajes ocurren sinergias, si la sinergia no es valida, entonces el evento no es valido (Listas de sinergias)
- Entre los personajes y los tipos hay relaciones establecidas, algunos no pueden cumplir cierto tipo de tareas
- Entre los lugares y los personajes hay relaciones establecidas, ciertos personajes no pueden estar en ciertas areas

##### Personajes y Lugares y Tipos:
- Entre los personajes ocurren diferentes restricciones ya explicadas anteriormente, las "AND", "OR" y "NAND".
- En Inventario.json se encuentran las restricciones entre ellos, esta se representan de dos formas: "Dependencia" e "Incapacidad"
- "Incapacidad", el motor impulsor de las Restricciones "NAND", cuando se introduce un objeto, personaje o lugar, se revisan estas restricciones, y su funciónamiento es que si esta el personaje, en la lista no puede estar ninguna otra, esto se revisa de la siguiente manera, cuando uno introduce un evento, se guardan los recursos usados, y se recorre por la lista de recursos del propio evento, si alguno esta en las restricciones del otro, devuelve que es invalido
- "Dependencia" se encarga de las instruccciones "AND"y "OR", el código recibe una lista con dos elementos,e l primero es un numero, 1 o 0 y el segundo sus restricciones, si es un 1 el código revisa que esten todos los elementos de esa lista, lo hace pasando esa lista por la de recursos, si uno no esta, da un break y devuelve false. Si es un 0, lo trata como un o, en el código, pasa por la lista de recursos y devuelve un True siempre que encuentre alguna de la lista de necesidad, si la lista no posee True, da un break y devuelve false

### Proceso de Validacion de Entrada:
- El programa accede a la llave con el valor del año, y luego al de valor del mes, luego revisa si tienen el mismo día y luego revisa si choca tiempos, si chocan los tiempos, revisa si tienen recursos comunes, si tienen al menos un recurso comun, lo manda a la función para validarlos.
- El proceso de entrada se basa en la revisión de fechas:
- Si la llave del año no esta, crea una llave con el año, otra interna con el mes y le introduce el evento
- Si la llave del mes no esta, crea una llave con el mes en la llave del año y le introduce el evento

# Validar Eventos:
- La función de Validar es una función recursiva, esta recibe el evento que no se pudo introducir, y el evento que no permitio que se introduciera. Obtiene la duracion del evento, y coloca de nueva fecha la fecha final del evento que no le permitio como fecha inicial, y de final la anterior + la duracion del evento
- Si este formato se pasa de tiempo, osea si el evento pasa de 24h, el evento se corre automaticamente a las 3am del otro día como fecha inicial y como final 3am + duracion

## Almacenamiento de Datos:
- El json esta formado de la siguiente manera:
{
    "Eventos en Ejecucion":
    {
        "Años":
         {
            "Meses del Año":[ [Eventos del día] ]
         }
    }
}
- Esta forma de asumir el json fue basada en la idea de la velocidad al acceder a un diccionario. La ventaja de este formato, es que si deseo acceder a los eventos de un mes o de un año, es tan facil como buscar las llaves [Año][Mes], en vez que recorrer todo el json, o que organizar los elementos del json, o crear un id basado en la fecha/recursos

## Cuellos de Botella
- Como el código puede manejar tantos eventos a la vez, cargar y descargar la base de datos seria contraproducente. La solucion implementada se basa en el juego Fallout, se hace una copia de la base de datos en un diccionario de python, y se trabaja con este. Para mantener la persistencia de datos, la base de datos se actualiza cuando pasas de la interfaz de Creacion a la de Menu y viceversa, y cuando se cierra el programa, sacrificando un poco de velocidad del programa para garantizar la integridad

## Experiencias:
- Durante el desarrollo hubo sus altibajos, principalmente la perida de un de entre un 40 y un 50 % del codigo, dos veces, este se debio principalmente a que se realizaron pull en vez que push, y sincronizo los cambios antiguos que ya estaban en github con los nuevos, lo que elimino horas de desarrollo
- Ademas debido al sistema de tkinter, no tenia ciertas comodidades a la hora de la belleza visual, por lo tanto tuve que reescribir el codigo, pasandolo de tkinter a customtkinter, y con este cambio, se vio en la necesidad de cambiar aproximadamente un 90% del proyecto,
- Ademas hubo problemas serio a la hora de validar eventos, debido a que al usar listas de listas, estas se copiaban por referencia, y al cambiarla, se cambiaba el evento en la base de datos fantasma

# Explicacion resumida del funcionamiento:
- Cuando entras, se despliega un calendario que muestra los dias de un mes, y un año, si tocas algun dia, este accede a los valores de la base de datos que poseean esta coincidencia, y te muestra una lista con el nombre
- Borrar el año borra la llave del año de la base de datos local o fantasma
- Borrar  el mes cumple el mismo proposito, pero con el mes
- Borrar el día, accede a la llave de año y mes, luego como solo puede haber un evento con las mismas caracteristicas, busca el indice de este y lo devuelve
- Crear te lleva a la otra interfaz
- Al escribir una fecha, una funcion revisa que poseea un len mayor que 0 y menor que 6, si pasa esto, revisa si la funcion que transforma de str a datetime es posible, si puede devuelve las horas. Luego revisa si la final es mayor que la inicial
- Luego revisa si el año esta entre 2025 y 9999, y si es un año valido, osea un número
- Luego revisa los meses, si la entrada es como lo describe el informe, lo acepta, si en una linea hay prescencia de comas, usara el primer elemento si es valido
- Lo mismo ocurre con los días, excepto en la parte de las comas, recibira todos los validos, aunque anunciara el error
- 



