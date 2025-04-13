Edición de Imágenes con OpenAI
Este proyecto permite editar imágenes utilizando la API de OpenAI. El script procesa una imagen de entrada, redimensionándola a 1024x1024 píxeles (si es necesario), crea una máscara personalizada y utiliza un prompt definido en un archivo de texto para modificar la imagen mediante la API.

Descripción
El proceso básico del proyecto es el siguiente:

Carga de Configuración: Se utilizan variables de entorno (con dotenv) para gestionar la clave API (OPENAI_API_KEY).

Preparación de la Imagen: Se comprueba la existencia de la imagen de entrada (img.png) y se ajusta al tamaño requerido (1024x1024) si no cumple con la condición.

Creación de Máscara: Se genera una máscara donde la mitad superior permanece opaca y la inferior se hace transparente. Esto define el área a editar.

Obtención del Prompt: Se lee el archivo prompt.txt dentro del directorio prompts para obtener el mensaje que guiará la edición.

Edición de la Imagen: Se utiliza el método images.edit de la API de OpenAI para aplicar el prompt a la imagen, enviando tanto la imagen original como la máscara.

Descarga y Visualización: Se descarga la imagen editada y se guarda en la carpeta images, mostrando finalmente el resultado al usuario.

Requisitos
Python 3.x

python-dotenv

Pillow

requests

OpenAI Python Client

Instalación
Clonar el repositorio:

bash
Copy
git clone <URL-del-repo>
cd <nombre-del-repo>
Crear y activar un entorno virtual (opcional pero recomendado):

bash
Copy
python -m venv venv
source venv/bin/activate   # En Linux/macOS
venv\Scripts\activate      # En Windows
Instalar las dependencias:

bash
Copy
pip install -r requirements.txt
Configurar las variables de entorno:
Crea un archivo .env en la raíz del proyecto y agrega la siguiente línea con tu clave API:

env
Copy
OPENAI_API_KEY=tu_api_key
Uso
Coloca la imagen que deseas editar en la raíz del proyecto con el nombre img.png.

Asegúrate de tener un archivo prompt.txt en el directorio prompts con el mensaje que dirigirá la edición.

Ejecuta el script:

bash
Copy
python <nombre_del_script>.py
La imagen editada se guardará en la carpeta images y se mostrará automáticamente.

Notas
El script ajusta la imagen a 1024x1024 píxeles si es necesario.

La máscara creada define la zona inferior de la imagen para permitir la edición solo de esa área.

El resultado se descarga desde la URL proporcionada por la API y se guarda localmente.

# openai_dalle
