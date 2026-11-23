import math


def amplitude(tmax, tmin):
    return tmax - tmin


def classificar_dia(chuva):
    if chuva >= 1:
        return "chuvoso"
    return "seco"


def graus_para_radianos(graus):
    return graus * math.pi / 180