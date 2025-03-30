from app.database.database import SoyPriceTable
from typing import Dict
from sqlalchemy.orm import Session


cache: Dict[str, float] = {}

def get_cached_price(mes: str, db: Session):
    if mes in cache:
        return cache[mes]

    try:
        registro = db.query(SoyPriceTable).filter(SoyPriceTable.contract_month == mes).order_by(SoyPriceTable.created_at.desc()).first()
        if registro:
            cache[mes] = registro.price
            return registro.price
    finally:
        db.close()
    
    return None
