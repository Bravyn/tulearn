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

def handle_client(client_socket, client_address):
    st.title("Client X")
    st.warning(f"Connected: {client_address}")
    
    while True:
        data = client_socket.recv(1024).decode()
        if not  data:
            break
        st.caption(f"Received from {client_address}: {data}")
    client_socket.close()
    st.warning(f"Disconnected: {client_address}")

def start_server():
    host = '127.0.0.1'
    port = 8080

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    st.info(f'Server listening on {host} : {port}')

    while True:
        client_socket = client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args = (client_socket, client_address))
        client_thread.start()

start_server()