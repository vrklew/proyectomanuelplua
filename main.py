from datetime import datetime

# 1. CLASE BASE: Persona (Herencia)
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

# 2. CLASE ESTUDIANTE: Hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, dni, matricula):
        super().__init__(nombre, dni)
        self.matricula = matricula
        self.cursos_inscritos = []
        self.creditos_totales = 0

# 3. CLASE PROFESOR: Hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, dni, departamento):
        super().__init__(nombre, dni)
        self.departamento = departamento

# 4. CLASE ASIGNATURA (Entidad)
class Asignatura:
    def __init__(self, nombre_curso, creditos, cupos):
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.cupos_disponibles = cupos

# 5. CLASE TRANSACCIONAL: Inscripcion
class Inscripcion:
    def __init__(self, estudiante, asignatura, profesor):
        self.fecha = datetime.now()
        self.estudiante = estudiante
        self.asignatura = asignatura
        self.profesor = profesor

    def procesar_registro(self):
        # Lógica Transaccional
        if self.asignatura.cupos_disponibles > 0:
            # 1. Reducir cupo de la materia
            self.asignatura.cupos_disponibles -= 1
            
            # 2. Actualizar datos del estudiante
            self.estudiante.cursos_inscritos.append(self.asignatura.nombre_curso)
            self.estudiante.creditos_totales += self.asignatura.creditos
            
            return True, "Inscripción exitosa"
        else:
            return False, "Error: No hay cupos disponibles"

# 6. CLASE DE CONTROL: SistemaUniversitario (Maneja la lógica de consola)
class SistemaUniversitario:
    def __init__(self):
        # Datos iniciales (Mock data)
        self.alumno = Estudiante("Juan Perez", "123456", "2024-001")
        self.profe = Profesor("Dra. Martinez", "987654", "Ciencias")
        self.curso = Asignatura("Programación Python", 6, 2)

    def menu(self):
        while True:
            print(f"\n--- UNI-REGISTRY PYTHON ---")
            print(f"Estudiante: {self.alumno.nombre} | Créditos: {self.alumno.creditos_totales}")
            print("1. Consultar Materia")
            print("2. Inscribir Materia (Transacción)")
            print("3. Ver mis Cursos")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"\nCurso: {self.curso.nombre_curso}")
                print(f"Créditos: {self.curso.creditos} | Cupos: {self.curso.cupos_disponibles}")
            
            elif opcion == "2":
                # Ejecución de la transacción
                transaccion = Inscripcion(self.alumno, self.curso, self.profe)
                exito, mensaje = transaccion.procesar_registro()
                print(f"\n{mensaje}")
            
            elif opcion == "3":
                print("\nCursos inscritos:")
                if not self.alumno.cursos_inscritos:
                    print("Ninguno.")
                for c in self.alumno.cursos_inscritos:
                    print(f"- {c}")
            
            elif opcion == "4":
                print("Saliendo del sistema...")
                break
            else:
                print("Opción no válida.")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    sistema = SistemaUniversitario()
    sistema.menu()