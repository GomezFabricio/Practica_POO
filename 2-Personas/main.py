from persona import Persona
from alumno import Alumno
from profesor import Profesor
from coordinador import Coordinador

alumno1 = Alumno("Fabricio", "Gomez", 20, 4)
print("------------------------------------------------------------")
print(alumno1.nombreCompleto())
print(alumno1.mayorEdad())
print(alumno1.detalleMaterias())


profesor1 = Profesor("Ricardo", "Plazas", 27, 30)
print("------------------------------------------------------------")
print(profesor1.nombreCompleto())
print(profesor1.mayorEdad())
print(profesor1.detalleHorasAcumuladas())


coordinador1 = Coordinador("Javier", "Ruiz Diaz", 40, 10)
print("------------------------------------------------------------")
print(coordinador1.nombreCompleto())
print(coordinador1.mayorEdad())
print(coordinador1.detalleCantidadCursos())

