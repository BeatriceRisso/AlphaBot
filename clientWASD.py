import socket
import keyboard  # libreria per leggere i tasti in tempo reale (installala con: pip install keyboard)
#RIFARE CON PYNPUT
# IP del Raspberry Pi e porta
SERVER_ADDRESS = ('192.168.1.128', 5001)
BUFFER = 4096

# Connessione al server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f"Connessione al server {SERVER_ADDRESS}...")
s.connect(SERVER_ADDRESS)
print("Connesso! Usa i tasti WASD per muovere il robot, X per fermarlo, Q per uscire.\n")

# Ciclo per leggere i tasti
while True:
    if keyboard.is_pressed("w"):
        s.send("w".encode())
    elif keyboard.is_pressed("s"):
        s.send("s".encode())
    elif keyboard.is_pressed("a"):
        s.send("a".encode())
    elif keyboard.is_pressed("d"):
        s.send("d".encode())
    elif keyboard.is_pressed("x"):
        s.send("x".encode())
    elif keyboard.is_pressed("q"):  # per uscire
        print("Chiusura connessione...")
        break

    # Riceve eventuale risposta dal server (non obbligatoria)
    s.setblocking(False)
    try:
        data = s.recv(BUFFER)
        if data:
            print("Server:", data.decode())
    except:
        pass
    s.setblocking(True)

# Chiude il socket
s.close()
print("Connessione chiusa.")
