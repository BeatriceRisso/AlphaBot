import socket
import AlphaBot

from AlphaBot import AlphaBot

ADDRESS=('0.0.0.0',5001) #0.0.0.0 è un ip speciale anche detto this host= questo pc perchè potrebbe cambiare ogni volta che mi collego alla rete, essendo che posso collegare in questo caso il mio pc personale viene comodo mettere questo ip
BUFFER= 4096

snoopy=AlphaBot()


s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) #stream perchè è tcp 

s.bind(ADDRESS) 


N=100 #numero massimo di connessioni accettate, lo decido io 
s.listen(N)


connection, address=s.accept()

data=connection.recv(BUFFER)
snoopy.forward() #appena si riceve un messaggio il robot va avanti 

while True:
    # Controllo comandi inviati da PuTTY
    if data.lower() == "avanti":
        snoopy.forward()
    elif data.lower() == "indietro":
        snoopy.backward()
    elif data.lower() == "sinistra":
        snoopy.left()
    elif data.lower() == "destra":
        snoopy.right()
    elif data.lower() == "stop":
        snoopy.stop()
    else:
        print("Comando sconosciuto")




connection.send("messaggio ricevuto".encode())#risposta quando mi arriva un messaggio, viene ,mandata al client 

snoopy.stop()
s.close()