import socket                  # Importa la libreria per la comunicazione via rete
from AlphaBot import AlphaBot  # Importa la classe per controllare il robot AlphaBot

# Impostazioni di rete
ADDRESS = ('0.0.0.0', 5001)    # '0.0.0.0' significa "accetta connessioni da qualsiasi indirizzo IP" sulla porta 5001
BUFFER = 4096                  # Dimensione massima dei dati ricevuti in un singolo pacchetto

# Crea l'oggetto per controllare il robot
snoopy = AlphaBot()

# Creazione del socket TCP (Stream = TCP)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Collega il socket all’indirizzo e alla porta specificata
s.bind(ADDRESS)

# Mette il server in ascolto (accetta 1 connessione alla volta)
s.listen(1)
print("In attesa di connessione...")

# Accetta una connessione in arrivo da un client (es. PuTTY o un altro script)
connection, address = s.accept()
print(f"Connesso con {address}")

# Ciclo principale che riceve e gestisce i comandi
while True:
    # Riceve i dati inviati dal client
    data = connection.recv(BUFFER)
    
    # Se non arriva nessun dato, la connessione è chiusa → esco dal ciclo
    if not data:
        print("Connessione chiusa dal client.")
        break

    # Converte i byte ricevuti in stringa, rimuove spazi e mette in minuscolo
    comando = data.decode().strip().lower()
    print(f"Ricevuto comando: {comando}")

    # Controlla il comando e muove il robot di conseguenza
    if comando == "avanti":
        snoopy.forward()
    elif comando == "indietro":
        snoopy.backward()
    elif comando == "sinistra":
        snoopy.left()
    elif comando == "destra":
        snoopy.right()
    elif comando == "stop":
        snoopy.stop()
    else:
        print("Comando sconosciuto")

    # Invia una conferma al client
    connection.send("Comando eseguito".encode())

# Quando il client chiude la connessione, ferma il robot e chiudi tutto
snoopy.stop()
connection.close()
s.close()
print("Connessione chiusa e robot fermato.")
