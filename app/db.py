DB_PY = r
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker




def get_engine(url: str | None = None):
if url:
return create_engine(url, future=True)
return create_engine('sqlite:///./sqlsafe.db', future=True)




def get_session_factory(engine):
return sessionmaker(bind=engine, expire_on_commit=False, future=True)
