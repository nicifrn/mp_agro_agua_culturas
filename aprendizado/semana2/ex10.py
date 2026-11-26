from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

caminho = Path("aprendizado/clima_exemplo.csv")
tabela = pd.read_csv(caminho)
marco = tabela[tabela["data"].astype(str).str.startswith("2024-03")].copy()

dias = pd.to_datetime(marco["data"]).dt.day
chuvas = marco["chuva"]

plt.figure(figsize=(10, 5))
plt.bar(dias, chuvas)
plt.xlabel("Dia")
plt.ylabel("Chuva (mm)")
plt.xticks(dias)
plt.tight_layout()

saida = Path(__file__).resolve().parent / "grafico_marco.png"
plt.savefig(saida)
plt.close()