import socket
import threading
 
PORT = 8080
SERVER = socket.gethostbyname('127.0.0.1')
 
ADDRESS = (SERVER, PORT)
 

FORMAT = "utf-8"
 
clients, names = [], []
 
server = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

server.bind(ADDRESS)
 

 
def startChat():
 
    print("O servidor está funcionando no endereço " + SERVER)
 
    server.listen()
 
    while True:
 
        conn, addr = server.accept()
        conn.send("NAME".encode(FORMAT))
 
        name = conn.recv(1024).decode(FORMAT)
 
        names.append(name)
        clients.append(conn)
 
        print(f"O usuário é :{name}")
 
        broadcastMessage(f"{name} entrou no chat!".encode(FORMAT))
 
        conn.send('Conexão bem sucedida!'.encode(FORMAT))
 

        thread = threading.Thread(target=handle,
                                  args=(conn, addr))
        thread.start()
 
        print(f"active connections {threading.active_count()-1}")
 
 
def handle(conn, addr):
 
    print(f"new connection {addr}")
    connected = True
 
    while connected:

        message = conn.recv(1024)
 

        broadcastMessage(message)
 
    conn.close()
 
 
 
def broadcastMessage(message):
    for client in clients:
        client.send(message)
 

startChat()
