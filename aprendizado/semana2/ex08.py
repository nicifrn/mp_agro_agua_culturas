import csv
from pathlib import Path

caminho = Path("aprendizado/clima_exemplo.csv")
total_chuva = 0.0
dias_secos = 0

with caminho.open(encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    for linha in leitor:
        if linha["data"].startswith("2024-03"):
            chuva = float(linha["chuva"])
            total_chuva += chuva
            if chuva < 1.0:
                dias_secos += 1

print(f"total {round(total_chuva, 1)} mm e {dias_secos} dias secos")