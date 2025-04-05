Feature: Registrar Empleado de Contacto para Campaña
  Como Director de Campaña,
  Quiero designar un empleado como punto de contacto principal con el cliente
  Para facilitar la comunicación y el seguimiento de la campaña.

  Scenario: Registrar un empleado de contacto
    Given existe una campaña en ejecución
    And hay empleados asignados a la campaña
    When el Director de Campaña selecciona un empleado para ser el contacto
    And confirma la designación
    Then el sistema asigna el rol de "Contacto de Personal" al empleado seleccionado
