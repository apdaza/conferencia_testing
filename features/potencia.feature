Feature: potencia calculdora
    Como usuario
    Ingreso un numero y un exponente
    Obtengo el valor de la potencia

    Scenario Outline: potencia
    Given <base> y <exponente> para calcular la potencia
    When la calculadora realiza la potencia
    Then el <valor> es correcto

    Examples:
        | base | exponente | valor |
        | 5    | 1         | 5     | 
        | 3    | 0         | 1     |
        | 5    | 3         | 125   |