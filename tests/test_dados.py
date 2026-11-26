
import pandas as pd
import pytest
from pathlib import Path


# Localização da pasta principal do projeto
PASTA_PROJETO = Path(__file__).resolve().parents[1]


# Municípios que serão testados
arquivos = [
    "clima_nova_cruz.csv",
    "clima_canguaretama.csv"
]


@pytest.fixture(params=arquivos)
def tabela(request):
    caminho = PASTA_PROJETO / "dados" / request.param

    return pd.read_csv(
        caminho,
        parse_dates=["data"],
        index_col="data"
    )


def test_quantidade_linhas(tabela):
    # São três anos bissextos no período: 2016, 2020 e 2024.
    # Por isso, temos 3650 + 3 = 3653 dias.
    assert len(tabela) == 3653


def test_datas(tabela):
    datas_esperadas = pd.date_range(
        start="2015-01-01",
        end="2024-12-31",
        freq="D"
    )

    assert tabela.index.equals(datas_esperadas)


def test_valores_vazios(tabela):
    valores_vazios = tabela.isna().sum()

    assert valores_vazios.sum() == 0, (
        f"Existem valores vazios:\n{valores_vazios}"
    )


def test_temperaturas(tabela):
    assert (tabela["tmin"] <= tabela["tmax"]).all()


def test_chuva(tabela):
    assert (tabela["chuva"] >= 0).all()
