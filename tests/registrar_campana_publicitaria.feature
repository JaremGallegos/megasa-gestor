Feature: Registrar Campaña Publicitaria
  Como Director de Campaña,
  Quiero crear una nueva campaña publicitaria
  Para iniciar el seguimiento y ejecución del proyecto.

  Scenario: Registrar una campaña con datos válidos
    Given el Director de Campaña está en la pantalla de registro de campaña
    When ingresa el "título", "fecha de inicio", "fecha prevista de finalización", "costes estimados" y "presupuesto"
    And confirma el registro de la campaña
    Then el sistema asigna un ID autogenerado a la campaña
    And la campaña se registra con estado "En ejecución"
