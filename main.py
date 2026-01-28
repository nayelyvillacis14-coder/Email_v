import sys
from PySide6.QtWidgets import QApplication
from src.src.persona import PersonaServicio

app = QApplication(sys.argv)
vtn_principal = PersonaServicio()
vtn_principal.show()
sys.exit(app.exec())