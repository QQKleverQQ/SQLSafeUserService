DB_PY = r
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# For production you'd use a proper DB URI. For this example we default to sqlite in-memory when requested.


def get_engine(url: str | None = None):
if url:
return create_engine(url, future=True)
# default: file-based sqlite for demo
return create_engine('sqlite:///./sqlsafe.db', future=True)




def get_session_factory(engine):
return sessionmaker(bind=engine, expire_on_commit=False, future=True)