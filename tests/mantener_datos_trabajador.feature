Feature: Mantener Datos de Trabajador
  Como Personal Contable,
  Quiero gestionar la información personal y profesional de los trabajadores,
  Para mantener una base de datos actualizada y correcta.

  Scenario: Crear o actualizar datos de un trabajador
    Given el Personal Contable está en la pantalla de gestión de trabajadores
    When ingresa o modifica los datos de un trabajador (nombre, email, categoría, etc.)
    And confirma la acción
    Then el sistema guarda o actualiza la información del trabajador correctamente

  Scenario: Eliminar un trabajador
    Given existe un registro de un trabajador
    When el Personal Contable selecciona la opción de eliminar el registro
    Then el sistema elimina el registro del trabajador
