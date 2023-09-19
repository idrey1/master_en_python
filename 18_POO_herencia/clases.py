# Herencia: es la posibilidad de compartir atributos y metodos entre clases
# Diferentes clases hereden de otras

class Persona:
   '''
   nombre
    apellidos
    altura
   '''

   def getNombre(self):
       return self.nombre

   def getApellidos(self):
       return self.apellidos

   def getAltura(self):
       return self.altura

   def getEdad(self):
       return self.edad

   def setNombre(self,nombre):
       self.nombre = nombre

   def setApellidos(self,apellidos):
        self.apellidos = apellidos

   def setAltura(self,altura):
        self.altura = altura

   def setEdad(self,edad):
        self.edad = edad

   def hablar(self):
        return 'Estoy hablando'

   def caminar(self):
        return 'Estoy caminando'

   def dormir(self):
        return 'Estoy durmiendo'


class Informatico(Persona):
    '''
    lenguajes
    experiencia
    '''

    def __init__(self):
        self.lenguajes = 'HTML,CSS,Javascript,PHP'
        self.experiencia = 5

    def getLenguajes(self):
        return self.lenguajes

    def aprender(self,lenguajes):
        self.lenguajes = lenguajes
        return self.lenguajes

    def programar(self):
        return 'Estoy programando'

    def repararPC(self):
        return 'He reparado tu ordenador'

class TecnicoRedes(Informatico):

    def __int__(self):
        super().__init__()
        self.auditarRedes ='experto'
        self.experienciaRedes = 15

    def auditoria(self):
        return 'Estoy auditando una red'