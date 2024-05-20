from PyQt6.QtWidgets import QMainWindow
from .forms.create_order_form_ui import Ui_CreateOrderWindow
from .db_scripts.patient_scripts import patient
from .db_scripts.user_script import user
from .db_scripts.procedure_scripts import procedure
from .db_scripts.order_scripts import orders
from datetime import datetime


class CreateOrderWindow(QMainWindow, Ui_CreateOrderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание заказа')
        
        self.procedure_list = procedure.get_procedures()
        self.patient_list = patient.get_patients()
        
        self.data_label.setText(f'Дата: {datetime.now().date()}')
        self.user_label.setText(f'Врвч: {user.fio}')
        self.filling_slots()
        
        self.procedureBox.currentIndexChanged.connect(self.get_price)
        self.create_btn.clicked.connect(self.create_procedure)
        self.cancel_btn.clicked.connect(self.close)
        
    def filling_slots(self):
        if self.procedure_list['code'] == 200:
            for procedure in self.procedure_list['data']:
                self.procedureBox.addItem(f'{procedure[1]}')
           
        if self.patient_list['code'] == 200:
            for patient in self.patient_list['data']:
                self.patientBox.addItem(f'{patient[1]}')
    
    def get_price(self):
        for procedure in self.procedure_list['data']:
            if self.procedureBox.currentText() == procedure[1]:
                self.price_label.setText(f'Цена: {procedure[3]} руб.')
    
    def create_procedure(self):
        data = datetime.now().date()
        comment = self.comment_plain_text.toPlainText()
        user_id = user.id
        
        for procedure in self.procedure_list['data']:
            if self.procedureBox.currentText() == procedure[1]:
                procedure_id = procedure[0]
                
        for patient in self.patient_list['data']:
            if self.patientBox.currentText() == patient[1]:
                patient_id = patient[0]
                
        if data and comment and procedure_id and user_id and patient_id:
            orders.create_order(data, comment, procedure_id, user_id, patient_id)
            self.close()