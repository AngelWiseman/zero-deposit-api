# Zero Deposit API

This Django REST API manages property listings. You can quickly replicate the full environment — including the database and its data — using the provided PostgreSQL dump file or use the standard SQLITE for testing.

---

## Getting Started (With Database Backup)

### Prerequisites

- Python 3.8+
- pip
- PostgreSQL
- Virtual environment

---

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/zero-deposit-api.git
cd zero-deposit-api
```

### 2. Set Up the Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Restore the PostgreSQL Database

First, ensure PostgreSQL is running and then create the user and database:
```bash
sudo -u postgres psql
```

Inside the PostgreSQL shell:
```bash
CREATE DATABASE zero_deposit_db;
CREATE USER zero_deposit_user WITH PASSWORD 'securepassword123';
GRANT ALL PRIVILEGES ON DATABASE zero_deposit_db TO zero_deposit_user;
\q
```

Then restore the backup:
```bash
pg_restore -U zero_deposit_user -d zero_deposit_db zero_deposit_db_backup.dump
```
### OR run SQLITE Database
```bash
export USE_SQLITE=true
python manage.py migrate
```

### 5. Run Migrations
```bash
python manage.py migrate
```

### 6. Create a Superuser
```bash
python manage.py createsuperuser
```

### 7. Run the Development Server
```bash
python manage.py runserver
```

Acess Django interface: http://127.0.0.1:8000/admin

## Running Tests
```bash
python manage.py test

python manage.py test users

python manage.py test properties
```

## REST API Endpoints

#### User Endpoints

| Method | Endpoint             | Description                   |
|--------|----------------------|-------------------------------|
| POST   | `/api/token/`        | Obtain auth token (login)     |
| POST   | `/api/token/refresh/`| Refresh auth token (login)     |
| POST   | `/api/users/register/`     | Register a new user           |

### Properties

| Method | Endpoint             | Description           |
|--------|----------------------|-----------------------|
| GET    | `/api/properties/`   | List all properties   |
| POST   | `/api/properties/`   | Create a new property |
| GET    | `/api/properties/<id>/` | Retrieve a property   |
| DELETE | `/api/properties/<id>/` | Delete a property     |

> ⚠️ **Note:** All property endpoints require the user to be authenticated using a token.