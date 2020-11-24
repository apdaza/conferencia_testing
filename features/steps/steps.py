from behave import *
from calculadora import *

@given('a {values} to sum')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calculator sums the values')
def step_impl(context):
    context.total = context.calculadora.sumar(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of sum is correct')
def step_impl(context, total):
    assert (context.total == total)

@given('a {values} to substract')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calculator substract the values')
def step_impl(context):
    context.total = context.calculadora.restar(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of substraction is correct')
def step_impl(context, total):
    assert (context.total == total)

@given('a {values} to Multiply')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calculator multiply the values')
def step_impl(context):
    context.total = context.calculadora.multiplicar(int(context.values[0]),int(context.values[1]))

@then('the {total:d} of multiply is correct')
def step_impl(context, total):
    assert (context.total == total)

@given('a {values} to Divide')
def step_impl(context, values):
    context.calculadora = Calculadora()
    context.values = values.split(',')

@when('the calculator divide the values')
def step_impl(context):
    context.total = context.calculadora.dividir(int(context.values[0]),int(context.values[1]))

@then('the {total} of divide is correct')
def step_impl(context, total):
    if total == "None":
        assert(True)
    else:
        assert (context.total == int(total))