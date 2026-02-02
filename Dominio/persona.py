import valor

class Persona:
    '''
    Clase que permite crear objetos de persona
    '''
    def __init__(self, cedula:str, nombre:str, apellido:str, sexo:str
                 , email:str, fechanacimiento:str):
        self._cedula = cedula
        self._nombre = nombre
        self._apellido = apellido
        self._sexo = sexo
        self._email = email
        self._fechanacimiento = fechanacimiento

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, valor):
        if not valor.isdigit():
            raise ValueError("La cédula debe contener solo números")
        self._cedula = valor

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor.strip():
            raise ValueError("El nombre no puede estar vacío")
        self._nombre = valor

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor.strip():
            raise ValueError("El apellido no puede estar vacío")
        self._apellido = valor

    @property
    def sexo(self):
        return self._sexo

    @sexo.setter
    def sexo(self, valor):
        if valor.lower() not in ["masculino", "femenino", "prefiero no decirlo"]:
            raise ValueError("El sexo debe ser 'masculino', 'femenino' o 'Prefiero no decirlo'")
        self._sexo = valor

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if valor and "@" not in valor:
            raise ValueError("El email debe contener '@'")
        self._email = valor

    @property
    def fechanacimiento(self):
        return self._fechanacimiento

    @fechanacimiento.setter
    def fechanacimiento(self, valor):
        self._fechanacimiento = valor
    # Representación en cadena
    def __str__(self):
        return (f"Persona: {self.__dict__.__str__()}")

if __name__ == "__main__":
    p1 = Persona(cedula="0123456789", nombre="Luis", apellido="Perez", sexo="Masculino", email="roxana_vida@live.com")

    print(p1)