Feature: Consultar Ideas de Anuncios
  Como Personal Creativo u otro empleado,
  Quiero consultar las ideas o notas conceptuales registradas
  Para planificar y revisar propuestas sobre los anuncios.

  Scenario: Consultar lista de ideas de anuncios
    Given existen varias ideas registradas en el sistema
    When el usuario solicita visualizar las ideas de anuncios
    Then el sistema muestra una lista con todas las ideas, incluyendo descripción y fecha
