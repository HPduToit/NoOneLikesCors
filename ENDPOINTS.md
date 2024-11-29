# API Documentation

## Endpoints

### `GET` /openapi.json

#### Parameters:

- `req`: <class 'starlette.requests.Request'>


### `GET` /docs

#### Parameters:

- `req`: <class 'starlette.requests.Request'>


### `GET` /docs/oauth2-redirect

#### Parameters:

- `req`: <class 'starlette.requests.Request'>


### `GET` /redoc

#### Parameters:

- `req`: <class 'starlette.requests.Request'>


### `POST` /login

#### Parameters:

- `form_data`: <class 'fastapi.security.oauth2.OAuth2PasswordRequestForm'>
- `db`: <class 'sqlalchemy.orm.session.Session'>


### `GET` /users/me

#### Parameters:

- `current_user`: <class 'ums.models.User'>


### `POST` /register

#### Parameters:

- `user`: <class 'ums.main.UserCreate'>
- `db`: <class 'sqlalchemy.orm.session.Session'>


### `POST` /ping

#### Parameters:

- `db`: <class 'sqlalchemy.orm.session.Session'>

