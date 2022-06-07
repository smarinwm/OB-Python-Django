class Alumno:
    nombre = ""
    nota = 0

    def nombre(self, nombre):
        self.nombre = nombre

    def nota(self, nota):
        self.nota = nota


def isAprobado(nota):
    return True if nota >= 5 else False


def datosAlumno(alumno):
    aprobado = "esta aprobado." if isAprobado(alumno.nota) else "esta suspendido."
    print("El alumno", alumno.nombre, "con una nota de", alumno.nota, aprobado)


alumno = Alumno()
alumno.nombre = "Antonio"
alumno.nota = 7.5

datosAlumno(alumno)
