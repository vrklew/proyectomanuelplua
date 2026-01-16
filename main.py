from datetime import datetime

# 1. CLASE BASE: Persona
class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

# 2. CLASE PROFESOR: Hereda de Persona
class Profesor(Persona):
    def __init__(self, nombre, dni, departamento):
        super().__init__(nombre, dni)
        self.departamento = departamento
        self.materias_asignadas = []

# 3. CLASE ASIGNATURA
class Asignatura:
    def __init__(self, nombre_curso, creditos, cupos):
        self.nombre_curso = nombre_curso
        self.creditos = creditos
        self.cupos_totales = cupos
        self.alumnos_inscritos = 0 # Contador de inscritos

# 4. CLASE DE CONTROL: SistemaDocente
class SistemaDocente:
    def __init__(self):
        self.profesor = None
        self.curso = None

    def configurar_perfil(self):
        print("--- REGISTRO DE PROFESOR ---")
        nombre = input("Ingresa tu nombre completo: ")
        dni = input("Ingresa tu DNI: ")
        depto = input("Departamento académico: ")
        self.profesor = Profesor(nombre, dni, depto)

        print("\n--- REGISTRO DE MATERIA A DICTAR ---")
        nom_asig = input("Nombre de la materia: ")
        cred_asig = int(input("Créditos de la materia: "))
        cupos_asig = int(input("Capacidad máxima de alumnos (cupos): "))
        self.curso = Asignatura(nom_asig, cred_asig, cupos_asig)
        
        # Guardamos la materia en el perfil del profesor
        self.profesor.materias_asignadas.append(self.curso.nombre_curso)
        print("\n¡Perfil y materia configurados correctamente!")

    def menu(self):
        if not self.profesor:
            self.configurar_perfil()

        while True:
            print(f"\n--- PANEL DOCENTE: {self.profesor.nombre} ---")
            print(f"Departamento: {self.profesor.departamento}")
            print("-" * 35)
            print("1. Ver detalles de mi materia")
            print("2. Registrar ingreso de alumno (Reducir cupo)")
            print("3. Ver resumen de carga académica")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"\nMateria: {self.curso.nombre_curso}")
                print(f"Créditos: {self.curso.creditos}")
                print(f"Cupos Totales: {self.curso.cupos_totales}")
                print(f"Lugares ocupados: {self.curso.alumnos_inscritos}")
                print(f"Lugares disponibles: {self.curso.cupos_totales - self.curso.alumnos_inscritos}")
            
            elif opcion == "2":
                # Lógica para manejar cupos
                if self.curso.alumnos_inscritos < self.curso.cupos_totales:
                    self.curso.alumnos_inscritos += 1
                    print(f"\n[OK] Alumno registrado. Cupos restantes: {self.curso.cupos_totales - self.curso.alumnos_inscritos}")
                else:
                    print("\n[ERROR] No se pueden registrar más alumnos. Cupos agotados.")
            
            elif opcion == "3":
                print(f"\nResumen para el Prof. {self.profesor.nombre}:")
                for m in self.profesor.materias_asignadas:
                    print(f"- Asignatura: {m} ({self.profesor.departamento})")
            
            elif opcion == "4":
                print("Cerrando sistema docente...")
                break
            else:
                print("Opción no válida.")

# --- EJECUCIÓN ---
if __name__ == "__main__":
    sistema = SistemaDocente()
    sistema.menu()