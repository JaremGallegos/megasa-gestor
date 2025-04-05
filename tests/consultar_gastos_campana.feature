Feature: Consultar Gastos de Campaña
  Como Director de Campaña,
  Quiero consultar un resumen de los gastos incurridos en la campaña
  Para evaluar si se están respetando los límites presupuestados.

  Scenario: Consultar resumen de gastos
    Given existe una campaña con gastos registrados
    When el Director de Campaña solicita el resumen de gastos
    Then el sistema muestra el total de gastos reales comparado con el presupuesto
