# Detector de Idioma

Este proyecto es una aplicación gráfica que detecta el idioma del texto ingresado por el usuario. Utiliza el módulo `langdetect` para identificar el idioma, mostrando el código del idioma detectado en la interfaz gráfica. Por ejemplo, si se ingresa texto en inglés, la aplicación mostrará 'en' como el idioma detectado.

## Funcionalidades

- **Entrada de Texto**: El usuario puede ingresar cualquier texto.
- **Detección de Idioma**: La aplicación detecta el idioma y muestra un código abreviado (por ejemplo, 'en' para inglés, 'de' para alemán).
- **Manejo de Errores**: Si el texto es demasiado corto o no se puede detectar el idioma, la aplicación mostrará un mensaje apropiado.

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado:

- Python 3.x
- Tkinter (generalmente incluido con Python)
- El módulo `langdetect`

Puedes instalar el módulo `langdetect` ejecutando el siguiente comando:

```bash
pip install langdetect
```
## Instalación y Uso
1. Clona este repositorio o descarga los archivos.
2. Asegúrate de tener instalado langdetect y Tkinter.
3. Ejecuta el script de la siguiente manera:
  python detector_idioma.py
4. Ingresar el texto en el campo de entrada de la ventana que aparece.
5. Presiona el botón Detectar Idioma para obtener el resultado del idioma detectado.

## Contribuir
Si tienes alguna sugerencia o mejora, siéntete libre de crear un pull request o abrir una issue en el repositorio.
