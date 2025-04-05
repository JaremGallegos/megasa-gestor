Feature: Mantener Datos Cliente
  Como usuario responsable de la información de clientes,
  Quiero ingresar, modificar y eliminar los datos de clientes,
  Para mantener un registro actualizado de cada cliente.

  Scenario: Crear un nuevo cliente
    Given el usuario se encuentra en la pantalla de registro de cliente
    When ingresa el "nombre", "dirección" y "detalle de contacto" válidos
    And confirma la creación del cliente
    Then el sistema registra el nuevo cliente exitosamente

  Scenario: Actualizar datos de un cliente existente
    Given existe un cliente registrado en el sistema
    When el usuario modifica el "nombre", "dirección" o "detalle de contacto"
    And confirma la actualización
    Then el sistema actualiza los datos del cliente correctamente

  Scenario: Eliminar un cliente
    Given existe un cliente registrado en el sistema
    When el usuario selecciona la opción de eliminar el cliente
    Then el sistema elimina el cliente y ya no se muestra en el listado