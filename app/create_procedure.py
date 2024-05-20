from PyQt6.QtWidgets import QMainWindow
from .forms.create_procedure_form_ui import Ui_CreateProcedureWindow
from .db_scripts.procedure_scripts import procedure


class CreateProcedureWindow(QMainWindow, Ui_CreateProcedureWindow):

    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание процедуры')
        
        self.create_btn.clicked.connect(self.create_procedure)
        self.cancel_btn.clicked.connect(self.close)
        
    def create_procedure(self):
        name = self.name_line.text()
        comment = self.comment_plain_text.toPlainText()
        price = self.price_line.text()
        
        if name and comment and price:
            procedure.create_procedure(name, comment, int(price))
            self.close()