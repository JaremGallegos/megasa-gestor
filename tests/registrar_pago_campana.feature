Feature: Registrar Pago de Campaña
  Como Director de Campaña,
  Quiero registrar cada pago parcial realizado por un cliente
  Para mantener un seguimiento financiero de la campaña.

  Scenario: Registrar un pago parcial
    Given existe una campaña activa
    And el cliente ha realizado un pago
    When el Director de Campaña ingresa el "monto" y "fecha de pago" del pago
    And confirma el registro del pago
    Then el sistema asocia el pago a la campaña y lo almacena correctamente
