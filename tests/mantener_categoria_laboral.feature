Feature: Mantener Categoría Laboral
  Como Personal Contable,
  Quiero crear y modificar categorías laborales,
  Para definir y ajustar los atributos (como el sueldo base) de cada categoría.

  Scenario: Crear una nueva categoría laboral
    Given el Personal Contable se encuentra en la pantalla de gestión de categorías laborales
    When ingresa el "nombre" y el "sueldo base" para la nueva categoría
    And confirma la creación
    Then el sistema registra la nueva categoría laboral

  Scenario: Modificar una categoría laboral existente
    Given existe una categoría laboral registrada
    When el Personal Contable modifica el "sueldo base" o el "nombre" de la categoría
    And confirma la actualización
    Then el sistema actualiza los datos de la categoría laboral
