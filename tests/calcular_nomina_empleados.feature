Feature: Calcular Nómina de los Empleados
  Como Personal Contable,
  Quiero calcular el monto de la nómina de los empleados,
  Para emitir los pagos salariales correctamente.

  Scenario: Calcular nómina con datos actualizados
    Given existen trabajadores registrados con sus respectivas categorías laborales
    And la información de los trabajadores está actualizada
    When el Personal Contable solicita el cálculo de la nómina
    Then el sistema calcula el monto a pagar a cada trabajador basado en su sueldo base y otros parámetros
    And genera las nóminas correspondientes
