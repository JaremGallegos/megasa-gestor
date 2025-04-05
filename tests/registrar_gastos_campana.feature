Feature: Registrar Gastos de Campaña
  Como Director de Campaña,
  Quiero registrar los gastos reales incurridos durante la campaña
  Para comparar con el presupuesto asignado y controlar costos.

  Scenario: Registrar un gasto en la campaña
    Given existe una campaña en ejecución con un presupuesto asignado
    When el Director de Campaña ingresa un valor de gasto
    And confirma el registro del gasto
    Then el sistema suma el gasto a los "costes reales" de la campaña
