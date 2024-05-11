from PyQt6.QtWidgets import QMainWindow
from forms.form_create_user import Ui_Dialog


class CreatePacient(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
