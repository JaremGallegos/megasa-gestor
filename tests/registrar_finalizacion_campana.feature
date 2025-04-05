Feature: Registrar Finalización de Campaña
  Como Director de Campaña,
  Quiero marcar la finalización de una campaña
  Para actualizar su estado y generar información para tareas contables.

  Scenario: Finalizar una campaña en ejecución
    Given existe una campaña con estado "En ejecución"
    When el Director de Campaña selecciona la opción de finalizar la campaña
    And confirma la acción
    Then el sistema actualiza el estado de la campaña a "Finalizada"
    And registra la fecha de finalización
