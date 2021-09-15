from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from sqlalchemy.ext.declarative import as_declarative

SQL_DATABASE_URL = 'postgresql://postgres:postgres@db:5432/postgres'

engine = create_engine(SQL_DATABASE_URL, echo=True)

metadata = MetaData(bind=engine)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=True)


@as_declarative(metadata=metadata)
class Base:
    pass



