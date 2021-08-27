# echo_02_threads.py

import socket
import threading


def run_server(host='127.0.0.1', port=55555):
    sock = socket.socket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen()
    while True:
        client_sock, addr = sock.accept()
        print('Connection from', addr)
        thread = threading.Thread(target=handle_client, args=[client_sock])
        thread.start()


def handle_client(sock):
    while True:
        recieved_data = sock.recv(4096)
        if not recieved_data:
            break
        sock.sendall(recieved_data)

    print('Client disconnected:', sock.getpeername())
    sock.close()


if __name__ == '__main__':
    run_server()