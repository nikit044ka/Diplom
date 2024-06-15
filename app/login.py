from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow, QMessageBox
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
        
    def warning_window(self, titel, text):
        '''Вывод окна с предупреждением'''
        message_box = QMessageBox()
        message_box.setWindowTitle(titel)
        message_box.setText(text)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        result = message_box.exec()
        if result == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
    def check_user(self):
        if user.check_user(self.name_input.text(), self.pass_input.text())['code'] == 200:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            self.warning_window('login EROR', 'Неверный логин или пароль')