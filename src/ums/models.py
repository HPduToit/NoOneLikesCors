import bcrypt
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    email = Column(String(120), unique=True, index=True)
    password_hash = Column(String(128))
    # otp = Column(String(6))
    # otp_valid_until = Column(DateTime)

    def set_password(self, plain_password):
        hashed = bcrypt.hashpw(plain_password.encode("utf-8"), bcrypt.gensalt())
        self.password_hash = hashed.decode("utf-8")

    def verify_password(self, plain_password):
        return bcrypt.checkpw(
            plain_password.encode("utf-8"), self.password_hash.encode("utf-8")
        )
