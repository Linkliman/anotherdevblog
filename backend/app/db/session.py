from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from .models import Base
from app.core.config import config


# Create the SQLAlchemy engine and session
engine = create_engine(f"postgresql://{config['psql_user']}:{config['psql_password']}@{config['psql_host']}/{config['psql_database']}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Create the database tables
Base.metadata.create_all(bind=engine)