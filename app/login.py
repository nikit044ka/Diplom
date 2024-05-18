from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.login_form_ui import Ui_LoginWindow
from .db_scripts.user_script import user
from .main import MainWindow


class Login(QMainWindow, Ui_LoginWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Login')
        
        self.login.clicked.connect(self.check_user)
        
    def check_user(self):
        if user.check_user(self.name_input.text(), self.pass_input.text())['code'] == 200:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()