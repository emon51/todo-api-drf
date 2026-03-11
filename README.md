# Todo API

A REST API for managing todos built with Django and PostgreSQL, running fully in Docker.

---

## Tech Stack

- Python, Django, Django REST Framework
- PostgreSQL 15
- JWT Authentication
- Docker & Docker Compose

---

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## Quick Start
```bash
# 1. Clone the repository
git clone 
cd todo_api

# 2. Create secrets directory and files
mkdir secrets
echo "todo_db" > secrets/db_name.txt
echo "todo_user" > secrets/db_user.txt
echo "todo_password" > secrets/db_password.txt
echo "your-secret-key-change-this" > secrets/secret_key.txt

# 3. Start the app
docker-compose up --build
```

API is now running at `http://localhost:8000/api/v1/`

---

## API Endpoints

| Method | Endpoint | Auth Required | Description |
|--------|----------|---------------|-------------|
| POST | `/api/v1/auth/register/` | No | Register a new user |
| POST | `/api/v1/auth/login/` | No | Login and get JWT tokens |
| GET | `/api/v1/todos/` | Yes | List all your todos |
| POST | `/api/v1/todos/` | Yes | Create a new todo |
| GET | `/api/v1/todos/<id>/` | Yes | Get a single todo |
| PUT | `/api/v1/todos/<id>/` | Yes | Update a todo |
| PATCH | `/api/v1/todos/<id>/` | Yes | Partially update a todo |
| DELETE | `/api/v1/todos/<id>/` | Yes | Delete a todo |

See [API_DOCS.md](API_DOCS.md) for full request/response examples.

---

## Query Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `status` | Filter by status | `?status=completed` or `?status=pending` |
| `search` | Search by title | `?search=groceries` |
| `sort_by` | Sort by field | `?sort_by=title` or `?sort_by=created_at` |
| `order` | Sort direction | `?order=asc` or `?order=desc` |
| `page` | Page number | `?page=2` |
| `limit` | Items per page | `?limit=5` |

---

## Running Tests
```bash
# Make sure containers are running
docker-compose up -d

# Run tests with coverage report
docker-compose exec web pytest tests/ -v
```

**Expected result:** 47 passed, 95% coverage

---

## Project Structure
```
todo_api/
├── apps/
│   ├── todos/          # Todo CRUD logic
│   └── users/          # Registration & login
├── config/             # Django settings, URLs, pagination
├── tests/              # All tests
├── secrets/            # Credentials — never committed to git
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── API_DOCS.md
```

---

## Useful Commands
```bash
# Start in background
docker-compose up -d

# Stop containers
docker-compose down

# Stop and delete all data
docker-compose down -v

# View logs
docker-compose logs -f web
```

---

## Security Notes

- `secrets/` is in `.gitignore` — never committed to git
- All credentials are managed via Docker secrets
- JWT tokens expire after 1 hour