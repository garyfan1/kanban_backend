# Kanban Board — Backend

Live site: [kanban-demo.live](https://kanban-demo.live)

REST API backend for a single-user Kanban task management app.

## Tech Stack

- Django 6 + Django REST Framework
- JWT authentication (simplejwt)
- PostgreSQL

Frontends:
- Nuxt 4: [garyfan1/kanban_nuxt](https://github.com/garyfan1/kanban_nuxt)
- Vue 3: [garyfan1/kanban_frontend](https://github.com/garyfan1/kanban_frontend)

## API

| Method | Endpoint | Auth | Description |
|---|---|---|---|
| POST | `/api/auth/login/` | No | Get access + refresh tokens |
| POST | `/api/auth/refresh/` | No | Refresh access token |
| GET | `/api/tasks/` | Yes | List tasks |
| POST | `/api/tasks/` | Yes | Create task |
| PATCH | `/api/tasks/{id}/` | Yes | Update task |
| DELETE | `/api/tasks/{id}/` | Yes | Delete task |
| GET | `/api/health/` | No | Health check |

Task `status` values: `todo`, `doing`, `done`

## Setup

Copy `.env.example` to `.env` and fill in your values.

```bash
# Start PostgreSQL
docker-compose up

# Apply migrations
python manage.py migrate

# Run dev server
python manage.py runserver
```
