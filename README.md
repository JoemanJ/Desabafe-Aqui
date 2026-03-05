> Note: this readme has a section in english down below

# Desabafe Aqui!
## O que é esse repositório?
Este é um projeto que eu criei para usar como estudo e portfolio de desenvolvimento web. A ideia foi criar um aplicativo web simples porém completo, com operações CRUD, comunicação com banco de dados, uma interface estilizada, sistema de autenticação e seguindo boas práticas de desenvolvimento web.

## O que é o projeto?
O "Desabafe Aqui" é uma paródia de rede social onde usuários podem se registrar para desabafar sobre histórias inconvenientes do dia-a-dia anonimamente em textos curtos, ou comentar nos desabafos dos outros. 

O conceito é uma piada com o fato de pessoas de forma geral acharem divertido reclamar de coisas coletivamente, e o nome é um trocadilho com o site "Reclame Aqui".

## Que funcionalidades tem?
Abaixo escrevi uma lista cheia de termos comuns e buzzwords que programadores amam elogiar ou mencionar o tempo todo, e que eu apliquei nesse projeto.

Alguns conceitos foram melhor aplicados que outros por conta da minha experiência e trejeitos de programação, mas me esforcei para seguir todos com paciência e bom senso. 

Até então o projeto incorpora:
- Framework backend (Django)
- Framework frontend (Angular)
- Comunicação com base de dados (SQlite)
- Autenticação de usuário (JWT)
- Operações CRUD
- API REST
- Modelo MVC
- Controle de acesso
- Sanitização de entrada de usuário
- Arquitetura desacoplada
- Apresentação SPA (Single Page Application)
- Boas práticas de desenvolvimento
    - Modularização extensa
    - Estruturas de pastas padronizadas
    - Test Driven Development (TDD)
    - etc.

## O que está implementado até agora? E quais os planos para o futuro?
Meu plano é ir adicionando novas funcionalidades ou melhorando funcionalidades já existentes à medida que eu for aprendendo, de forma gradual. Isso significa que a frequência de commits pode variar entre algumas horas e vários anos, a depender do meu tempo livre e paciência para estudar coisas novas nele.

Funcionalidades implementadas até então (completude da lista depende da minha memória):
- Backend funcional
    - Modelos de perfil de usuário, post e comentário
    - Autenticação por JWT
    - Rotas de api com controle de acesso e serialização em JSON para operações CRUD de cada modelo
    - Rotas para documentação de API ('/api/docs/')
    - Testes unitários para cada modelo e endpoint da API
- Frontend funcional (Ressalto que não me dou muito bem com frontend)
    - Modelo Single Page Application (SPA)
    - Cores e fontes padronizadas, compartilhadas por todo o site
    - Componentes reativos (layouts diferentes para usuários logados)
    - Controle de acesso por redirecionamento
    - Página funcional de login e cadastro, com tratamento de erros
    - Possibiliade de criar posts com atualização automática do feed
- Algumas entidades de exemplo em um banco SQLite


Funcionalidades planejadas:
- Página de perfil de usuário
- Possibilidade de edição e exclusão de posts pelo frontend
- Possibilidade de dar "likes" em posts e comentários
- Possibilidade de comentar em psots e outros comentários
- Feed com scrolling infinito, mas renderizando apenas os posts visíveis
- Possibilidade de posts com imagem
- Funcionalidades de administrador 
- Tags para posts

## Como rodar localmente?
Pré-requisitos:

- Django 6.0+
- Node.js (recomenda-se v20 ou superior)
- Angular CLI (npm install -g @angular/cli)

1. Configuração do Backend (Django)

O backend gerencia a autenticação JWT, perfis de usuário e a persistência dos posts.

Navegue até a pasta do backend:
```Bash
cd backend
```

Crie e ative um ambiente virtual:
```Bash
python3 -m venv venv
# No Linux/macOS:
source venv/bin/activate
# No Windows:
.\venv\Scripts\activate
```
Instale as dependências:
```Bash
pip install -r ./requirements.txt
```
Entre na pasta do projeto:
```Bash
cd desabafeAqui
```
Execute as migrações do banco de dados: 
```Bash
python3 manage.py migrate
```
> OBS: Já existe um arquivo de banco de dados com algumas entidades de exemplo no repositório, mas é bom executar as migrações caso eu tenha esquecido de atualizar esse banco de exemplo

Inicie o servidor de desenvolvimento:
```Bash
python3 manage.py runserver
```
O servidor estará disponível em: http://127.0.0.1:8000/\
A interface de admin do Django pode ser acessada em http://127.0.0.1:8000/admin. O login e a senha de admin do banco de dados de exemplos são ambos "admin".\
Documentação da API pode ser vista em http://127.0.0.1:8000/docs/swagger ou http://127.0.0.1:8000/docs/redoc.

2. Configuração do Frontend (Angular)

O frontend consome a API e fornece a interface web.

Navegue até a pasta do frontend:
```Bash
cd frontend/desabafeAqui
```
Instale as dependências do Node:
```Bash
npm install
```
Inicie o servidor do Angular:
```Bash
ng serve
```
Acesse a aplicação:
Abra o seu navegador em http://localhost:4200/

## Quais as tecnologias usadas?
O backend é feito usando [Django](https://www.djangoproject.com/) e a [Django Rest Framework](https://www.django-rest-framework.org/), e o frontend é feito usando [Angular](https://angular.dev/). A aplicação é desacoplada, ou seja, frontend e backend rodam em servidores distintos. A autenticação é feita usando SimpleJWT.

Versões:
- Django: 6.0.2
- Angular: 21.1.4
- Django REST Framework: 3.16.1
- DRF SimpleJWT: 5.5.1

## Sobre uso de ferramentas de IA
Nenhuma única linha de código neste repositório foi gerada por inteligência artificial. Cada linha de código porcamente formatada e cada erro bobo são inteiramente meus.

Usei ferramentas de IA generativa (em especial Google Gemini) ao longo de todo o projeto apenas para guiar meus estudos, mostrar exemplos de código de ferarmentas novas para mim (praticamente todas elas) e tirar dúvidas sobre boas práticas.

IA generativa também foi usada para escrever a sessão "como rodar localmente" desse readme e para fazer a tradução da sessão do readme para inglês (por pura preguiça da minha parte mesmo), mas cada linha de texto ou código gerada foi revisada e/ou corrigida por mim manualmente.

# (English section starts here)
# Desabafe Aqui! (Vent Here!)
## What is this repository?

This is a project I created for study purposes and as a web development portfolio. The goal was to build a simple yet complete web application featuring CRUD operations, database communication, a styled interface, and an authentication system—all while following web development best practices.

## What is the project?

"Desabafe Aqui" is a social media parody where users can register to anonymously vent about inconvenient daily life stories through short texts, or comment on others' rants.

The concept is a joke on the fact that people generally find it fun to complain about things collectively. The name itself is a pun on the famous Brazilian website "Reclame Aqui" (Complain Here).

## What features does it have?

Below is a list full of common terms and buzzwords that programmers love to praise or mention all the time, which I have applied in this project.

Some concepts were better implemented than others due to my experience and programming habits, but I tried to follow all of them with patience and common sense.

So far, the project incorporates:

- Backend Framework (Django)
- Frontend Framework (Angular)
- Database communication (SQLite)
- User Authentication (JWT)
- CRUD Operations
- REST API
- MVC Pattern
- Access Control
- User Input Sanitization
- Decoupled Architecture
- SPA (Single Page Application) Presentation
- Development Best Practices
    - Extensive modularization
    - Standardized folder structures
    - Test Driven Development (TDD)
    - etc.

## What is implemented so far? And what are the plans for the future?

My plan is to gradually add new features or improve existing ones as I learn. This means commit frequency may vary between a few hours and several years, depending on my free time and patience to study new things.

Features implemented so far (completeness depends on my memory):

- Functional Backend
    - Models for User Profile, Post, and Comment.
    - JWT Authentication.
    - API routes with access control and JSON serialization for CRUD operations on each model.
    - API documentation routes ('/api/docs/').
    - Unit tests for each model and API endpoint.
- Functional Frontend (I wanna point out that frontend isn't my cup of tea)
    -  Single Page Application (SPA) model.
    -  Standardized colors and fonts shared across the site.
    -  Reactive components (different layouts for logged-in users).
    -  Access control via redirection.
    -  Functional Login and Sign-up pages with error handling.
    -  Ability to create posts with automatic feed updates.
- Example entities provided in a SQLite database.

Planned features:

- User profile pages.
- Ability to edit and delete posts via the frontend.
- Ability to "like" posts and comments.
- Ability to comment on posts and other comments.
- Feed with infinite scrolling (rendering only visible posts).
- Support for posts with images.
- Admin functionalities.
- Post tags.

## How to run locally?

Prerequisites:

- Django 6.0+
- Node.js (v20 or higher recommended)
- Angular CLI (npm install -g @angular/cli)

1. Backend Setup (Django)

The backend handles JWT authentication, user profiles, and post persistence.

Navigate to the backend folder:
```Bash
cd backend
```

Create and activate a virtual environment:
```Bash
python3 -m venv venv
# On Linux/macOS:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

Install dependencies:
```Bash
pip install -r ./requirements.txt
```

Enter the project folder:
```Bash
cd desabafeAqui
```

Run database migrations:
```Bash
python3 manage.py migrate
```
>NOTE: A database file with example entities is already in the repository, but it is good practice to run migrations in case I forgot to update this example DB.

Start the development server:
```Bash
python3 manage.py runserver
```

The server will be available at: http://127.0.0.1:8000/\
The Django admin interface can be accessed at http://127.0.0.1:8000/admin. Both the login and password for the example database are "admin".\
API documentation can be viewed at http://127.0.0.1:8000/docs/swagger or http://127.0.0.1:8000/docs/redoc.

2. Frontend Setup (Angular)

The frontend consumes the API and provides the web interface.

Navigate to the frontend folder:
```Bash
cd frontend/desabafeAqui
```

Install Node dependencies:
```Bash
npm install
```
Start the Angular server:
```Bash
ng serve
```

Access the application:
Open your browser at http://localhost:4200/

## What technologies are used?

The backend is built using Django and the Django Rest Framework, and the frontend is built using Angular. The application is decoupled, meaning frontend and backend run on distinct servers. Authentication is handled via SimpleJWT.

Versions:

- Django: 6.0.2
- Angular: 21.1.4
- Django REST Framework: 3.16.1
- DRF SimpleJWT: 5.5.1

## On the use of AI tools

Not a single line of code in this repository was generated by artificial intelligence. Every poorly formatted line and every silly mistake is entirely my own.

I used generative AI tools (specifically Google Gemini) throughout the project solely to guide my studies, provide code examples for tools new to me (nearly all of them), and answer questions about best practices.

Generative AI was also used to write the "how to run locally" section of this readme and to translate this readme into English (this exact section) (purely out of laziness on my part), but every line of text or code generated was manually reviewed and/or corrected by me.