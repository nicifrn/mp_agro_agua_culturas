from pathlib import Path
import pandas as pd

caminho = Path("aprendizado/clima_exemplo.csv")
tabela = pd.read_csv(caminho)

marco = tabela[tabela["data"].astype(str).str.startswith("2024-03")].copy()

total_chuva = round(marco["chuva"].sum(), 2)
media_tmax = round(marco["tmax"].mean(), 2)
dias_acima_33 = len(marco[marco["tmax"] > 33])

marco["amplitude"] = marco["tmax"] - marco["tmin"]
media_amplitude = round(marco["amplitude"].mean(), 2)

idx_mais_chuvoso = marco["chuva"].idxmax()
dia_mais_chuvoso = marco.loc[idx_mais_chuvoso, "data"]
maior_chuva = round(marco.loc[idx_mais_chuvoso, "chuva"], 2)

print(f"chuva {total_chuva}; máxima média {media_tmax}; {dias_acima_33} dias acima de 33 °C")
print(f"amplitude média {media_amplitude}; dia mais chuvoso {dia_mais_chuvoso}, com {maior_chuva} mm")