"""Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. 
Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente."""

clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

for cliente in clientes:
    print(cliente)

# O laço for é mais adequado nesse caso, pois sabemos o número exato de elementos na lista (5 nomes).
# Com o laço for, iremos percorrer todos os itens de maneira clara e direta, sem precisar gerenciar manualmente um contador ou condição de parada.
