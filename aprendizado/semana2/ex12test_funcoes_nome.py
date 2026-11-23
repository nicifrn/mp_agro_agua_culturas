import pytest
from ex12test_funcoes_nome import amplitude, classificar_dia, graus_para_radianos


def test_amplitude():
    assert amplitude(33, 22) == pytest.approx(11.0)


def test_classificar_dia_chuvoso_e_seco():
    assert classificar_dia(8.62) == "chuvoso"
    assert classificar_dia(0.5) == "seco"


def test_classificar_dia_exatamente_1mm():
    assert classificar_dia(1.0) == "chuvoso"


def test_graus_para_radianos_norte():
    assert graus_para_radianos(13 + 44 / 60) == pytest.approx(0.240, abs=0.001)


def test_graus_para_radianos_sul():
    sul_decimal = -(22 + 54 / 60)
    assert graus_para_radianos(sul_decimal) == pytest.approx(-0.400, abs=0.001)