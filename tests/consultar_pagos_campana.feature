Feature: Consultar Pagos de Campaña
  Como Director de Campaña o Cliente,
  Quiero consultar el historial de pagos de una campaña
  Para verificar el cumplimiento financiero.

  Scenario: Consultar historial de pagos
    Given existe una campaña con varios pagos registrados
    When el usuario solicita ver el historial de pagos
    Then el sistema muestra una lista con los detalles de cada pago (monto y fecha de pago)
