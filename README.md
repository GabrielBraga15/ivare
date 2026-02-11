# Pet Vaccine API

API REST desenvolvida para controle de responsáveis, pets, vacinas e registros de vacinação.
O projeto foi construído utilizando Django REST Framework, autenticação JWT e banco MySQL, podendo ser executado localmente ou totalmente via Docker.

---

## Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)
* MySQL
* Docker + Docker Compose

---

## Estrutura do projeto

A aplicação está organizada em apps Django independentes:

* **users** → responsáveis pelos pets
* **pets** → cadastro dos pets
* **vaccines** → cadastro das vacinas
* **vaccinations** → registro das vacinações

Essa estrutura facilita manutenção, testes e escalabilidade.

---

## Instalação do projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/GabrielBraga15/ivare/
cd ivare
```

---

## Configuração das variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

Rode esse comando para gerar a DJANGO_SECRET_KEY:
docker compose exec web python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

```env
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=1
DB_NAME=pet_vaccine_api
DB_USER=petuser
DB_PASSWORD=petpass
DB_HOST=db
DB_PORT=3306
```

---

## Executando totalmente com Docker

### 1. Subir os containers

```bash
docker compose up -d --build
```

Isso irá iniciar:

* Container **web** (Django)
* Container **db** (MySQL)

---

### 2. Criar banco e usuário (primeira execução)

Entrar no MySQL:

```bash
docker compose exec db mysql -u root -p
```

Senha:

```
root
```

Executar:

```sql
create database pet_vaccine_api character set utf8mb4 collate utf8mb4_unicode_ci;
create user 'petuser'@'%' identified by 'petpass';
grant all privileges on pet_vaccine_api.* to 'petuser'@'%';
flush privileges;
```

---

### 3. Rodar migrations

Digite exit para sair do MySql

```bash
docker compose exec web python manage.py migrate
```

---

### 4. Criar usuário administrador

```bash
docker compose exec web python manage.py createsuperuser
```

---

### 5. Acessar o sistema

* Admin: http://127.0.0.1:8000/admin/
* API: http://127.0.0.1:8000/api/

---

## Autenticação JWT

Gerar token:

POST `/api/token/`

```json
{
  "username": "usuario criado no superuser",
  "password": "senha criado no superuser"
}
```

Usar nas requisições:

```
Authorization: Bearer ACCESS_TOKEN
```

---

## Endpoints principais

* `/api/responsibles/`
* `/api/pets/`
* `/api/vaccines/`
* `/api/vaccinations/`

Todos os endpoints exigem autenticação JWT.

---

## Executando localmente sem Docker (opcional)

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## Observações

* Projeto estruturado em apps Django independentes seguindo boas práticas
* Autenticação JWT aplicada em toda a API
* Configuração baseada em variáveis de ambiente
* Preparado para execução local ou via Docker
