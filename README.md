# Pet Vaccine API

API REST desenvolvida para controle de responsáveis, pets, vacinas e registros de vacinação.
O projeto foi estruturado seguindo boas práticas de organização em apps Django independentes, autenticação via JWT e execução simplificada utilizando Docker.

---

## Tecnologias utilizadas

* Python 3
* Django
* Django REST Framework
* JWT Authentication (SimpleJWT)
* MySQL
* Docker / Docker Compose

---

## Estrutura do projeto

A aplicação está organizada em módulos independentes:

* **users** — responsáveis pelos pets
* **pets** — cadastro dos pets
* **vaccines** — cadastro das vacinas
* **vaccinations** — registro das vacinações realizadas

Cada módulo possui seus próprios models, serializers, views e rotas, facilitando manutenção e escalabilidade.

---

## Clonando o projeto

```bash
git clone https://github.com/GabrielBraga15/ivare.git
cd ivare
```

---

## Configuração do ambiente

Crie o arquivo `.env` na raiz do projeto baseado no `.env.example`:

```
DJANGO_SECRET_KEY=your_secret_key
DJANGO_DEBUG=1
DB_NAME=pet_vaccine_api
DB_USER=petuser
DB_PASSWORD=petpass
DB_HOST=db
DB_PORT=3306
```

---

## Executando com Docker (recomendado)

### 1. Subir containers

```bash
docker compose up -d --build
```

Isso iniciará:

* Container MySQL
* Container da aplicação Django

---

### 2. Aplicar migrations

```bash
docker compose exec web python manage.py migrate
```

---

### 3. Criar usuário administrador

```bash
docker compose exec web python manage.py createsuperuser
```

---

### 4. Executar aplicação

Caso o container não esteja executando automaticamente:

```bash
docker compose exec web python manage.py runserver 0.0.0.0:8000
```

---

## Acessos

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

Utilizar nas requisições protegidas:

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

## Executando sem Docker (opcional)

Criar ambiente virtual:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

Aplicar migrations e executar:

```bash
python manage.py migrate
python manage.py runserver
```

---

## Observações

* Projeto estruturado seguindo boas práticas Django
* Configuração via variáveis de ambiente
* Autenticação JWT aplicada globalmente na API
* Compatível com execução local ou containerizada
