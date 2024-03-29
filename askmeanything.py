import streamlit as st
import wikipedia
import pyttsx3

engine = pyttsx3.init()
st.title('Ask me anything library')
topic = st.text_input('Ask  :')
if(st.button('Generate')):
    text = wikipedia.summary(topic,sentences=1)
    st.write(text)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(text)
    engine.runAndWait()


