# Pet Vaccine API

API REST desenvolvida para controle de responsáveis, pets, vacinas e registros de vacinação.
O projeto foi construído seguindo boas práticas de organização em apps Django independentes, autenticação via JWT e estrutura preparada para execução local ou via Docker.

---

## Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)
* MySQL
* Docker (opcional)

---

## Estrutura do projeto

A aplicação está organizada em módulos independentes:

* **users** — responsáveis pelos pets
* **pets** — cadastro dos pets
* **vaccines** — cadastro das vacinas
* **vaccinations** — registro das vacinações realizadas

Cada módulo possui seus próprios models, serializers, views e rotas, facilitando manutenção e escalabilidade.

---

## Instalação

### 1. Clonar o projeto

```bash
git clone <repo>
cd pet_vaccine_api
```

### 2. Criar ambiente virtual

Linux / Mac:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

---

## Configuração do ambiente

Crie um arquivo `.env` baseado no `.env.example` e configure:

```
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=1
DB_NAME=pet_vaccine_api
DB_USER=petuser
DB_PASSWORD=petpass
DB_HOST=127.0.0.1
DB_PORT=3306
```

---

## Banco de dados

Criar banco e usuário MySQL:

```sql
create database pet_vaccine_api character set utf8mb4 collate utf8mb4_unicode_ci;
create user 'petuser'@'%' identified by 'petpass';
grant all privileges on pet_vaccine_api.* to 'petuser'@'%';
flush privileges;
```

Aplicar migrations:

```bash
python manage.py migrate
```

Criar usuário administrador:

```bash
python manage.py createsuperuser
```

---

## Executando o projeto

```bash
python manage.py runserver
```

Acessos:

* Admin: http://127.0.0.1:8000/admin/
* API: http://127.0.0.1:8000/api/

---

## Autenticação JWT

Gerar token:

POST `/api/token/`

```json
{
  "username": "admin",
  "password": "123456"
}
```

Usar nas requisições protegidas:

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

## Executando com Docker (opcional)

```bash
docker compose up -d
python manage.py migrate
python manage.py runserver
```

---

## Observações

* Projeto estruturado em apps independentes seguindo boas práticas Django
* Autenticação JWT aplicada em toda a API
* Configuração de ambiente feita via variáveis `.env`
* Banco MySQL configurado para ambiente local ou containerizado
