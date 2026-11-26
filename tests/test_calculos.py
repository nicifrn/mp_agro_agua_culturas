from datetime import date
from pathlib import Path
import pandas as pd
import pyet
import pytest

from calculos import (
    angulo_por_do_sol,
    declinacao_solar,
    dia_do_ano,
    distancia_relativa,
    et0_hargreaves,
    graus_para_radianos,
    mj_para_mm,
    radiacao_extraterrestre,
)


def _detectar_coluna(df: pd.DataFrame, candidatas: list[str]) -> str:
    mapa = {col.strip().lower(): col for col in df.columns}
    for cand in candidatas:
        if cand.lower() in mapa:
            return mapa[cand.lower()]
    raise KeyError(f"Nenhuma das colunas {candidatas} encontrada em {list(df.columns)}")


def _obter_lat_nova_cruz() -> float:
    df_mun = pd.read_csv(Path("dados/municipios.csv"))
    col_mun = _detectar_coluna(df_mun, ["municipio", "nome", "cidade"])
    col_lat = _detectar_coluna(df_mun, ["latitude", "lat"])
    norm = df_mun[col_mun].astype(str).str.strip().str.lower().str.replace(" ", "_")
    return float(df_mun.loc[norm == "nova_cruz", col_lat].iloc[0])


def test_exemplo_7_graus_para_radianos():
    lat_norte = 13 + 44 / 60  # 13° 44' norte
    lat_sul = -(22 + 54 / 60)  # 22° 54' sul

    assert graus_para_radianos(lat_norte) == pytest.approx(0.240, abs=0.001)
    assert graus_para_radianos(lat_sul) == pytest.approx(-0.400, abs=0.001)


def test_dia_do_ano():
    assert dia_do_ano(date(2026, 9, 3)) == 246
    assert dia_do_ano(date(2024, 9, 3)) == 247
    assert dia_do_ano(date(2024, 1, 1)) == 1
    assert dia_do_ano(date(2024, 12, 31)) == 366


def test_exemplo_8_radiacao_extraterrestre():
    lat_graus = -20.0
    j = 246
    lat_rad = graus_para_radianos(lat_graus)

    dr = distancia_relativa(j)
    delta = declinacao_solar(j)
    ws = angulo_por_do_sol(lat_rad, delta)
    ra = radiacao_extraterrestre(lat_graus, j)
    ra_mm = mj_para_mm(ra)

    assert dr == pytest.approx(0.985, abs=0.001)
    assert delta == pytest.approx(0.120, abs=0.001)
    assert ws == pytest.approx(1.527, abs=0.001)
    assert ra == pytest.approx(32.2, abs=0.1)
    assert ra_mm == pytest.approx(13.1, abs=0.1)


def test_tmax_menor_que_tmin_levanta_value_error():
    with pytest.raises(ValueError, match="tmax menor que tmin"):
        et0_hargreaves(tmax=23.0, tmin=26.0, tmedia=24.5, ra_mm=14.0)


def test_conta_a_mao_nova_cruz():
    df = pd.read_csv(Path("dados/clima_nova_cruz.csv"))
    col_data = _detectar_coluna(df, ["data", "date"])
    col_tmax = _detectar_coluna(df, ["tmax", "temperatura_maxima", "temp_max"])
    col_tmin = _detectar_coluna(df, ["tmin", "temperatura_minima", "temp_min"])
    col_tmed = _detectar_coluna(df, ["tmedia", "tmean", "temperatura_media", "temp_med"])

    linha = df.iloc[0]
    lat_graus = _obter_lat_nova_cruz()
    j = dia_do_ano(date.fromisoformat(str(linha[col_data])[:10]))

    ra_mm = mj_para_mm(radiacao_extraterrestre(lat_graus, j))
    et0 = et0_hargreaves(
        tmax=float(linha[col_tmax]),
        tmin=float(linha[col_tmin]),
        tmedia=float(linha[col_tmed]),
        ra_mm=ra_mm,
    )

    valor_esperado_mao = round(et0, 2)
    assert et0 == pytest.approx(valor_esperado_mao, abs=0.02)


def test_comparacao_com_pyet_primeiros_31_dias():
    df_clima = pd.read_csv(Path("dados/clima_nova_cruz.csv")).head(31).copy()
    col_data = _detectar_coluna(df_clima, ["data", "date"])
    col_tmax = _detectar_coluna(df_clima, ["tmax", "temperatura_maxima", "temp_max"])
    col_tmin = _detectar_coluna(df_clima, ["tmin", "temperatura_minima", "temp_min"])
    col_tmed = _detectar_coluna(df_clima, ["tmedia", "tmean", "temperatura_media", "temp_med"])

    df_clima["data_dt"] = pd.to_datetime(df_clima[col_data])
    df_clima = df_clima.set_index("data_dt")

    lat_graus = _obter_lat_nova_cruz()
    lat_rad = graus_para_radianos(lat_graus)

    et0_pyet = pyet.hargreaves(
        tmean=df_clima[col_tmed],
        tmax=df_clima[col_tmax],
        tmin=df_clima[col_tmin],
        lat=lat_rad,
    )

    for dt_idx, row in df_clima.iterrows():
        j = dia_do_ano(dt_idx.date())
        ra_mm = mj_para_mm(radiacao_extraterrestre(lat_graus, j))
        et0_nosso = et0_hargreaves(
            tmax=float(row[col_tmax]),
            tmin=float(row[col_tmin]),
            tmedia=float(row[col_tmed]),
            ra_mm=ra_mm,
        )
        assert abs(et0_nosso - float(et0_pyet.loc[dt_idx])) < 0.1