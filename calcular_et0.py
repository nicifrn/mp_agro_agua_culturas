from datetime import date
from pathlib import Path
import pandas as pd

from calculos import dia_do_ano, et0_hargreaves, mj_para_mm, radiacao_extraterrestre

MUNICIPIOS = ["nova_cruz", "canguaretama"]


def _detectar_coluna(df: pd.DataFrame, candidatas: list[str]) -> str:
    mapa = {col.strip().lower(): col for col in df.columns}
    for cand in candidatas:
        if cand.lower() in mapa:
            return mapa[cand.lower()]
    raise KeyError(f"Nenhuma das colunas {candidatas} encontrada em {list(df.columns)}")


def obter_latitude(df_municipios: pd.DataFrame, municipio: str) -> float:
    col_mun = _detectar_coluna(df_municipios, ["municipio", "nome", "cidade"])
    col_lat = _detectar_coluna(df_municipios, ["latitude", "lat"])

    normalizado = (
        df_municipios[col_mun]
        .astype(str)
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    filtro = normalizado == municipio.lower()
    if not filtro.any():
        raise ValueError(f"Município não encontrado em municipios.csv: {municipio}")
    return float(df_municipios.loc[filtro, col_lat].iloc[0])


def processar_municipio(
    municipio: str,
    dados_dir: Path,
    resultados_dir: Path,
    df_municipios: pd.DataFrame,
) -> None:
    lat_graus = obter_latitude(df_municipios, municipio)
    caminho_clima = dados_dir / f"clima_{municipio}.csv"
    df_clima = pd.read_csv(caminho_clima)

    col_data = _detectar_coluna(df_clima, ["data", "date"])
    col_tmax = _detectar_coluna(df_clima, ["tmax", "temperatura_maxima", "temp_max"])
    col_tmin = _detectar_coluna(df_clima, ["tmin", "temperatura_minima", "temp_min"])
    col_tmed = _detectar_coluna(df_clima, ["tmedia", "tmean", "temperatura_media", "temp_med"])

    linhas_saida = []
    for row in df_clima.itertuples(index=False):
        data_bruta = getattr(row, col_data)
        j = dia_do_ano(date.fromisoformat(str(data_bruta)[:10]))
        ra_mm = mj_para_mm(radiacao_extraterrestre(lat_graus, j))
        et0_hs = et0_hargreaves(
            tmax=float(getattr(row, col_tmax)),
            tmin=float(getattr(row, col_tmin)),
            tmedia=float(getattr(row, col_tmed)),
            ra_mm=ra_mm,
        )
        linhas_saida.append(
            {
                "data": data_bruta,
                "ra_mm": round(ra_mm, 4),
                "et0_hs": round(et0_hs, 4),
            }
        )

    df_out = pd.DataFrame(linhas_saida, columns=["data", "ra_mm", "et0_hs"])
    resultados_dir.mkdir(parents=True, exist_ok=True)
    caminho_out = resultados_dir / f"et0_{municipio}.csv"
    df_out.to_csv(caminho_out, index=False)

    datas_dt = pd.to_datetime(df_out["data"])
    df_out["ano"] = datas_dt.dt.year
    media_diaria = df_out["et0_hs"].mean()
    total_medio_anual = df_out.groupby("ano")["et0_hs"].sum().mean()

    print(
        f"[{municipio}] Linhas: {len(df_out)} | "
        f"ET0 média diária: {media_diaria:.2f} mm/dia | "
        f"ET0 total médio anual: {total_medio_anual:.1f} mm/ano"
    )


def main() -> None:
    base_dir = Path(__file__).resolve().parent
    dados_dir = base_dir / "dados"
    resultados_dir = base_dir / "resultados"
    df_municipios = pd.read_csv(dados_dir / "municipios.csv")

    for municipio in MUNICIPIOS:
        processar_municipio(municipio, dados_dir, resultados_dir, df_municipios)


if __name__ == "__main__":
    main()