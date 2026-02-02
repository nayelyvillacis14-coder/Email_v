# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'vtnPrincipal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(753, 579)
        font = QFont()
        font.setPointSize(8)
        vtnPrincipal.setFont(font)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnGuardar = QPushButton(self.centralwidget)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(280, 460, 101, 41))
        self.btnGuardar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnlimpiar = QPushButton(self.centralwidget)
        self.btnlimpiar.setObjectName(u"btnlimpiar")
        self.btnlimpiar.setGeometry(QRect(430, 460, 101, 41))
        self.btnlimpiar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnBuscar = QPushButton(self.centralwidget)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(590, 40, 101, 41))
        self.btnBuscar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.txtNombre = QLineEdit(self.centralwidget)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(270, 100, 301, 31))
        self.txtNombre.setMaxLength(50)
        self.cbsexo = QComboBox(self.centralwidget)
        self.cbsexo.addItem("")
        self.cbsexo.addItem("")
        self.cbsexo.addItem("")
        self.cbsexo.setObjectName(u"cbsexo")
        self.cbsexo.setGeometry(QRect(270, 350, 131, 31))
        self.txtApellido = QLineEdit(self.centralwidget)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(270, 150, 301, 31))
        self.txtcedula = QLineEdit(self.centralwidget)
        self.txtcedula.setObjectName(u"txtcedula")
        self.txtcedula.setGeometry(QRect(270, 200, 301, 31))
        self.txtcedula.setMaxLength(10)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(270, 250, 301, 31))
        self.txtfechanacimiento = QLineEdit(self.centralwidget)
        self.txtfechanacimiento.setObjectName(u"txtfechanacimiento")
        self.txtfechanacimiento.setGeometry(QRect(270, 300, 301, 31))
        self.txtBuscarXcedula = QLineEdit(self.centralwidget)
        self.txtBuscarXcedula.setObjectName(u"txtBuscarXcedula")
        self.txtBuscarXcedula.setGeometry(QRect(270, 50, 301, 31))
        self.lbBuscar = QLabel(self.centralwidget)
        self.lbBuscar.setObjectName(u"lbBuscar")
        self.lbBuscar.setGeometry(QRect(90, 40, 181, 51))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.lbBuscar.setFont(font1)
        self.lbNombre = QLabel(self.centralwidget)
        self.lbNombre.setObjectName(u"lbNombre")
        self.lbNombre.setGeometry(QRect(180, 90, 91, 51))
        self.lbNombre.setFont(font1)
        self.lbApellido = QLabel(self.centralwidget)
        self.lbApellido.setObjectName(u"lbApellido")
        self.lbApellido.setGeometry(QRect(180, 140, 91, 51))
        self.lbApellido.setFont(font1)
        self.lbCedula = QLabel(self.centralwidget)
        self.lbCedula.setObjectName(u"lbCedula")
        self.lbCedula.setGeometry(QRect(190, 190, 91, 51))
        self.lbCedula.setFont(font1)
        self.lbEmail = QLabel(self.centralwidget)
        self.lbEmail.setObjectName(u"lbEmail")
        self.lbEmail.setGeometry(QRect(200, 240, 91, 51))
        self.lbEmail.setFont(font1)
        self.lbCelular = QLabel(self.centralwidget)
        self.lbCelular.setObjectName(u"lbCelular")
        self.lbCelular.setGeometry(QRect(60, 290, 211, 51))
        self.lbCelular.setFont(font1)
        self.lbSexo = QLabel(self.centralwidget)
        self.lbSexo.setObjectName(u"lbSexo")
        self.lbSexo.setGeometry(QRect(210, 340, 91, 51))
        self.lbSexo.setFont(font1)
        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 753, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        vtnPrincipal.setToolTip(QCoreApplication.translate("vtnPrincipal", u"Ingrese solo n\u00fameros", None))
#endif // QT_CONFIG(tooltip)
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"GUARDAR", None))
        self.btnlimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"LIMPIAR", None))
        self.btnBuscar.setText(QCoreApplication.translate("vtnPrincipal", u"BUSCAR", None))
        self.txtNombre.setPlaceholderText(QCoreApplication.translate("vtnPrincipal", u"Ingrese su nombre", None))
        self.cbsexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbsexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))
        self.cbsexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Prefiero no decirlo", None))

#if QT_CONFIG(tooltip)
        self.txtcedula.setToolTip(QCoreApplication.translate("vtnPrincipal", u"Ingrese solo n\u00fameros", None))
#endif // QT_CONFIG(tooltip)
        self.txtcedula.setInputMask("")
        self.txtcedula.setPlaceholderText(QCoreApplication.translate("vtnPrincipal", u"0991234567", None))
        self.txtEmail.setPlaceholderText(QCoreApplication.translate("vtnPrincipal", u"nombre@ejemplo.com", None))
        self.lbBuscar.setText(QCoreApplication.translate("vtnPrincipal", u"Buscar por cedula:", None))
        self.lbNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lbApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.lbCedula.setText(QCoreApplication.translate("vtnPrincipal", u"Cedula:", None))
        self.lbEmail.setText(QCoreApplication.translate("vtnPrincipal", u"Email:", None))
        self.lbCelular.setText(QCoreApplication.translate("vtnPrincipal", u"Fecha de nacimiento:", None))
        self.lbSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
    # retranslateUi

