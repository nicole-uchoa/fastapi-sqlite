import pytest
from app.calculos import CalcFlatPrice

@pytest.mark.parametrize("price, basis, expected", [
    (125.75,-5, 133.1),
    (170.46,-5, 182.39),
    (205.41,-5, 220.91), 
])

def test_calcular_preco_soja(price, basis, expected):
    assert CalcFlatPrice.calcular_flat_price(price, basis) == expected
