Feature: Registrar Anuncio de Campaña
  Como Director de Campaña,
  Quiero registrar un anuncio asociado a una campaña
  Para llevar un control del proceso de preparación y ejecución de anuncios.

  Scenario: Registrar un anuncio
    Given existe una campaña activa
    When el Director de Campaña ingresa la "descripción" del anuncio
    And confirma el registro del anuncio
    Then el sistema asigna un ID autogenerado al anuncio
    And lo asocia a la campaña con estado "En preparación"
