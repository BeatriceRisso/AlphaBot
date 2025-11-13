import socket  # Importa la libreria per la comunicazione via rete

# Indirizzo IP e porta del server (il Raspberry Pi con l’AlphaBot)
SERVER_ADDRESS = ('192.168.1.128', 5001)  
BUFFER = 4096  # Dimensione massima dei dati ricevuti

# Crea un socket IPv4 (AF_INET) e TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connessione al server
print(f"Connessione al server {SERVER_ADDRESS}...")
s.connect(SERVER_ADDRESS)
print("Connesso! Puoi ora inviare comandi al robot.\n")

# Ciclo principale per inviare comandi al server
while True:
    # Legge un comando dall'utente
    message = input("Scrivi un comando (avanti, indietro, sinistra, destra, stop, esci): ")

    # Se l’utente scrive “esci”, chiude la connessione
    if message.lower() == "esci":
        print("Disconnessione dal server...")
        break

    # Invia il messaggio al server
    s.send(message.encode())

    # Riceve la risposta dal server e la mostra
    data = s.recv(BUFFER)
    print("Risposta del server:", data.decode())

# Chiude il socket
s.close()
print("Connessione chiusa.")
