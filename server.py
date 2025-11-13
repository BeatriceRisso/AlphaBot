import socket
from AlphaBot import AlphaBot

# Impostazioni del server
ADDRESS = ('0.0.0.0', 5001)
BUFFER = 4096

# Inizializza il robot
snoopy = AlphaBot()

# Crea socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(ADDRESS)
s.listen(1)

print("In attesa di connessione...")
connection, address = s.accept()
print(f"Connesso con {address}")

# Ciclo principale per ricevere comandi
while True:
    data = connection.recv(BUFFER)
    if not data:
        print("Connessione chiusa dal client.")
        break

    comando = data.decode().strip().lower()
    print(f"Ricevuto comando: {comando}")
    destra, sinistra = snoopy.sensori()

    #controllo sensori 
    if destra != 0 & sinistra != 0:
        # Controllo tasti WASD
        if comando == "w":
            snoopy.forward()
        elif comando == "s":
            snoopy.backward()
        elif comando == "a":
            snoopy.left()
        elif comando == "d":
            snoopy.right()
        elif comando == "x":
            snoopy.stop()
        else:
            print("Comando sconosciuto")

    else:
        snoopy.stop()


    # Risposta al client
    connection.send("Comando eseguito".encode())

# Chiude tutto quando la connessione termina
snoopy.stop()
connection.close()
s.close()
print("Connessione chiusa e robot fermato.")
