# Proyecto CI0110 - Decodificación de Mensajes en Notación Numérica

Este proyecto fue desarrollado como parte del curso de Introducción a la Computación (CI0110) de la carrera de Ciencias de la Computación e Informática en la Universidad de Costa Rica (UCR). Su objetivo principal fue poner en práctica los fundamentos de la lógica algorítmica, el manejo de estructuras de control y la programación funcional utilizando Python nativo.

## Función

Este es un script de Python desarrollado para procesar y decodificar archivos de texto plano que contienen mensajes encriptados en diferentes bases numéricas (Binario, Terciario, Quinario y Hexadecimal). El programa lee las líneas del documento, valida matemáticamente las bases indicadas, convierte los valores a sus correspondientes caracteres ASCII y exporta el mensaje final traducido.

## Características Técnicas

* **Interfaz gráfica de selección:** Implementación de `tkinter` para abrir un explorador de archivos nativo, mejorando la experiencia del usuario.
* **Manejo de excepciones:** Bloques `try...except` para capturar errores de valor (`ValueError`) y evitar caídas del sistema si un dígito no corresponde a la base declarada.
* **Manipulación del sistema de archivos:** Uso de la biblioteca `os` para generar rutas dinámicas y guardar el archivo de salida exactamente en el mismo directorio que el archivo de origen.
* **Limpieza de datos:** Algoritmo optimizado para ignorar líneas en blanco y manejar los espacios entre caracteres.

## Instalación y Requisitos

Este proyecto requiere **Python 3.13** (o superior).

Las bibliotecas utilizadas (`tkinter` y `os`) están integradas de forma nativa en Python, por lo que no es necesario instalar dependencias externas ni utilizar gestores de paquetes como `pip`.

## Formato del Archivo de Entrada

El programa espera un archivo `.txt` donde cada línea inicie con un identificador de base permitido (`B02`, `B03`, `B05` o `B16`), seguido de los valores numéricos separados por espacios.

**Ejemplo:**
```text
B16 A1 48 6F 6C 61 21
B02 1000101 1110011 1110100 1100001
B05 401 430
```

Para correr el script en tu computadora, abre la terminal en la carpeta donde descargaste el repositorio y ejecuta:
```bash
python "Proyecto CI0110.py"
```
* Se abrirá una ventana emergente; selecciona tu archivo .txt codificado.

* Revisa la consola para ver el texto decodificado y cualquier advertencia sobre dígitos incorrectos.

* El programa te preguntará si deseas guardar el resultado. Digita Sí para generar el archivo Mensaje decodificado.txt en tu carpeta local.


## Autor

* **David Zuñiga** - *Estudiante de Ciencias de la Computación e Informática (UCR)*
* **LinkedIn:** [Conecta conmigo en LinkedIn](https://www.linkedin.com/in/david-z%C3%BA%C3%B1iga-torres-872136324/)
* **GitHub:** [Visita mi perfil de GitHub](https://github.com/davidzu7sc/)

* **Año:** 2026