"""João recebeu uma lista de valores representando as receitas de sua loja de roupas.
Ele quer calcular a soma total dessas receitas para entender o desempenho financeiro semanal."""

numeros = [10, 20, 30, 40, 50]

soma = 0

for numero in numeros:
    soma += numero

print(f"A soma total das receitas é: {soma}")
