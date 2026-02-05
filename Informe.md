## Eventos:
- Los eventos estan conformados de la siguiente forma:
["Nombre","Hora","Mes","Dia",["Recursos de Personal"],["Recrusos de Lugar"]]
Osea decidi que cada evento fuera tratado como una lista, preferi hacerlo directamente como una lista, ya que es un tipo de dato primitivo de python, en vez que definir una clase y su constructor para definirlo

## Validacion 
- La validacion de un evento tiene varias capas:
1- Validacion de Datos
2- Validacion de Restricciones
3- Validacion de Entrada

### Validacion de Datos:
- Esta se encuentra en el archivo Main, se basa en recibir los datos de manera correcta, osea que cada elemento introducido en la lista este en el formato correcto
#### Procesos de Validacion de Datos
- Nombre: Todo nombre es valido, en el codigo no es tomado en cuenta, solo se usa para que el usuario encuentre el eveno deseado cuando lo busque
- Hora: El usuario introduce una hora inicial y una hora final, estos deben estar en formato 24h. Ejemplo: 11:00, 22:23. (No es valido el 00:00 ni 24:00). Estos se almacenan en un string de forma: "horaInicial a horaFinal'
- Mes: La entrada del mes es especial, los datos deben introducirse en uno debajo del otro, separados por Enter, si hay un espacio vacio entre estos o despues de estos, se ignorara
- Dias: La entrada del dia es especial, los datos deben introducirse separados por comas sin espacios
- *Sinergia del Dia-Mes:
Aqui ocurre algo curioso, se pueden introducir tantas lineas de dias como desee el usuario. El proceso base es el siguiente
Linea del Mes -> Linea del Dia
Ejemplo:
1 -> 1,2,3,4,5
2 -> 4,5
Aqui se crearan 5 eventos individuales en enero, con los mismos recursos, en esos dias y dos eventos en los dias 4 y 5
El programa hara eso con cada linea del mes con cada linea del dia, mientras haya igual cantidad
- Si hay mas LM que LD:
El programa hara la operacion base, hasta quedarse acabarse las lineas de dias, luego las demas lineas de meses estaran relacionadas con la ultima linea de dias
- Si hay mas LD que LM:
Si hay mas lineas de dias que de meses, el programa hara la operacion base, y luego le otorgara todas las lineas de disa que sobran al ultimo mes

#### Procesos de Validacion de Restricciones
- La validacion de Restricciones ocurre en el archivo Main, donde se reciben los datos, por las funciones que revisan la entrada de los propios archivos
- Estas revisan las restricciones que tiene el json inventario, y solo ocurre entre los lugares y los recursos
- Reglas:
- Dos lugares no pueden ser asignados al mismo evento
- Entre los personajes ocurren sinergias, si la sinergia no es valida, entonces el evento no es valido (Listas de sinergias)
- Entre los personajes y los tipos hay relaciones establecidas, algunos no pueden cumplir cierto tipo de tareas
- Entre los lugares y los personajes hay relaciones establecidas, ciertos personajes no pueden estar en ciertas areas

##### Personajes y Lugares y Tipos:
- Entre los personajes ocurren diferentes restricciones ya explicadas anteriormente, las "AND", "OR" y "NAND".
- En Inventario.json se encuentran las restricciones entre ellos, esta se representan de dos formas: "Dependencia" e "Incapacidad"
- "Incapacidad", el motor impulsor de las Restricciones "NAND", cuandoo se introduce un objeto, personaje o lugar, se revisan estas restricciones, y su funcionamiento es que si esta el personaje, en la lista no puede estar ninguna otra, esto se revisa de la siguiente manera, cuando uno introduce un evento, se guardan los recursos usados, y se recorre por la lista de recursos del propio evento, si alguno esta en las restricciones del otro, devuelve que es invalido
- "Dependencia" se encarga de las instruccciones "AND"y "OR", el codigo recibe una lista con dos elementos,e l primero es un numero, 1 o 0 y el segundo sus restricciones, si es un 1 el codigo revisa que esten todos los elementos de esa lista, lo hace pasando esa lista por la de recursos, si uno no esta, da un break y devuelve false. Si es un 0, lo trata como un o, en el codigo, pasa por la lista de recursos y devuelve un True siempre que encuentre alguna de la lista de necesidad, si la lista no posee True, da un break y devuelve false

### Proceso de Validacion de Entrada:
- El proceso de entrada se basa en la revision de fechas:
- El programa accede a la llave con el valor del ano, y luego al de valor del mes, luego revisa si tienen el mismo dia y luego revisa si choca tiempos, si chocan los tiempos, revisa si tienen recursos comunes, si tienen al menos un recurso comun, lo manda a la funcion para validarlos.
- Si la llave del ano no esta, crea una llave con el ano, otra interna con el mes y le introduce el evento
- Si la llave del mes no esta, crea una llave con el mes en la llave del ano y le introduce el evento

# Validar Eventos:
- La funcion de Validar es una funcion recursiva, esta recibe el evento que no se pudo introducir, y el evento que no permitio que se introduciera. Obtiene la duracion del evento, y coloca de nueva fecha la fecha final del evento que no le permitio como fecha inicial, y de final la anterior + la duracion del evento
- Si este formato se pasa de tiempo, osea si el evento pasa de 24h, el evento se corre automaticamente a las 3am del otro dia como fecha inicial y como final 3am + duracion

## Almacenamiento de Datos:
- El json esta formado de la siguiente manera:
{
    "Eventos en Ejecucion":
    {
        "Años":
         {
            "Meses del Año":[ [Eventos del Dia] ]
         }
    }
}
- Esta forma de asumir el json fue basada en la idea de la velocidad al acceder a un diccionario. La ventaja de este formato, es que si deseo acceder a los eventos de un mes o de un año, es tan facil como buscar las llaves [Año][Mes], en vez que recorrer todo el json, o que organizar los elementos del json, o crear un id basado en la fecha/recursos

## Cuellos de Botella
- Como el codigo puede manejar tantos eventos a la vez, cargar y descargar la base de datos seria contraproducente. La solucion implementada se basa en el juego Fallout, se hace una copia de la base de datos en un diccionario de python, y se trabaja con este. Para mantener la persistencia de datos, la base de datos se actualiza cuando pasas de la interfaz de Creacion a la de Menu y viceversa, y cuando se cierra el programa, sacrificando un poco de velocidad del programa para garantizar la integridad





