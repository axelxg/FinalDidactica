from Persona import Persona
class Estudiante(Persona):
    #atributos
    carnet = 0
    curso = ""
    zona = 0
    examen = 0

    #metodos setter y getter 
    def getCarnet(self):
        return self.carnet
    def setCarnet(self, carnet):
        self.carnet = carnet

    def getCurso(self):
        return self.curso
    def setCurso(self, curso):
        self.curso = curso
    
    def getZona(self):
        return self.zona
    def setZona(self, zona):
        self.zona = zona

    def getExamen(self):
        return self.examen
    def setExamen(self, examen):
        self.examen = examen

    def getNotaFinal(self):
        return self.examen + self.zona
