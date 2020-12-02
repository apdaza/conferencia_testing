class Calculadora():
    
    def sumar(self, valor1, valor2):
        return valor1 + valor2

    def restar(self, valor1, valor2):
        return valor1 - valor2

    def multiplicar(self, valor1, valor2):
        return valor1 * valor2
        
    def dividir(self, valor1, valor2):
        if valor2 == 0:
            return "None"
        return valor1 // valor2

    def elevar(self, base, exponente):
        return base ** exponente

    def concatenar(self, valor1, valor2):
        return valor1 + valor2