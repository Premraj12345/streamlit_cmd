import streamlit as st
import os

st.header('CMD')

cmd_input = st.text_input('Enter a command')
button_click = st.button('RUN')

if button_click == True:
    with st.container():
        text = os.popen(cmd_input).read()
        st.markdown(text)
