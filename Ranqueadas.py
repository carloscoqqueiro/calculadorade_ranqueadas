def calculator(pardidasG, pardidasP):
    calculo = pardidasG - pardidasP
    return calculo

resultado = calculator(58, 14)
vitorias = resultado
rank = ""

while True:
    if (vitorias < 10):
        rank = "ferro"
    if (vitorias > 11 and vitorias < 20):
        rank = "bronze"
    if (vitorias > 21 and vitorias < 50):
        rank = "prata"
    if (vitorias > 51 and vitorias < 80):
        rank = "ouro"
    if (vitorias > 81 and vitorias < 90):
        rank = "diamente"
    if (vitorias > 91 and vitorias < 100):
        rank = "lendário"
    if (vitorias >= 101):
        rank = "imortal"

    break

print(f"O Herói tem um saldo de {vitorias} vitórias e está no rank {rank}")


