Instalação
1. Clonar o projeto
git clone [<repo>](https://github.com/GabrielBraga15/ivare.git)
cd pet_vaccine_api

2. Criar ambiente virtual
python -m venv .venv
source .venv/bin/activate
# Windows
.venv\Scripts\activate

3. Instalar dependências
pip install -r requirements.txt

Banco de dados (MySQL)
create database pet_vaccine_api character set utf8mb4 collate utf8mb4_unicode_ci;
create user 'petuser'@'%' identified by 'petpass';
grant all privileges on pet_vaccine_api.* to 'petuser'@'%';
flush privileges;

Executando o projeto

Aplicar migrations:

python manage.py migrate


Criar usuário administrador:

python manage.py createsuperuser


Executar servidor:

python manage.py runserver


Acessos:

Admin: http://127.0.0.1:8000/admin/

API: http://127.0.0.1:8000/api/

Autenticação JWT

Gerar token:

POST /api/token/

{
  "username": "123456",
  "password": "123456"
}


Usar nas requisições:

Authorization: Bearer ACCESS_TOKEN

Endpoints principais
Endpoint	Descrição
/api/responsibles/	CRUD de responsáveis
/api/pets/	CRUD de pets
/api/vaccines/	CRUD de vacinas
/api/vaccinations/	Registro de vacinação
Execução com Docker
docker compose up -d


Depois:

python manage.py migrate
python manage.py runserver
