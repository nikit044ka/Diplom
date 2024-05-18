
from PyQt6.QtWidgets import QMainWindow
from .forms.main_form_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)