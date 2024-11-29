from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ums.logger import log_root, log_ume

db_name = "UMSDB"
DATABASE_URL = f"mysql+pymysql://root:user@localhost:50011/{db_name}"

# Connect to the MySQL server without specifying a database. For existance check.
engine = create_engine(DATABASE_URL.rsplit("/", 1)[0])

# Connects to the server in general. Not a DB. Create the database if it doesn't exist.
# This is really not needed.. just for convienence
with engine.connect() as conn:
    result = conn.execute(
        text(
            "SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = :db_name",
        ),
        {"db_name": db_name}  # Safely pass the parameter
    )
    if result.fetchone():
        log_root.info(f"The database '{db_name}' already exists.")
    else:
        conn.execute(text(f"CREATE DATABASE {db_name}"))
        log_root.warning(f"Database '{db_name}' created successfully.")

# Connect to the database
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
try:
    with engine.connect() as conn:
        # Attempt a simple query to confirm the connection
        result = conn.execute(text("SELECT 1"))
        log_root.info("Connection to the database was successful.")
except Exception as e:
    log_root.error(f"Failed to connect to the database with error: {e}")

# A session factory that provides database sessions for requests.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)