from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import text
from sqlalchemy.orm import Session
from ums.models import Base
from ums.database import engine
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from ums.settings import settings
from ums.database import SessionLocal



app = FastAPI()

# Shit that's allowed to connect to my API


# fmt: off
app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:4200'],      # Allows requests from specified origins
    # Set to True if your frontend needs to send cookies or authentication headers.
    allow_credentials=True,
    allow_methods=["*"],        # Allows all HTTP methods
    allow_headers=["*"],        # Allows all headers
)
# fmt: on

# Create the tables
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get(settings.endpoint.ping_ep)
def ping(db: Session = Depends(get_db)):
    try:
        return {"message": "pong"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
