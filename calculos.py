from datetime import date
import math

G_SC = 0.0820  # Constante solar em MJ m^-2 min^-1 (FAO-56)


def graus_para_radianos(graus: float) -> float:
    """Converte um ângulo em graus para radianos (FAO-56, eq. 22)."""
    return graus * (math.pi / 180.0)


def dia_do_ano(data: date) -> int:
    """Retorna o dia do ano (J: 1 a 365/366) a partir de um datetime.date."""
    return data.timetuple().tm_yday


def distancia_relativa(j: int) -> float:
    """Calcula a distância relativa inversa Terra-Sol (dr, FAO-56, eq. 23)."""
    return 1.0 + 0.033 * math.cos((2.0 * math.pi / 365.0) * j)


def declinacao_solar(j: int) -> float:
    """Calcula a declinação solar em radianos (delta, FAO-56, eq. 24)."""
    return 0.409 * math.sin((2.0 * math.pi / 365.0) * j - 1.39)


def angulo_por_do_sol(lat_rad: float, declinacao: float) -> float:
    """Calcula o ângulo horário do pôr do sol em radianos (ws, FAO-56, eq. 25)."""
    termo = -math.tan(lat_rad) * math.tan(declinacao)
    termo_limitado = max(-1.0, min(1.0, termo))
    return math.acos(termo_limitado)


def radiacao_extraterrestre(lat_graus: float, j: int) -> float:
    """Calcula a radiação extraterrestre Ra em MJ m^-2 dia^-1 (FAO-56, eq. 21)."""
    lat_rad = graus_para_radianos(lat_graus)
    dr = distancia_relativa(j)
    delta = declinacao_solar(j)
    ws = angulo_por_do_sol(lat_rad, delta)

    fator = (24.0 * 60.0 / math.pi) * G_SC * dr
    soma_angulos = (
        ws * math.sin(lat_rad) * math.sin(delta)
        + math.cos(lat_rad) * math.cos(delta) * math.sin(ws)
    )
    return fator * soma_angulos


def mj_para_mm(valor: float) -> float:
    """Converte radiação de MJ m^-2 dia^-1 para mm dia^-1 (FAO-56, eq. 20)."""
    return 0.408 * valor


def et0_hargreaves(tmax: float, tmin: float, tmedia: float, ra_mm: float) -> float:
    """Calcula a ET0 diária (mm/dia) pelo método de Hargreaves-Samani (FAO-56, eq. 52)."""
    if tmax < tmin:
        raise ValueError("tmax menor que tmin")
    return 0.0023 * (tmedia + 17.8) * math.sqrt(tmax - tmin) * ra_mm