from PyQt6.QtWidgets import QMainWindow
from .forms.create_user_form_ui import Ui_CreateUserWindow
from .db_scripts.user_script import user


class CreateUserWindow(QMainWindow, Ui_CreateUserWindow):

    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание пользователя')
        
        self.create_btn.clicked.connect(self.create_user)
        self.cancel_btn.clicked.connect(self.close)
        
    def create_user(self):
        name = self.name_line.text()
        phone = self.phone_line.text()
        email = self.email_line.text()
        adres = self.adres_line.text()
        login = self.login_line.text()
        password = self.password_line.text()
        
        if name and phone and email and adres and login and password:
            user.create_user(name, phone, adres, email, login, password)
            self.close()