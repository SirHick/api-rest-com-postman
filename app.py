#desenvolver um back end com api -
#postman - teste http -> verificar respostas da API
# 1. Objetivo 
# 2. URL base
# 3. Endpoints
# 4. Recursos disponibilizados

# Vamos criar uma api:

"""
1. Consultar
2. Criar
3. Editar
4. Excluir
CRUD
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
    "id" : 1,
    "titulo" : "A Paixão Segundo G.H.",
    "autor" : "Clarice Lispector"
    },
    {"id": 2,
     "titulo": "Pai Rico Pai Pobre",
     "autor": "Robert Kiyosaki"
    },
    {"id": 3,
    "titulo": "O Hobbit",
    "autor": "J.R.R Tolkien"
    },{
        "id": 4,
        "titulo": "1984",
        "autor": "George Orwell"
    },
    {
        "id": 5,
        "titulo": "Dom Quixote",
        "autor": "Miguel de Cervantes"
    },
    {
        "id": 6,
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien"
    },
    {
        "id": 7,
        "titulo": "A Menina que Roubava Livros",
        "autor": "Markus Zusak"
    },
    {
        "id": 8,
        "titulo": "O Alquimista",
        "autor": "Paulo Coelho"
    },
    {
        "id": 9,
        "titulo": "Cem Anos de Solidão",
        "autor": "Gabriel García Márquez"
    },
    {
        "id": 10,
        "titulo": "Ensaio sobre a Cegueira",
        "autor": "José Saramago"
    },
    {
        "id": 11,
        "titulo": "O Principezinho",
        "autor": "Antoine de Saint-Exupéry"
    },
    {
        "id": 12,
        "titulo": "A Revolução dos Bichos",
        "autor": "George Orwell"
    },
    {
        "id": 13,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling"
    }
]

#Consultar livros - Criar uma função
def obter_livros():
    return jsonify(livros)

#Criar as rotas
#/livros
#A rota foi especificada, só será aceito o método GET
@app.route("/livros", methods = ["GET"])
def obter_livros():
    return jsonify(livros)

@app.route("/livros/<int:id>", methods = ["GET"])
def livro_por_id(id):
    for livro in livros:
        if livro.get("id") == id:
            return jsonify(livro)
    return jsonify({"Message": "Livro não encontrado!"})


#PUT

@app.route("/livros/<int:id>", methods = ["PUT"])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route("/novo_livro", methods = ["POST"])
def incluir_novo_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Deletar um livro
@app.route("/remover_livro/<int:id>", methods = ["DELETE"])
def remover_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get("id") == id:
            livros.pop(indice)
            return jsonify(livros)
    return jsonify({"Message": "Livro não encontrado ou já removido!"})
        
#Inicialização do supervisor local
app.run(
    host = "localhost",
    port = "5000",
    debug = True
)