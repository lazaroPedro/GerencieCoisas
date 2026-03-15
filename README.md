
# GerencieCoisas - Sistema de Gerenciamento Web

Este repositório contém o Trabalho Final da disciplina de Programação para Web I do curso de Análise e Desenvolvimento de Sistemas (4º Período).

O projeto consiste em uma aplicação web completa desenvolvida com Django, utilizando Function-Based Views (FBV), sistema de autenticação e interface responsiva com Bootstrap.

## 🎯 Objetivo

O objetivo deste projeto é demonstrar a aplicação prática de conceitos fundamentais do desenvolvimento web com Python e Django, incluindo:

* Implementação de operações CRUD (Create, Read, Update, Delete) completas.
* Controle de acesso, autenticação (Login/Logout) e permissões de usuários.
* Uso estrito de Function-Based Views (FBVs) conforme requisito técnico.
* Front-end responsivo utilizando framework Bootstrap.

## 🚀 Funcionalidades

O sistema possui controle de acesso (login necessário) e conta com 5 módulos principais de CRUD, onde é possível listar, cadastrar, editar, excluir e visualizar detalhes dos registros:

1. Gestão de Autenticação (Login, Logout e Permissões)
2. Produtos (CRUD Completo)
3. Categorias (CRUD Completo)
4. Fornecedores (CRUD Completo)
5. Movimentações (CRUD Completo)
6. Usuários (CRUD Completo)

## 🛠️ Tecnologias Utilizadas

* Python (Linguagem Base)
* Django (Framework Web)
* SQLite (Banco de Dados)
* Bootstrap 5 (Estilização e Responsividade)
* HTML5 / CSS3

## 📺 Apresentação do Projeto

Confira o vídeo demonstrativo com o funcionamento do sistema, fluxo de telas e operações CRUD:

[CLIQUE AQUI PARA ASSISTIR AO VÍDEO NO YOUTUBE](https://youtu.be/q7bJAl0KEVk)

---

## 💻 Instruções para Execução Local

Siga os passos abaixo para rodar o projeto em sua máquina:

### 1. Clone o repositório
```bash
git clone [https://github.com/lazaroPedro/GerencieCoisas.git](https://github.com/lazaroPedro/GerencieCoisas.git)
cd GerencieCoisas
````

### 2\. Crie e ative um ambiente virtual (Virtualenv)

**No Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**No Linux/Mac:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3\. Instale as dependências

```bash
pip install django
```
### 4\. Aplique as migrações do banco de dados

```bash
python manage.py migrate
```

### 5\. Crie um superusuário (Para acessar o sistema/admin)

```bash
python manage.py createsuperuser
```

### 6\. Execute o servidor

```bash
python manage.py runserver
```

O projeto estará acessível em: `http://127.0.0.1:8000/`

-----

## 👥 Integrantes do Grupo

  * **Caio Alves Nascimento**
  * **Lazaro Pedro Martins Santos**

-----

**Professor:** Carlos Anderson  
**Disciplina:** Programação para Web I


## 🔌 Endpoints de API adicionados para Web II

Além das telas HTML do projeto original, agora o sistema pode expor endpoints REST com Django REST Framework.

Exemplos:

- `GET /api/categorias/`
- `POST /api/categorias/`
- `GET /api/categorias/1/`
- `GET /api/fornecedores/`
- `GET /api/produtos/`

As listagens da API usam paginação por página e aceitam parâmetros como:

- `?page=2`
- `?page_size=10`

Para usar a API navegável do DRF com login de sessão:

- `GET /api-auth/login/`
