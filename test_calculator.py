"""
Unit tests for the calculator library
"""

from calculadora import *


class TestCalculadora:

    def test_suma(self):
        calculadora = Calculadora()
        assert 4 == calculadora.sumar(2, 2)

    def test_resta(self):
        calculadora = Calculadora()
        assert 2 == calculadora.restar(4, 2)

    def test_multiplicacion(self):
        calculadora = Calculadora()
        assert 15 == calculadora.multiplicar(3, 5)

    def test_division(self):
        calculadora = Calculadora()
        assert 2 == calculadora.dividir(14, 5)

    def test_potencia(self):
        calculadora = Calculadora()
        assert  125 == calculadora.elevar(5, 3)

    def test_concatenar(self):
        calculadora = Calculadora()
        assert "13" == calculadora.concatenar("1", "3")

