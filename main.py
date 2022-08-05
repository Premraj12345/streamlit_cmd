import streamlit as st
import os
from download import download
from zipfile import ZipFile

st.header('CMD')
button_click2 = st.button('Download the zip File') 

cmd_input = st.text_input('Enter a command')
button_click = st.button('RUN')


if button_click == True:
    with st.container():
        text = os.popen(cmd_input).read()
        st.markdown(text)
if button_click2 == True:
    with st.container():
        status = download('https://github.com/dreamnettech/dreampower-checkpoints/releases/download/0.0.1/v0.0.1.zip','model.zip')
        st.markdown(status)
        button_click3 = st.button(f'Extract the {status} File')
        if button_click3 == True:
            with ZipFile('model.zip','r') as zipObj:
                zipObj.extractall()
