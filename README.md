## Idea Específica: Simulador de Comunicación por Cable Ethernet con Codificación Binaria y Ruido Variante para Coordenadas de Aviones

### Fuente de Información:

Utilizando una API que proporciona datos en tiempo real de coordenadas de aviones, se generarán datos de latitud y longitud que representarán la información a transmitir.

### Transmisor:

Los datos de coordenadas de aviones obtenidos se codificarán en formato binario para su transmisión. Además, estos datos se agruparán en paquetes Ethernet estándar, los cuales son comunes en redes de comunicación.

### Canal (Simulador de Cable Ethernet con Ruido Variante):

El canal de comunicación se modelará como un simulador de cable Ethernet, que es una tecnología de transmisión ampliamente utilizada. Se introducirá ruido en el canal, imitando interferencias, cambiando aleatoriamente algunos bits en los paquetes de datos binarios. También se variará la velocidad de transmisión para simular cambios en la calidad de la conexión.

### Receptor:

En el extremo receptor, se implementará la decodificación necesaria para revertir la codificación realizada en el transmisor. Esto permitirá recuperar las coordenadas originales en formato binario.

### Destino de Información:

Una vez recuperadas las coordenadas de aviones, se mostrarán tanto las coordenadas originales obtenidas de la API como las coordenadas recuperadas después de pasar por el proceso de comunicación a través del simulador de cable Ethernet. Este proceso permitirá realizar una comparación visual de las coordenadas para evaluar cómo el ruido en el canal afecta la precisión de los datos.

