from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def connect_mysql_db():
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ittimoo:ittimoo@stockdb/stockservice"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base = declarative_base()
    
    class Stock(Base):
        __tablename__ = 'stock'
        id = Column(Integer,primary_key=True)
        name = Column(String)
        product_id = Column(String)
        quantity = Column(Integer)
        price = Column(Integer)
        img = Column(String)
        version = Column(Integer)
        create_at = Column(DateTime)
        
    def get_database_session():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
        
    return get_database_session,Stock