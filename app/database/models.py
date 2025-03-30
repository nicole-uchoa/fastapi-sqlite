from pydantic import BaseModel, field_validator
import re
from typing import List
from app.custom_error import ValueErrorMonth, ValueErrorBasis

class FlatPrice(BaseModel):
    basis: float
    contract_month: List[str]

    @field_validator("contract_month") 
    def validate_mes(cls, v):
        if not isinstance(v, list) or not all(isinstance(m, str) for m in v):
            raise ValueErrorMonth("Contract month must be a list of string MMMYY (ex: ['MAY24'])")        
        for month in v:
            if not re.match(r"^[A-Z]{3}\d{2}$", month):
                raise ValueErrorMonth("Contract month must be a list of string MMMYY (ex: ['MAY24'])")
        return v
    
    @field_validator("basis") 
    def validate_price(cls, v):
        if v >= 50 or v <= -50:
            raise ValueErrorBasis("Basis must be a number between -50 and 50")
        return v
    
