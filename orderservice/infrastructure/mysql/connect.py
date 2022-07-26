from sqlalchemy import create_engine,Column,Integer,String,DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

def connect_mysql_db():
    SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://ittimoo:ittimoo@ordersdb/orderservice"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    Base = declarative_base()
    
    class Transaction(Base):
        __tablename__ = 'transaction'
        id = Column(Integer,primary_key=True)
        name = Column(String)
        product_id = Column(String)
        quantity = Column(Integer)
        total_amount = Column(Integer)
        pay_amount = Column(Integer)
        pay_amount_detail = Column(String)
        change = Column(Integer)
        change_detail = Column(String)
        
    def get_database_session():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()
        
    return get_database_session,Transaction