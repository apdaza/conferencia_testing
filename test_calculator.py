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

