import streamlit as st
import socket
import threading

def  check_hostname():
    hostname = socket.gethostname()
    st.write("Current computer name")
    st.info(hostname)
    st.write("IP address")
    st.info(socket.gethostbyname(hostname))

check_hostname()

#st.warning(f"Connected: {client_address}")

def handle_client(client_socket, client_address):
    
    while True:
        data = client_socket.recv(1024).decode()
        if not  data:
            break
        #st.info(f"Received from {client_address}: {data}")
    client_socket.close()
    #st.warning(f"Disconnected: {client_address}")

host = '127.0.0.1'
port = 8004

st.info(f'Server listening on {host} : {port}')
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(5)
st.info(f'Server listening on {host} : {port}')

def start_server():

    while True:
        client_socket,  client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args = (client_socket, client_address))
        client_thread.start()

start_server()