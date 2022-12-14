from empleado import Gerente
from empleado import Tecnico
from empleado import Gestora
from empleado import Administrador
from reportes import ReporteContabilidad
from reportes import ReporteEmpleados
from reportes import ReporteProgramacion
from programacion import Matutino
from programacion import Vespertino

empleados = [
    Gerente("Roberto", "Garcia", "$20,000.00", Matutino()),
    Gestora("Alejandra", "Radillo", "$8,000.00", Vespertino()),
    Gestora("Selene","Solis" ,"$8,000.00", Matutino()),
    Tecnico("Artemio","De la Cruz" , "$9,000.00", Matutino()),
    Tecnico("Salvador","Mendoza" ,"$9,000.00", Vespertino()),
    Tecnico("Rolando","Ramirez" ,"$9,000.00", Vespertino()),
    Administrador("Marco","Castillo" ,"$15,000.00", Matutino())
]

reportes = [
    ReporteContabilidad(empleados),
    ReporteEmpleados(empleados),
    ReporteProgramacion(empleados)
]

for r in reportes:
    r.print_reporte()

    
#reporteContabilidad = ReporteContabilidad(empleados)
#reporteContabilidad.reporte_contabilidad()
#reporteEmpleados = ReporteEmpleados(empleados)
#reporteEmpleados.reporte_empleados()