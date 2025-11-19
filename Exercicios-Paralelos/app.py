from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Bem vindo a minha primeira API SOLO"

@app.route("/usuarios")
def listar_usuarios():
    usuarios = [
        {"id": 1, "nome": "Galak"},
        {"id": 2, "nome": "Lira"}
    ]
    return jsonify(usuarios) 

@app.route("/mensagem", methods=["GET"])
def mensagem():
    return jsonify({"mensagem": "API respondendo com GET"})

if __name__ == "__main__":
    app.run(debug=True)