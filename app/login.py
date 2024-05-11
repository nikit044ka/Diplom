from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.login import Ui_LoginWindow
from .db_scripts.doctor_scripts import docors
from .main_form import MainWindow


class Login(QMainWindow, Ui_LoginWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.doc = docors
        self.login.clicked.connect(self.chec_user)

    def chec_user(self):
        user = self.doc.check_user(self.name_input.text(), self.pass_input.text())
        if user['code'] == 200:
            self.doc.activ_user(int(user['data'][0]), user['data'][1])
            print(self.doc.__dict__)
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
