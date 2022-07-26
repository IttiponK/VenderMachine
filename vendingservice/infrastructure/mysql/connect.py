from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def connect_mysql_db():
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ittimoo:ittimoo@vendingdb/vendingservice"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base = declarative_base()
    
    class Cashbag(Base):
        __tablename__ = 'cashbag'
        id = Column(Integer,primary_key=True)
        value = Column(Integer)
        quantity = Column(Integer)
        active = Column(Integer)
        create_at = Column(DateTime)
        
    def get_database_session():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
        
    return get_database_session,Cashbag