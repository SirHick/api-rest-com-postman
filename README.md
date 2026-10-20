# api-rest-com-postman

# API de Gerenciamento de Livros

Uma API REST simples desenvolvida em Python utilizando o micro-framework Flask. O projeto demonstra operações básicas de CRUD (Consultar, Criar, Editar e Excluir) gerenciando um catálogo de livros armazenado diretamente na memória.

## 📋 Pré-requisitos

-   Python 3.x
    
-   Flask
    

Para instalar o Flask, execute o comando:

Bash

```
pip install flask
```

## 🚀 Como Executar

1.  Salve o arquivo principal contendo o código (ex: `app.py`).
    
2.  Abra o terminal e navegue até a pasta onde o arquivo foi salvo.
    
3.  Inicie o servidor com o comando:
    
    Bash
    
    ```
    python app.py
    ```
    
4.  O servidor local estará rodando no endereço: `http://localhost:5000`
    

## 🔗 Endpoints da API

Para testar a API, recomenda-se o uso de ferramentas como **Postman** ou **Insomnia**. A API consome e retorna dados no formato JSON.

### 1\. Consultar todos os livros

-   **Rota:** `/livros`
    
-   **Método:** `GET`
    
-   **Retorno:** Lista completa com todos os livros cadastrados.
    

### 2\. Consultar livro por ID

-   **Rota:** `/livros/<id>`
    
-   **Método:** `GET`
    
-   **Retorno:** Dados do livro correspondente ou uma mensagem de "Livro não encontrado!".
    

### 3\. Criar um novo livro

-   **Rota:** `/novo_livro`
    
-   **Método:** `POST`
    
-   **Corpo da Requisição (JSON):**
    
    JSON
    
    ```
    {
      "id": 14,
      "titulo": "O Nome da Rosa",
      "autor": "Umberto Eco"
    }
    ```
    

### 4\. Editar um livro existente

-   **Rota:** `/livros/<id>`
    
-   **Método:** `PUT`
    
-   **Corpo da Requisição (JSON):**
    
    JSON
    
    ```
    {
      "titulo": "Título Alterado",
      "autor": "Autor Alterado"
    }
    ```
    

### 5\. Remover um livro

-   **Rota:** `/remover_livro/<id>`
    
-   **Método:** `DELETE`
    
-   **Retorno:** Lista de livros atualizada após a exclusão ou mensagem de erro caso o ID não seja encontrado.