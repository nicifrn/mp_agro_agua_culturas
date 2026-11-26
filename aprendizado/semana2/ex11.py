import requests

codigos = {
    "Nova Cruz": "2408300",
    "Canguaretama": "2402204",
}

for nome_esperado, codigo in codigos.items():
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}"
    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()
    dados = resposta.json()

    nome = dados["nome"]
    microrregiao = dados["microrregiao"]["nome"]
    mesorregiao = dados["microrregiao"]["mesorregiao"]["nome"]

    print(f"{nome}: microrregião {microrregiao}; mesorregião {mesorregiao}")