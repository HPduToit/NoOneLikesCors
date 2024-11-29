# User Session Management
This project is a micro service for managing users sessions, tokens and access to 
restriced pages/screens. It follows the stateless session management approach. Tokens 
are king and nothing representing the state is stored in the database. All HTTP calls
are inherently stateless and will require an access token for user authentication. 

## Create the MySQL DB
This creates a MySQL DB called `UMSDB` available on port `50011` as user `root`:  
`docker compose up`

## Formatting
The package uses `Black` for formatting. 

## Logging

There are two loggers, `root` and `ums`. Root logs to the console and ums to a log file called
ums_logfile.log in the logs directory. 

## Python stuff
> **Without venvit**

Create the venv (used 3.12.4): `python -m venv ums`  
Activate the venv: `source.sh`
Install packages with `poetry install` (install poetry first with `pip install poetry` if you don't have it)

> **With venvit**

`vn ...` and `vi ...`

The below packages are now part of the pyproject.toml file.  
This list is no longer updated (17/11/2024)

```bash
pip install SQLAlchemy
pip install bcrypt
pip install pymysql
pip install cryptography
pip install fastapi uvicorn
pip install colorlog
pip install jose
pip install python-jose
pip install python-multipart
pip install pydantic[email]
pip install pydantic-settings
```

## Run FastAPI (the application)
This will create the database if it does not exsist as well as the database tables.  
`uvicorn src.ums.main:app --reload` or simply `start.ps1`