# Esquema del Canal de Comunicación Simulado

## Telescopio Espacial a Estación Espacial

### Fuente de Información:
- El telescopio captura datos científicos como imágenes y espectros de luz de objetos celestes.
- Los datos se convierten en matrices numéricas para su transmisión.

### Emisor:
- Las matrices de datos se empaquetan en un formato adecuado para la transmisión.
- Los valores numéricos se convierten en una secuencia de bits utilizando codificación.

### Canal de Transmisión en Espacio Profundo:
- El "canal" en esta simulación se refiere al espacio profundo a través del cual se transmiten las señales.
- No es un medio físico como un cable, sino el espacio mismo que atraviesa la señal durante su viaje.
- El tipo de señal transmitida es **una señal electromagnética**, consistente en ondas electromagnéticas que transportan los datos desde el telescopio a la estación espacial.
- Fuentes de Ruido:
  - Ruido Térmico o Johnson-Nyquist
  - Ruido de Fondo Cósmico
  - Radiación Cósmica
  - Ruido de Interferencia Electromagnética (EMI)
  - Ruido de Amplitud y Fase Aleatoria

### Receptor:
- El receptor recibe la señal con ruido después de su travesía por el canal.
- Aplica algoritmos de corrección de errores y detección de errores para mitigar el efecto del ruido.
- Decodifica la secuencia de bits para reconstruir las matrices de datos originales.
- Almacena la imagen reconstruida a partir de los datos decodificados.

