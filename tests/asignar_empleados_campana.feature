Feature: Asignar Empleados a Campaña
  Como Director de Campaña,
  Quiero asignar empleados a una campaña publicitaria
  Para formar el equipo de trabajo y definir roles en la campaña.

  Scenario: Asignar un empleado a la campaña
    Given existe una campaña en ejecución
    And hay empleados disponibles para asignar
    When el Director de Campaña selecciona uno o varios empleados
    And confirma la asignación
    Then el sistema asocia los empleados a la campaña
