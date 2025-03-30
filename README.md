# fastapi-sqlite
Criando um Endpoint para Cálculo do Flat Price da Soja

## Run application
1. instalar requirements.txt
   > pip install -r requirements.txt
2. acessar diretório app 
    > cd app
3. inicializar api 
    > uvicorn main:app --reload


Podemos testar a api por linha de comando ou usando aplicações como postman 

> curl -X 'POST' 'http://127.0.0.1:8000/api/flat_price' \
     -H 'Content-Type: application/json' \
     -d '{"contract_month": ["MAY24"], "basis": 1.5}'

#### Modelo input
```  
{
  "basis": -5.00,
  "contract_months": ["MAY24"]
}
```
#### Output esperado 
``` 
{
      "results": [
    {
      "contract_month": "MAY24",
      "cbot_price":125.75,"basis":1.5,"flat_price":140.27
    }
  ]
}
```

## Run testes
No diretório 'tests '
> pytest -q test.py