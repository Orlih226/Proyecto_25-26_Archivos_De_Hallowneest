# Archivos de Hallowneest: Planificador de Eventos
## Manual de Bienvenida al Usuario:
### Bienvenida:
Hola nuevo escribano al servicio del Rey, soy yo Monomon, la sonadora, espero que estes a gusto en tu nuevo trabajo. Vamos a darte un breve recordatorio sobre lo que ha pasado ultimamente. Como sabes el Caballero sometio al Destello, provocando la liberacion del Reino. Nuestro Rey y Reina han regresado, y han sacrificado parte de sus poderes para poder revivir a los Caballeros Reales, y otorgarle vida al Hollow Knight. 
### Eres nuevo en Hallowneest?
Hallowneest es el Reino donde estas ahora, este posee diferentes zonas donde descansar, una vez que termines el trabajo por supuesto, te recomiendo visitar la Ciudad de Lagrimas (Lleva una sombrilla). Este reino esta integrado por insectos, y seres de vacio, entre sus principales tribus esta Las Mantis, Las Abejas, Los Seres Palidos, Los Seres Vacios, Los insectos del Reino.
### Objetivo:
Tu papel como escribano es ver los eventos que necesiten realizarse y subirlos a la base de datos, como sabemos que por problemas energeticos del Reino, por la muerte de Unn, se ha permitido poner eventos del ano pasado, o de dias anteriores al actual. Se te brindara una guia con imagenes de como hacerlo 

## Guia de Trabajo
Buenos vamos al rollo, abre el archivo main para iniciar la aplicacion

### Menu
Cuando lo hagas te saldra el Menu de bienvenida. En este tendremos diferentes botones visibles, en la parte inferior izquierda uno que dice "Crear" y otro que dice "Salir", el de Crear te lleva al Menu de Creacion de Eventos, el de Salir es literal. En la esquina inferior izquierda tienes 3 botones, "Borrar evento" para que este boton tenga resultado, debes seleccionar un evento, como?, pues en el calendario a la izquierda, dispones de  lo necesario, muevete por los meses, dias y anos que desees revisar los eventos disponibles, si tocas un dia con evento, en la esquina superior derecha te saldra una lista desplegable que al tocarla te ensenara los eventos del dia, cuando toques uno saldra su descripcion en pantalla, en el textbox abajo al fondo, ahi sabras que esta seleccionado, los otros funcionan dependiendo del mes/ano en el que este el calendario posicionado ///OJO/// si borras un evento, no poras recuperlo, deberas crearlo otra vez

### Creacion
Bueno accediste al Menu de Creacion, aqui las cosas se ponen mas interesantes:
Los campos que tienes diferentes cajas de texto para rellenar, debe poner la informacion correcta en cada una, o el programa no hara nada, hay casos como poner dias o meses negativos, o fuera de convencion, que el programa simplemente ignorara el dia con error, mientras haya otro valido
La entrada de datos:
Ambas horas se deben asignar en formato 24h, osea 12:00 por ejemplo, el programa no recibira las horas 00:00, ni 24:00, cualquiera fuera de ese formato sera invalido, cuidado con dejar espacios antes o despues de la hora, solo debe estar la hora
El ano, debido a los problemas antes mencionados, el limite inferior de anos validos es 2025, puede programar eventos hasta un maximo de 9999
El mes, el mes tiene una forma especial de recibir entrada, los meses se separan por espacios de tipo enter, osea pones un numero, tocas enter y pones otro, de forma que haya un solo caracter en la linea, si no sigue este formato, no espere que su evento se escriba en la base de datos
Los dias tambien son especiales, deben escribirse separados por coma, ejemplo: 1,2,3,4,5
Aqui ocurre una sinergia especial entre dias y meses
Como los meses se separan por lineas, usted puede jugar con esto, el programa hara lo siguiente:
Primera linea de mes - Primera linea de dias
Asi con todos los meses, lo que le permite introducir un mismo evento en diferentes meses y dias a la vez, genial no?.
Esto tiene un truco curioso
Si pone mas lineas de dias que de mes, el programa tendra el mismo comportamiento, pero cuando acaben los meses, las demas lineas de dias, se le corresponderan al ultimo mes
Si hay mas L-M, que L-D, entonces pasara lo mismo del caso base, y cuando se acaben los dias, los meses que siguen se les corresponde la ultima fila de dias que aparezca
El nombre del evento no posee restriccion
Los tipos de eventos que aparecen no tienen perdida, solo debe escoger uno solo para representar un evento
Los personajes tampoco tienen perdida, puede seleccionar varios a la vez
Los lugares cumplen la misma propiedad de los tipos, solo seleccione uno
*Los errores se te anunciaran en la pantalla, estos cumplen una prioridad de error, primero seran los de Hora
*Hay combinaciones de recursos invalidas, explorelo mas abajo

### Segunda Creacion
Suponiendo que lo hayas hecho todo perfecto, esto no garantiza que el evento se introduzca al sistema. Pueden ocurrir COLISIONES, osea que dos recursos se usen a la vez. 
Aqui hay diferentes botones que le permitiran ver, las instrucciones son directas, y cumplen lo que dicen. La que hablare es "Seleccionar Validados"
Aqui otra interfaz se muestra en pantalla, esta posee tres botones, inscribir todos te inscribira los validados y los que pasaron a la primera, inscribir seleccionados te permitira decidir cuales quieres inscirbir,junto con los validos, y no inscribir te mandara directo al menu de creacion

## Descripcion:
Sistema desarrollado en Python para la gestion y organizacion de eventos de interes para el Palacio Blanco, capital del Reino de  Hallowneest.

## Eventos:
Los eventos a su disposicion son personalizables por los escribas, usuarios de la aplicacion, teniendo la posibilidad de nombrar el eventos y asignar quienes se encargaran de hacerlo, donde lo haran y con que enfoque deben hacerlo

## Recursos:
Los recursos se dividen en dos tipos, recursos de lugar y recursos de brigada.
En los recursos de brigada tenemos, a las brigadas de construccion y mineria reales, a nuestros fieles caballeros reales, a el principe y la princesa del reino, a el cartografo real y al propio rey. En los recursos de lugares tenemos a los diferentes zonas de nuestro Reino.

## Personajes:
Brigada de construccion
Brigada de Mineria
Ogrim
Isma
Hegemol
Doliente Gris
Hornet
Hollow Knight
Rey Palido

## Lugares:

## Restricciones:
Debido a la naturaleza de ciertas zonas, preferencias de ciertos caballeros y necesidades de los subditos, se integro un sistema de de cancelacion automatica, que no permite la entrada de un evento que no cumpla los requisitos de restriccion. Aqui les traigo las restricciones decididas:
### Personajes
-Ogrim: Debido a su caracter, Ogrim debe estar siempre emparejado con Isma, quien controla sus actos heroicos fuera de lugar. Ademas Ogrim puede realizar todas los tipos de actividades, excepto mineria, la cual no se le da nada bien. 

-Isma: Isma, siendo la unica capaz de controlar, soportar, el suficiente tiempo a Ogrim, esta obligada a siempre estar con el, por lo tanto si esta Isma esta Ogrim, obligacion que agradece mucho.

-Hegemol: Debido a su armadura, hegemol no es el mas agil, tiene la confianza suficiente del Rey para encargarse de ls tareas solo, sin embargo no puede realizar ninguna de tipo de acividad del tipo: "Mantenimiento","Exploracion","Mineria","Recoleccion"

-Doliente Gris: Aguda espadachin con grandes dotes marciales, jardineros y administrativos. El unico inconveniente es su su negacion a participar en actividades como "Mineria","Mantenimiento","Construccion", debido a que no lo ve como digno de ella

-Brigada de Construccion: La Brigada de Construccion Real, esta constituidas por los insectos mas habiles graduados de la Facultad de Ciudad de Lagrimas. Esta no necesita estar acompanada por ningun personaje, pues se le ofrece proteccion de los habitantes de las zonas, debido al Ultimo Trataddo de Expansion Territoral del Reino, esta solo es capaz de realizar "Mantenimiento" y "Construccion"

-Brigada de Construccion: La Brigada de Mineria Real, es graduada al mismo nivel a la Brigada de Construccion Real y en el mismo Instituto, esta solo puede hacer "Mineria", como actividad

-Cornifer: Nuestro Cartografo Real, durante la caida del Reino ayudo al heroe, a moverse por el mapa, cartografiando todo el Reino por el. Cornifer puede realizar actividades solos, el conseguira los recursos, pero por peticion de la Reina, uno de los caballeros reales o la princesa debe estar con el. No puede participar en activiades del tipo: "Combate","Guardia","Relaciones"

-Hornet: Princesa del Reino, conocida como la Sentinela, el Vigia, ella no posee restricciones de ningun tipo de actividad, sin embargo, el Rey no la deja participar en actividades del tipo: "Mineria","Mantenimiento","Construccion"

-Hollow Knigth: Principe Caiddo del Reino, amado por el pueblo, pero el idioma que habla es imposible de entender por cualquier ser no vacio, por lo tanto la Princesa o el Rey deben ir con el, no puede realizar las siguientes activades debido a que no es capaz de dirigir: "Mineria","Mantenimiento","Construccion"

-Rey Palido: El Rey de Hallownest, es considerado una insecto evasivo, pero eso era en otra era, luego de la victoria sobre el Destello este decidio involucrarse mas con sus subditos, a pesar de fundar el Palacio el solo, ha perdido sus habilidades, por lo tanto no puede realizar ninguna del tipo: "Mantenimiento","Exploracion","Recoleccion","Guardia","Mineria","Construccion". Este ademas debe ser acompanado por algun Caballero Real o la Princesa o el Hollow Knight
### Lugares:






