from behave import *
from calculadora import *

@given('{numero1} y {numero2} para concatenar')
def implemetacion(context, numero1, numero2):
    context.calculadora = Calculadora()
    context.valor1 = numero1
    context.valor2 = numero2

@when('la calculadora concatena los numeros')
def implementacion(context):
    context.total = context.calculadora.concatenar(context.valor1, context.valor2)

@then('el {valor} concatenado es correcto')
def implementacion(context, valor):
    assert context.total == valor