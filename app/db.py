from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker


engine = create_engine("sqlite:///users.db", echo=False, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)




def get_db():
db = SessionLocal()
try:
yield db
finally:
db.close()
