import pytest
from decouple import config 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base

# Crie um banco de dados SQLite em memória para os testes
DB_URL = config('DB_URL')

@pytest.fixture(scope="session")
def db_engine():
    """Configura o engine do banco para testes."""
    engine = create_engine(DB_URL)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def db_session(db_engine):
    """Fixture para gerenciar a sessão do banco de dados."""
    Session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)
    session = Session()
    yield session
    session.close()
