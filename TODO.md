### UC1: Mantener Datos Cliente
    - Permite ingresar, modificar y eliminar la información de los clientes.
    - Precondición: El usuario (Director de Campaña) debe estar autenticado.
    - Flujo Principal: Seleccionar la acción (agregar, modificar, eliminar) y confirmar la operación.
    - Requerimientos: La transacción debe ser atómica y registrar la operación para auditoría.

### UC2: Registrar Campaña Publicitaria
    - Permite crear una nueva campaña ingresando título, fechas, costes estimados, presupuesto, etc.
    - Precondición: Director de Campaña autenticado y con permisos.
    - Requerimientos: La información debe almacenarse de forma consistente.

### UC3: Registrar Finalización de Campaña
    - Permite marcar la campaña como finalizada y registrar la fecha de cierre.
    - Precondición: La campaña debe estar en estado “En ejecución”.
    - Requerimientos: Debe existir trazabilidad para auditoría.

### UC4: Registrar Pago de Campaña
    - Permite registrar un pago parcial asociado a la campaña.
    - Precondición: La campaña debe estar activa.
    - Requerimientos: La transacción debe ser segura y auditable.

### UC5: Consultar Pagos de Campaña
    - Permite recuperar el historial de pagos de una campaña.
    - Precondición: Debe existir al menos un pago registrado.
    - Requerimientos: La información debe actualizarse en tiempo real.

### UC6: Asignar Empleados a Campaña
    - Permite asignar empleados a una campaña definiendo sus roles.
    - Precondición: La campaña debe estar registrada y en ejecución.
    - Requerimientos: Se debe llevar registro de los cambios para auditoría.

### UC7: Registrar Empleado de Contacto para Campaña
    - Permite designar a un empleado como contacto principal en la campaña.
    - Precondición: Debe existir una campaña activa y empleados asignados.
    - Requerimientos: La designación debe reflejarse de forma inmediata.

### UC8: Registrar Anuncio de Campaña
    - Permite ingresar los datos de un anuncio asociado a la campaña.
    - Precondición: La campaña debe estar activa.
    - Requerimientos: El registro debe permitir la actualización posterior.

### UC9: Registrar Finalización de Anuncio
    - Permite marcar un anuncio como finalizado.
    - Precondición: El anuncio debe estar en curso.
    - Requerimientos: La operación debe generar registros para auditoría.

### UC10: Registrar Gastos de Campaña
    - Permite ingresar y actualizar los gastos reales de la campaña.
    - Precondición: La campaña debe estar en ejecución y tener presupuesto definido.
    - Requerimientos: La operación debe ser reversible en caso de errores.

### UC11: Consultar Gastos de Campaña
    - Permite visualizar un resumen de los gastos de la campaña.
    - Precondición: Debe existir registro de gastos.
    - Requerimientos: La consulta debe actualizarse en tiempo real.

### UC12: Registrar Ideas de Anuncios
    - Permite al Personal Creativo ingresar ideas o notas conceptuales para los anuncios.
    - Precondición: Usuario autenticado con permisos de Personal Creativo.
    - Requerimientos: Debe permitirse la edición o eliminación posterior.

### UC13: Consultar Ideas de Anuncios
    - Permite visualizar las ideas y notas conceptuales registradas.
    - Precondición: Debe existir al menos una idea registrada.
    - Requerimientos: La consulta debe permitir filtrar o buscar.

### UC14: Mantener Datos de Trabajador
    - Permite gestionar (alta, modificación, eliminación) los datos de los trabajadores.
    - Precondición: Contable autenticado.
    - Requerimientos: Debe existir registro histórico de cambios.

### UC15: Mantener Categoría Laboral
    - Permite crear, modificar o eliminar categorías laborales.
    - Precondición: Contable con permisos.
    - Requerimientos: Los cambios deben reflejarse inmediatamente.

### UC16: Calcular Nómina de los Empleados
    - Permite calcular el monto a pagar a cada trabajador según su categoría laboral.
    - Precondición: Datos de trabajadores y categorías actualizados.
    - Requerimientos: El cálculo debe ser preciso y exportable.