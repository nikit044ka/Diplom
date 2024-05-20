from PyQt6.QtWidgets import QApplication
import sys
from app.login import Login
from app.create_patient import CreatePatient


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()