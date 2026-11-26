
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


# Caminhos das pastas
PASTA_PROJETO = Path(__file__).resolve().parent
PASTA_DADOS = PASTA_PROJETO / "dados"
PASTA_RESULTADOS = PASTA_PROJETO / "resultados"
PASTA_GRAFICOS = PASTA_PROJETO / "graficos"


# Cria as pastas caso ainda não existam
PASTA_RESULTADOS.mkdir(exist_ok=True)
PASTA_GRAFICOS.mkdir(exist_ok=True)


# Lê os CSVs dos municípios
nova_cruz = pd.read_csv(
    PASTA_DADOS / "clima_nova_cruz.csv",
    parse_dates=["data"],
    index_col="data"
)

canguaretama = pd.read_csv(
    PASTA_DADOS / "clima_canguaretama.csv",
    parse_dates=["data"],
    index_col="data"
)


# Guarda os municípios em um dicionário
municipios = {
    "Nova Cruz": nova_cruz,
    "Canguaretama": canguaretama
}


# 1. Calcula a chuva total de cada ano
chuvas_anuais = []

for nome, tabela in municipios.items():

    chuva_anual = tabela.groupby(tabela.index.year)["chuva"].sum()

    for ano, total in chuva_anual.items():

        chuvas_anuais.append({
            "municipio": nome,
            "ano": ano,
            "chuva_total": total
        })


# Transforma os resultados em DataFrame
resultado_anual = pd.DataFrame(chuvas_anuais)

# Salva o resultado anual
resultado_anual.to_csv(
    PASTA_RESULTADOS / "chuva_anual.csv",
    index=False
)


# 2. Calcula a chuva média de cada mês
chuvas_mensais = {}

for nome, tabela in municipios.items():

    chuvas_mensais[nome] = (
        tabela.groupby(tabela.index.month)["chuva"].mean()
    )


# 3. Cria o gráfico de barras lado a lado
meses = [
    "Jan", "Fev", "Mar", "Abr",
    "Mai", "Jun", "Jul", "Ago",
    "Set", "Out", "Nov", "Dez"
]

posicoes = np.arange(12)
largura = 0.35

plt.figure(figsize=(12, 6))

plt.bar(
    posicoes - largura / 2,
    chuvas_mensais["Nova Cruz"].reindex(range(1, 13)).values,
    largura,
    label="Nova Cruz"
)

plt.bar(
    posicoes + largura / 2,
    chuvas_mensais["Canguaretama"].reindex(range(1, 13)).values,
    largura,
    label="Canguaretama"
)

plt.xticks(posicoes, meses)

plt.xlabel("Meses")
plt.ylabel("Chuva média (mm/dia)")
plt.title("Média mensal de precipitação")

plt.legend()
plt.tight_layout()

# Salva o gráfico
plt.savefig(
    PASTA_GRAFICOS / "chuva_mensal.png",
    dpi=300
)

plt.show()


# 4. Identifica o ano mais seco e o mais chuvoso de Nova Cruz
chuva_nova_cruz = resultado_anual[
    resultado_anual["municipio"] == "Nova Cruz"
]

ano_mais_seco = chuva_nova_cruz.loc[
    chuva_nova_cruz["chuva_total"].idxmin()
]

ano_mais_chuvoso = chuva_nova_cruz.loc[
    chuva_nova_cruz["chuva_total"].idxmax()
]

print("\nANÁLISE DE NOVA CRUZ")

print(
    f"Ano mais seco: {int(ano_mais_seco['ano'])} "
    f"({ano_mais_seco['chuva_total']:.2f} mm)"
)

print(
    f"Ano mais chuvoso: {int(ano_mais_chuvoso['ano'])} "
    f"({ano_mais_chuvoso['chuva_total']:.2f} mm)"
)

print("\nAnálise concluída!")
