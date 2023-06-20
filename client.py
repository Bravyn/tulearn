import socket
import streamlit as st
import random

def send_message():
    host = '127.0.0.1'
    port = 8080

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    
    message = st.text_input("Type message")
    st.caption("Type exit to quit")

    while True:
        client_socket.sendall(message.encode())
        if message.lower() == "exit":
           break
    client_socket.close()
    st.warning("Client socket closed")

send_message()

