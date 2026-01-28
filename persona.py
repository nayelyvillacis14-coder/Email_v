from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from src.UI.vtnprincipal import Ui_vtnPrincipal

class PersonaServicio(QMainWindow):
    """
    Clase que genera la lógica de los objetos persona
    """
    def __init__(self):
        super().__init__()
        self.ui = Ui_vtnPrincipal()
        self.ui.setupUi(self)

        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.txtCedula.setValidator(QIntValidator())

    def guardar(self):
        nombre = self.ui.txtNombre.text()
        apellido = self.ui.txtApellido.text()
        cedula = self.ui.txtCedula.text()
        sexo = self.ui.cbSexo.currentText()
        # validacion de los datos del formulario
        if nombre == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el nombre")
        elif apellido == "":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el apellido")
        elif len(cedula) < 10:
            QMessageBox.warning(self, "Advertencia", "Debe ingresar la cedula")
        elif sexo == "Seleccionar":
            QMessageBox.warning(self, "Advertencia", "Debe ingresar el sexo")
        else:
           # persona= Persona(cedula=cedula, nombre=nombre, apellido=apellido, sexo=sexo)
            print(nombre)
            print(apellido)
            print(cedula)
            print(sexo)

        self.ui.statusbar.showMessage('Se guardo la información', 500)

    def limpiar(self):
        self.ui.txtNombre.clear()
        self.ui.txtApellido.clear()
        self.ui.txtCedula.clear()




        #if nombre == "" or apelike == "" or cedula == "":
            #QMessageBox.warning(self, "Advertencia", "Debe de ingresar la informacion")
        #else:
            #print(nombre)
            #print(apelike)
            #print(cedula)