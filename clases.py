class Curso:
    def __init__(self, id_curso, nombre, creditos, anos_de_estudio):
        self.id_curso = id_curso
        self.nombre = nombre
        self.creditos = creditos
        self.anos_de_estudio = anos_de_estudio

    def mostrar_ficha_curso(self):
        print(f"Ficha del curso {self.nombre}:")
        print(f"ID: {self.id_curso}")
        print(f"Créditos: {self.creditos}")
        print(f"Años de estudio: {self.anos_de_estudio}")
        print()

class Alumno:
    def __init__(self, id_alumno, nombre, email):
        self.id_alumno = id_alumno
        self.nombre = nombre
        self.email = email

    def mostrar_ficha_alumno(self):
        print(f"Ficha del alumno {self.nombre}:")
        print(f"ID: {self.id_alumno}")
        print(f"Email: {self.email}")
        print()

class Matricula:
    def __init__(self, id_matricula, fecha_matricula, id_alumno, id_curso):
        self.id_matricula = id_matricula
        self.fecha_matricula = fecha_matricula
        self.id_alumno = id_alumno
        self.id_curso = id_curso

    def mostrar_datos_matricula(self):
        print(f"Datos de matrícula (ID: {self.id_matricula}):")
        print(f"Fecha de matrícula: {self.fecha_matricula}")
        print(f"ID del alumno: {self.id_alumno}")
        print(f"ID del curso: {self.id_curso}")
        print()

curso1 = Curso(1, "Matemáticas", 4, 2)
alumno1 = Alumno(1, "Juan Pérez", "juan@campus.es")
matricula1 = Matricula(101, "01-01-2023", alumno1.id_alumno, curso1.id_curso)

curso2 = Curso(2, "Programación", 3, 3)
alumno2 = Alumno(2, "Ana García", "ana@campus.es")
matricula2 = Matricula(102, "02-01-2023", alumno2.id_alumno, curso2.id_curso)
matricula3 = Matricula(103, "03-01-2023", alumno2.id_alumno, curso1.id_curso)

# Mostrar ficha del curso y del alumno
curso1.mostrar_ficha_curso()
alumno1.mostrar_ficha_alumno()

# Alumno1 se matricula en un curso
matricula1.mostrar_datos_matricula()

# Alumno2 se matricula en dos cursos
matricula2.mostrar_datos_matricula()
matricula3.mostrar_datos_matricula()

# Reto: Mostrar todas las matrículas realizadas en el centro
def mostrar_todas_matriculas(matriculas):
    print("Matrículas realizadas en el centro:\n")
    for matricula in matriculas:
        matricula.mostrar_datos_matricula()

# Lista de todas las matrículas
todas_matriculas = [matricula1, matricula2, matricula3]
mostrar_todas_matriculas(todas_matriculas)
