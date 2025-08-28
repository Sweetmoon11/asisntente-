from streamlit_mic_recorder import speech_to_text
from langchain_openai import ChatOpenAI
import streamlit as st 

openai_Api_key = "clave api"
#Se agregara el modelo gpt-4o para el llm 
llm = ChatOpenAI(model="gpt-4o", openai_api_key=openai_Api_key)

st.title("Asistente todo en uno")

st.write("aplicacion de chat habilitada por voz")

text = speech_to_text(language="es", use_container_width =True, just_once=False, key="STT")

if text:
    st.write("Tu:", text)
    response = llm.invoke(text)
    st.write("Respuesta del modelo:", response.content)