
import os
import json
import requests
import pandas as pd
import numpy as np


URL = "https://power.larc.nasa.gov/api/temporal/daily/point"


municipios = {
    "Nova Cruz": {
        "codigo_ibge": 2408300,
        "latitude": -6.4778,
        "longitude": -35.4339
    },
    "Canguaretama": {
        "codigo_ibge": 2402204,
        "latitude": -6.3800,
        "longitude": -35.1281
    }
}


PARAMETROS = (
    "T2M,T2M_MAX,T2M_MIN,PRECTOTCORR,"
    "RH2M,WS2M,ALLSKY_SFC_SW_DWN"
)


def baixar(latitude, longitude, inicio, fim):
    parametros = {
        "parameters": PARAMETROS,
        "community": "AG",
        "longitude": longitude,
        "latitude": latitude,
        "start": inicio,
        "end": fim,
        "format": "JSON"
    }

    resposta = requests.get(URL, params=parametros, timeout=120)

    resposta.raise_for_status()

    return resposta.json()


def json_para_tabela(dados):
    parametros = dados["properties"]["parameter"]

    tabela = pd.DataFrame(parametros)

    tabela.index = pd.to_datetime(
        tabela.index,
        format="%Y%m%d"
    )

    tabela.index.name = "data"

    tabela = tabela.rename(columns={
        "T2M": "tmedia_nasa",
        "T2M_MAX": "tmax",
        "T2M_MIN": "tmin",
        "PRECTOTCORR": "chuva",
        "RH2M": "umidade",
        "WS2M": "vento",
        "ALLSKY_SFC_SW_DWN": "radiacao"
    })

    tabela = tabela.replace(-999, np.nan)

    tabela["tmedia"] = (tabela["tmax"] + tabela["tmin"]) / 2

    return tabela


def main():

    os.makedirs("dados/brutos", exist_ok=True)
    os.makedirs("dados", exist_ok=True)

    dados_municipios = []

    for nome, municipio in municipios.items():

        nome_arquivo = nome.lower().replace(" ", "_")

        caminho_json = f"dados/brutos/nasa_{nome_arquivo}.json"
        caminho_csv = f"dados/clima_{nome_arquivo}.csv"

        if os.path.exists(caminho_json):

            print(f"Arquivo existente: {caminho_json}")

            with open(caminho_json, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)

        else:

            print(f"Baixando dados de {nome}...")

            dados = baixar(
                municipio["latitude"],
                municipio["longitude"],
                "20150101",
                "20241231"
            )

            with open(caminho_json, "w", encoding="utf-8") as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        tabela = json_para_tabela(dados)

        tabela.to_csv(caminho_csv, index=True)

        print(f"CSV salvo: {caminho_csv}")

        coordenadas = dados["geometry"]["coordinates"]

        dados_municipios.append({
            "municipio": nome,
            "codigo_ibge": municipio["codigo_ibge"],
            "latitude": municipio["latitude"],
            "longitude": municipio["longitude"],
            "altitude": coordenadas[2]
        })

    tabela_municipios = pd.DataFrame(dados_municipios)

    tabela_municipios.to_csv(
        "dados/municipios.csv",
        index=False
    )

    print("Dados dos municípios salvos!")


if __name__ == "__main__":
    main()
