def amplitude(tmax, tmin):
    return tmax - tmin


def media(a, b):
    return (a + b) / 2


def classificar_dia(chuva):
    if chuva >= 1:
        return "chuvoso"
    return "seco"


print("amplitude:", amplitude(33, 22))
print("media:", media(33, 22))
print("0.5:", classificar_dia(0.5))
print("8.62:", classificar_dia(8.62))