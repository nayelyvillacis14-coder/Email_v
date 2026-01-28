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
from PySide6.QtWidgets import (QApplication, QComboBox, QFormLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_vtnPrincipal(object):
    def setupUi(self, vtnPrincipal):
        if not vtnPrincipal.objectName():
            vtnPrincipal.setObjectName(u"vtnPrincipal")
        vtnPrincipal.resize(800, 600)
        self.centralwidget = QWidget(vtnPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(100, 170, 182, 172))
        self.formLayout = QFormLayout(self.layoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.lblNombre = QLabel(self.layoutWidget)
        self.lblNombre.setObjectName(u"lblNombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.lblNombre)

        self.txtNombre = QLineEdit(self.layoutWidget)
        self.txtNombre.setObjectName(u"txtNombre")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.txtNombre)

        self.lblApellido = QLabel(self.layoutWidget)
        self.lblApellido.setObjectName(u"lblApellido")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lblApellido)

        self.txtApellido = QLineEdit(self.layoutWidget)
        self.txtApellido.setObjectName(u"txtApellido")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.txtApellido)

        self.lblCedula = QLabel(self.layoutWidget)
        self.lblCedula.setObjectName(u"lblCedula")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lblCedula)

        self.txtCedula = QLineEdit(self.layoutWidget)
        self.txtCedula.setObjectName(u"txtCedula")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.txtCedula)

        self.btnLimpiar = QPushButton(self.layoutWidget)
        self.btnLimpiar.setObjectName(u"btnLimpiar")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.FieldRole, self.btnLimpiar)

        self.btnGuardar = QPushButton(self.layoutWidget)
        self.btnGuardar.setObjectName(u"btnGuardar")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.btnGuardar)

        self.lblSexo = QLabel(self.layoutWidget)
        self.lblSexo.setObjectName(u"lblSexo")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lblSexo)

        self.cbSexo = QComboBox(self.layoutWidget)
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.addItem("")
        self.cbSexo.setObjectName(u"cbSexo")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.cbSexo)

        vtnPrincipal.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(vtnPrincipal)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 21))
        vtnPrincipal.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(vtnPrincipal)
        self.statusbar.setObjectName(u"statusbar")
        vtnPrincipal.setStatusBar(self.statusbar)

        self.retranslateUi(vtnPrincipal)

        QMetaObject.connectSlotsByName(vtnPrincipal)
    # setupUi

    def retranslateUi(self, vtnPrincipal):
        vtnPrincipal.setWindowTitle(QCoreApplication.translate("vtnPrincipal", u"MainWindow", None))
        self.lblNombre.setText(QCoreApplication.translate("vtnPrincipal", u"Nombre:", None))
        self.lblApellido.setText(QCoreApplication.translate("vtnPrincipal", u"Apellido:", None))
        self.lblCedula.setText(QCoreApplication.translate("vtnPrincipal", u"cedula:", None))
        self.btnLimpiar.setText(QCoreApplication.translate("vtnPrincipal", u"Limpiar", None))
        self.btnGuardar.setText(QCoreApplication.translate("vtnPrincipal", u"Guardar", None))
        self.lblSexo.setText(QCoreApplication.translate("vtnPrincipal", u"Sexo:", None))
        self.cbSexo.setItemText(0, QCoreApplication.translate("vtnPrincipal", u"seleccionar", None))
        self.cbSexo.setItemText(1, QCoreApplication.translate("vtnPrincipal", u"Masculino", None))
        self.cbSexo.setItemText(2, QCoreApplication.translate("vtnPrincipal", u"Femenino", None))

    # retranslateUi

