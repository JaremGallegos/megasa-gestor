Feature: Registrar Ideas de Anuncios
  Como Personal Creativo,
  Quiero ingresar y almacenar ideas o notas conceptuales sobre anuncios
  Para que dichas propuestas puedan ser consultadas y evaluadas posteriormente.

  Scenario: Registrar una idea para un anuncio
    Given el Personal Creativo está en la pantalla de registro de ideas
    When ingresa la "descripción" de la idea y la "fecha" de registro
    And confirma el registro de la idea
    Then el sistema asigna un ID autogenerado a la idea
    And almacena la idea para su consulta futura
