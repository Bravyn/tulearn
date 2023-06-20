import socket
import streamlit as st
import random
st.title("Client X")
def send_message():

    host = '127.0.0.1'
    port = 8005

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((host, port))
    except Exception as e:
        st.warning(f"Sorry, {str(e).split(']')[1].lower()}.")

    
    message = st.text_input("Type message")
    st.caption("Type exit to quit")
    
    if st.button("Send"):
            
        try:
            client_socket.sendall(message.encode())
        except Exception as e:
            st.warning(f"Sorry, {str(e).split(']')[1].lower()}.")
    
        
        client_socket.close()
        #st.warning("Client socket closed")

send_message()

