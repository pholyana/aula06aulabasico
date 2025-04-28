nomes=["pedro","tiago","ezequiel","barquinho","joão",]

nome=input("Digite um nome que voce quer encontrar:")
for y in range(len(nome)):
    if nome== nomes [y]:
        print(f"achei o {nome} na posição {y}")