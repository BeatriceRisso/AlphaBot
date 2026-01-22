from flask import Flask, render_template, request, redirect, url_for
from flask_login import (
    LoginManager, UserMixin,
    login_user, login_required,
    logout_user, current_user
)
from AlphaBot import AlphaBot


app = Flask(__name__)
app.secret_key = "Snoopy"   # chiave segreta per le sessioni (è come una password)

snoopy = AlphaBot() # inizializza il robot

snoopy.stop() # per far stare fermo il robot dopo il collegamento

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"                 


class User(UserMixin):
    def __init__(self, id):
        self.id = id


# dizionario in cui mettiamo gli utenti che ci possono essere (è più sicuro con un database)
USERS = {
    "admin": {"password": "alphabot"}
}


# carica l'utente controllando che sia presente del dizionario di prima
@login_manager.user_loader
def load_user(user_id):
    if user_id in USERS:
        return User(user_id)
    return None


# -------------------- LOGIN --------------------
@app.route("/", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        #qua ci vanno le query se e quando ci sarà il database

        if username in USERS and USERS[username]["password"] == password:
            login_user(User(username))
            return redirect(url_for("control"))

        return "Credenziali non valide"

    return render_template("login.html")


# -------------------- LOGOUT --------------------
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


# -------------------- PAGINA DI CONTROLLO --------------------
@app.route("/control")
@login_required
def control():
    return render_template("control.html")


# -------------------- MOVIMENTO ROBOT --------------------
@app.route("/move/<cmd>")
@login_required
def move(cmd):
    cmd = cmd.lower()

    if cmd == "w":
        snoopy.forward()
    elif cmd == "s":
        snoopy.backward()
    elif cmd == "a":
        snoopy.left()
    elif cmd == "d":
        snoopy.right()
    elif cmd == "x":
        snoopy.stop()
    else:
        return "Comando sconosciuto"


# -------------------- AVVIO SERVER --------------------
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")
