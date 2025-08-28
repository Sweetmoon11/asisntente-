🎤 Asistente de Voz con IA

Una aplicación web interactiva que permite interactuar con GPT-4o mediante comandos de voz. Desarrollada con Streamlit y LangChain.

✨ Características
🎤 Reconocimiento de voz: Graba y transcribe audio en tiempo real

🤖 IA conversacional: Integración con GPT-4o de OpenAI

🌍 Soporte multilenguaje: Compatible con español y otros idiomas

🎨 Interfaz intuitiva: Diseño limpio y fácil de usar

⚡ Tiempo real: Respuestas inmediatas del modelo de IA

📦 Requisitos Previos
Python 3.8 o superior

pip (gestor de paquetes de Python)

API key de OpenAI

🚀 Instalación
Método 1: Clonación del repositorio

# Clonar el repositorio
git clone https://github.com/tuusuario/asistente-voz-ia.git
cd asistente-voz-ia

# Crear entorno virtual (recomendado)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

Método 2: Instalación rápida
# Instalar dependencias directamente
pip install streamlit streamlit-mic-recorder langchain-openai openai

⚙️ Configuración
1. Configurar API Key de OpenAI
Crea un archivo .streamlit/secrets.toml en la raíz del proyecto:

# .streamlit/secrets.toml
OPENAI_API_KEY = "tu_api_key_aqui"

2. Obtener una API Key
Visita OpenAI Platform

Inicia sesión o crea una cuenta

Ve a "API Keys" → "Create new secret key"

Copia la key y guárdala de forma segura

🎯 Uso
Ejecutar la aplicación

**streamlit run main.py**

Tecnologías Utilizadas
Streamlit: Framework para aplicaciones web en Python

Streamlit Mic Recorder: Componente de grabación de audio

LangChain: Framework para aplicaciones con LLMs

OpenAI GPT-4o: Modelo de lenguaje avanzado

Python: Lenguaje de programación principal

🛠️ Personalización
Cambiar el modelo de OpenAI

Edita en Main.py

llm = ChatOpenAI(model="gpt-4-turbo", openai_api_key=openai_Api_key)

Modificar el idioma
Cambia el parámetro language en speech_to_text:
text = speech_to_text(language="en", ...)  # Para inglés

📦 Estructura del Proyecto

asistente-voz-ia/
├── 📜 main.py                    # Aplicación principal
├── 📜 requirements.txt           # Dependencias de Python
├── 📜 INSTALAR.bat               # Instalador automático
├── 📜 LANZAR.bat                 # Lanzador de la aplicación
└── 📜 README.md                  # Este archivo
