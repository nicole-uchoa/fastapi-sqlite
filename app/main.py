from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from sqlalchemy.orm import Session
from app.database.database import Base, engine, init_db, SessionLocal
from app.database.models import FlatPrice
from app.database.cache import get_cached_price
from app.calculos import CalcFlatPrice
from app.custom_error import ValueErrorMonth, ValueErrorBasis

Base.metadata.create_all(bind=engine)
init_db()

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    return {"message": "Hello desafio germinare"}

@app.post("/api/flat_price")
def calc_flat_price(request: dict, db: Session = Depends(get_db)):
    try:
        validated_request = FlatPrice(**request)
    except ValueErrorMonth:        
        raise HTTPException(status_code=400, detail="Contract month must be a list of string MMMYY (ex: ['MAY24'])")
    except ValueErrorBasis:
        raise HTTPException(status_code=400, detail="Basis must be a number between -50 and 50")

    try:
        resultados = []
        for month in validated_request.contract_month:
            price = get_cached_price(month, db)
            if price is None:
                raise HTTPException(status_code=404, detail=f"Contract month {month} not found")

            flat_price = CalcFlatPrice.calcular_flat_price(price, validated_request.basis)
            resultados.append({
                  "contract_month": month,
                  "cbot_price": price,
                  "basis": validated_request.basis,   
                  "flat_price": flat_price
                })
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="Unexpected server error")
    
    return {"results": resultados}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)