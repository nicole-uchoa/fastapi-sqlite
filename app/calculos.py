class CalcFlatPrice:
    @staticmethod
    def calcular_flat_price(price: float, basis: float) -> float:
        # Flat Price = (Preço Futuro (CBOT) + Basis)*Fator de conversão
        fator_conversao = 1.10231
        flat_price = (price + basis)*fator_conversao
        return round(flat_price, 2)