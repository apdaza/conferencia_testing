Feature: concatenar calculdora
    Como usuario
    Ingreso dos numeros
    Obtengo los numeros concatenados

    Scenario Outline: concatenar
    Given <numero1> y <numero2> para concatenar
    When la calculadora concatena los numeros
    Then el <valor> concatenado es correcto

    Examples:
        | numero1 | numero2 | valor |
        | 5    | 1         | 51     | 
        | 3    | 0         | 30     |
        | 5    | 3         | 53   |