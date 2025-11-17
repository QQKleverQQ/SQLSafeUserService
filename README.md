# (markdown text)
README = r"""
# SQLSafe User Service


This minimal project shows:
- A `users` table (SQLAlchemy) with an integer `id` primary key.
- Safe data access using SQLAlchemy and parameterized queries (prevents SQL Injection).
- Password hashing using bcrypt.
- Unit tests (uses pytest) with in-memory SQLite and mocks where appropriate.
- Example of coverage setup (pytest-cov).


## Requirements
Python 3.10+


## Install
```bash
python -m venv .venv
source .venv/bin/activate # on Windows: .venv\Scripts\activate
pip install -e .
```


## Running tests with coverage
```bash
pytest --cov=app --cov-report=term-missing
```


Goal: 100% coverage for the `app` package in these examples.
"""