from Datos.conexion import Conexion
from Dominio.persona import Persona
from datetime import datetime

import pyodbc as bd

class PersonaDAO:
    _INSERT = ("INSERT INTO Persona (nombre, apellido, cedula, sexo, email, campo) "
               "VALUES (?, ?, ?, ?,?, ?)")
    _SELECT = ("SELECT idPersona, nombre, apellido, cedula, sexo, email, campo "
               "FROM Persona WHERE cedula = ?")

    @classmethod
    def insertar_persona(cls, persona):
        try:
            with Conexion.obtener_Cursor() as cursor:
                datos = (persona.nombre, persona.apellido, persona.cedula, persona.sexo,persona.email,persona.fechanacimiento)
                cursor.execute(cls._INSERT, datos)
                respuesta = cursor.rowcount
                if respuesta == 1:
                    return {'ejecuto': True, 'mensaje': 'Se guardo con exito.'}
        except bd.IntegrityError as e_bb:
            print(f'Error en la cedula: {e_bb}')
            if 'UQ_Cedula' in e_bb.__str__():
                return {'ejecuto': False, 'mensaje': 'Cedula ya existe.'}
            elif 'UQ_Email' in e_bb.__str__():
                return {'ejecuto': False, 'mensaje': 'Email ya existe.'}
        except Exception as e:
            print(f'Error general: {e}')
            print(type(e))
            return {'ejecuto': False, 'mensaje': 'Error al guardar los datos, comuncarse sistemas.'}

    @classmethod
    def seleccionar_persona(cls, cedula):
        persona = None
        try:
            with Conexion.obtener_Cursor()as cursor:
                datos = (cedula,)
                cursor.execute(cls._SELECT, datos)
                registros = cursor.fetchall()
                for registro in registros:
                    persona = Persona(nombre=registro[1], apellido=registro[2],
                                      cedula=registro[3], sexo=registro[4], email=registro[5],fechanacimiento=(registro[6]))
                return persona
        except Exception as e:
            print(f'Error general: {e}')
            print(type(e))
            return persona

if __name__ == "__main__":
    # Creamos una persona de prueba con el nuevo campo email
    p_prueba = Persona(cedula="1205701517", nombre="Roxana", apellido="Rina", sexo="Femenino", email="roxana_vida@live.com",)

    # Intentamos insertar
    resultado = PersonaDAO.insertar_persona(p_prueba)
    print(f"¿Se guardó?: {resultado['mensaje']}")

    # Intentamos buscarla para ver si aparece
    busqueda = PersonaDAO.seleccionar_persona('1234567890')
    print(f"Datos encontrados: {busqueda}")