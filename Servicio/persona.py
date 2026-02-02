from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox

from Datos.personaDAO import PersonaDAO
from Dominio.persona import Persona
from UI.vtnPrincipal import Ui_vtnPrincipal
import re

class PersonaServicio(QMainWindow):
    '''
    Clase que genera la logica de los objetos persona
    '''
    def __init__(self):
        super(PersonaServicio, self).__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnlimpiar.clicked.connect(self.limpiar)
        self.ui.txtBuscarXcedula.setValidator(QIntValidator())

    def guardar(self):
        #recolección de datos del formulario
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtcedula.text()
        sexo = self.ui.cbsexo.currentText()
        email = self.ui.txtEmail.text()
        fechanacimiento = self.ui.txtfechanacimiento.text()

        #validación de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self,'Advertencia', 'Debe ingresar el nombre')
        elif apellido == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el apellido')
        elif len(cedula) < 10:
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el cedula')
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, 'Advertencia', 'Debe seleccionar el sexo')
        elif email == "":
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el email')
        elif fechanacimiento == "":  # Validación de campo vacío para fecha
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar la fecha de nacimiento')
        else:
            persona = Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo,email=email,fechanacimiento=fechanacimiento)
            respuesta_dict = PersonaDAO.insertar_persona(persona)
            if respuesta_dict['ejecuto']:
                print(persona)
                #mostrar confirmación de que guardo
                self.ui.statusbar.showMessage('Se guardo la información', 3000)
                #borrar campos del formulario
                self.limpiar()

            else:
                QMessageBox.critical(self, 'Error', respuesta_dict['mensaje'])

    def buscar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtcedula.setText('')
        self.ui.cbsexo.setCurrentText('Seleccionar')
        self.ui.txtfechanacimiento.setText('')
        cedula = self.ui.txtBuscarXcedula.text()
        if len(cedula) < 10:
            QMessageBox.warning(self, 'Advertencia', 'Debe ingresar el cedula a buscar.')
        else:
            persona = PersonaDAO.seleccionar_persona(cedula)
            if persona:
                self.ui.txtNombre.setText(persona.nombre)
                self.ui.txtApellido.setText(persona.apellido)
                self.ui.txtcedula.setText(persona.cedula)
                self.ui.cbsexo.setCurrentText(persona.sexo)
                self.ui.txtEmail.setText(persona.email)
                self.ui.txtfechanacimiento.setText(persona.fechanacimiento)
                self.ui.statusbar.showMessage('campos limpiados', 2000)
            else:
             QMessageBox.warning(self, 'Advertencia','No existe persona registrada con'+
              'la cedula buscada.')
    def limpiar(self):
        self.ui.txtNombre.setText('')
        self.ui.txtApellido.setText('')
        self.ui.txtcedula.setText('')
        self.ui.txtEmail.setText('')
        self.ui.cbsexo.setCurrentText('seleccionar')
        self.ui.txtBuscarXcedula.setText('')
        self.ui.txtfechanacimiento.setText('')