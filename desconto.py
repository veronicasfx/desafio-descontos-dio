descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input().strip())
cupom = input().strip()

if cupom in descontos:
    percentual_desconto = descontos[cupom]
else:
    percentual_desconto = 0.0

valor_desconto = preco * percentual_desconto
valor_final = preco - valor_desconto

print(f"{valor_final:.2f}")
