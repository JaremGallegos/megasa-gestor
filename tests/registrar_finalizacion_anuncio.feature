Feature: Registrar Finalización de Anuncio
  Como Director de Campaña o Contacto de Personal,
  Quiero marcar la finalización de un anuncio
  Para actualizar su estado y generar información para el control de la campaña.

  Scenario: Finalizar un anuncio en preparación
    Given existe un anuncio con estado "En preparación" asociado a una campaña
    When el usuario selecciona la opción de finalizar el anuncio
    And confirma la acción
    Then el sistema actualiza el estado del anuncio a "Finalizado"
