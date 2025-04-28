# API Principal

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Index Page"

@app.route('/register', methods=['POST'])
def register():
    data = request.json

    descricao = data.get('descricao')
    valor = daga.get('valor')
    local = data.get('local')
    metodo_pagamentoo = data.get('metodo_pagamento')

##

    # Inserçao do gasto no banco de dados

    #Ex:
    #cursor.execute("INSERT INTO gastos (descricao, valor, local, metodo_pagamento) VALUES (%s, %s, %s, %s)",
    #                (descricao, valor, local, metodo_pagamento))
    
##

return jsonify({"status": "sucesso", "mensagem": "Gasto registrado com sucesso 😉."}), 201

