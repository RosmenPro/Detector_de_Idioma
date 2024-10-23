"""Detector de Idioma
En este proyecto utilizarás el módulo "langdetect" para ayudarnos a identificar el idioma que
se ha ingresado. Esto puede ser realmente útil si no estás seguro de qué idioma estás
tratando.
Puedes crear también una GUI sencilla para interactuar con el usuario. Después puedes
recopilar el texto del campo de entrada y procesarlo con "langdetect" para determinar qué
idioma se ingresó. Finalmente, puedes imprimir este resultado en la GUI para informar al
usuario sobre el resultado.
Ten en cuenta que los resultados devueltos por "langdetect" son códigos abreviados de
idioma. Por ejemplo, si ingresamos texto en inglés, veremos 'en' como el valor de retorno."""

import tkinter as tk
from langdetect import detect, LangDetectException

def detect_language():
    text = entry.get().strip()  # Obtener y limpiar el texto ingresado por el usuario
    min_characters = 20  # Definir el número mínimo de caracteres para detectar el idioma
    if len(text) >= min_characters:  # Comprobar si el texto tiene al menos el número mínimo de caracteres
        try:
            detected_language = detect(text)  # Detectar el idioma del texto utilizando la función detect
            result_label.config(text=f"Idioma detectado: {detected_language}")  # Configurar la etiqueta de resultado para mostrar el idioma detectado
        except LangDetectException:
            result_label.config(text="No se pudo detectar el idioma, por favor intente con más texto.")  # Manejo de excepción en caso de error de detección
    else:
        result_label.config(text="Texto demasiado corto para detectar el idioma")  # Configurar la etiqueta de resultado si el texto es demasiado corto

root = tk.Tk()  # Crear la ventana principal de la interfaz gráfica de usuario
root.title("Detector de Idioma")  # Establecer el título de la ventana

label = tk.Label(root, text="Ingrese el texto:")  # Crear una etiqueta para instruir al usuario
label.pack(pady=5)  # Colocar la etiqueta en la ventana y establecer un espacio vertical de 5 píxeles

entry = tk.Entry(root, width=50)  # Crear un campo de entrada para que el usuario ingrese el texto
entry.pack(pady=5)  # Colocar el campo de entrada en la ventana y establecer un espacio vertical de 5 píxeles

detect_button = tk.Button(root, text="Detectar Idioma", command=detect_language)  # Crear un botón para iniciar la detección del idioma
detect_button.pack(pady=5)  # Colocar el botón en la ventana y establecer un espacio vertical de 5 píxeles

result_label = tk.Label(root, text="")  # Crear una etiqueta para mostrar el resultado de la detección del idioma
result_label.pack(pady=5)  # Colocar la etiqueta de resultado en la ventana y establecer un espacio vertical de 5 píxeles

root.mainloop()  # Iniciar el bucle principal de la interfaz gráfica de usuario