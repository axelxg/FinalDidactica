from Estudiante import Estudiante
listaEstudiantes = []

for i in range(1):
    est1 = Estudiante()
    est1.setCarnet(int(input("Ingrese carne: ")))
    est1.setCurso(input("Ingrese curso: "))
    est1.setZona(int(input("Ingrese zona: ")))
    est1.setExamen(int(input("Ingrese Examen: ")))
    listaEstudiantes.append(est1)

for est in listaEstudiantes:
    print (est.getCarnet())
    print (est.getCurso())
    print (est.getNotaFinal())
