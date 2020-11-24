from behave import *
from calculadora import *

@given('{base:d} y {exponente:d} para calcular la potencia')
def step_implement(context, base, exponente):
    context.calculadora = Calculadora()
    context.base = base
    context.exponente = exponente

@when('la calculadora realiza la potencia')
def stem_implement(context):
    context.total = context.calculadora.elevar(context.base, context.exponente)

@then('el {valor:d} es correcto')
def step_implement(context, valor):
    assert (context.total == valor)