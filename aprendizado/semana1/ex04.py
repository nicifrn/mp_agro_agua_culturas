chuvas = [8.62, 0.88, 2.11, 1.71, 15.56, 6.27, 8.06]

total = 0.0
maior = chuvas[0]
dias_secos = 0

for chuva in chuvas:
    total += chuva
    if chuva > maior:
        maior = chuva
    if chuva < 1:
        dias_secos += 1

total_arredondado = round(total, 2)
print(f"total {total_arredondado}, maior {maior}, {dias_secos} dia seco")