from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime, func
from sqlalchemy.orm import sessionmaker, declarative_base
from time import sleep

DATABASE_URL = "sqlite:///./flatprice.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class SoyPriceTable(Base):
    __tablename__ = "soybean_meal_prices"
    id = Column(Integer, primary_key=True, index=True)
    contract_month = Column(String(5), nullable=False) # "Deve buscar o último preço futuro disponível no banco de dados para cada contract_month" - mais de um preço por mês
    price = Column(Float, nullable=False)
    created_at = Column(DateTime, default=func.now())

def init_db():
    db = SessionLocal()
    if not db.query(SoyPriceTable).first():
        initial_data = [
            {"contract_month": "MAY24", "price": 125.75},
            {"contract_month": "JUN24", "price": 170.46},
            {"contract_month": "JUL24", "price": 205.41},
            {"contract_month": "SEP24", "price": 188.23},
            {"contract_month": "MAY24", "price": 145.75},
            # {"contract_month": "MAY21", "price": 145.75},
        ]
        for data in initial_data:
            db.add(SoyPriceTable(**data)) 
        db.commit()
    db.close()