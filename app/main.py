
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.main_form_ui import Ui_MainWindow
from .create_patient import CreatePatient
from .create_user import CreateUserWindow
from .create_procedure import CreateProcedureWindow
from .db_scripts.patient_scripts import patient
from .db_scripts.user_script import user
from .db_scripts.procedure_scripts import procedure
from .db_scripts.order_scripts import orders


class MainWindow(QMainWindow, Ui_MainWindow):

    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Главная')
        
        self.print_all_patients()
        
        self.patients_btn.clicked.connect(self.print_all_patients)
        self.create_patients_btn.clicked.connect(self.create_patient)
        self.users_btn.clicked.connect(self.print_all_users)
        self.create_users_btn.clicked.connect(self.create_user)
        self.procedures_btn.clicked.connect(self.print_all_procedures)
        self.create_procedures_btn.clicked.connect(self.create_procedure)
        self.orders_btn.clicked.connect(self.print_all_orders)
        
    def clear_table(self):
        self.data_table.clear()
        self.data_table.setRowCount(0)
        self.data_table.setColumnCount(0)
    
    def delete_patient(self, patient_id):
        patient.delete_patient(patient_id)
        self.print_all_patients()
    
    def print_all_patients(self):
        self.clear_table()
        patients = patient.get_patients()['data']
        
        if patients:
            row = len(patients)
            col_row = 0
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(5)
            self.data_table.setHorizontalHeaderLabels(
                ['Имя', 'Дата рождения', 'Вид животного', 'Порода', '']) 
            
            for pat in patients:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(pat[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(pat[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(patient.get_kind(pat[3]))))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(patient.get_breed(pat[4]))))
                self.delte_patient_btn =  QPushButton('Удалить')
                self.delte_patient_btn.clicked.connect(lambda _, data=pat[0]: self.delete_patient(data))
                self.data_table.setCellWidget(col_row, 4, self.delte_patient_btn)
                self.data_table.resizeColumnsToContents()
                col_row += 1

    def create_patient(self):
        self.main_window = CreatePatient()
        self.main_window.show()
        
    def print_all_users(self):
        self.clear_table()
        users = user.get_users()['data']
        
        if users:
            row = len(users)
            col_row = 0
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(5)
            self.data_table.setHorizontalHeaderLabels(
                ['Имя', 'Телефон', 'Аддрес', 'Почта', 'Должность']) 
            
            for us in users:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(us[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(us[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(us[3])))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(us[4])))
                self.data_table.setItem(col_row, 4, QTableWidgetItem(str(user.get_post(us[5]))))
                col_row += 1
    
    def create_user(self):
        self.main_window = CreateUserWindow()
        self.main_window.show()
    
    def print_all_procedures(self):
        self.clear_table()
        all_procedures = procedure.get_procedures()['data']
        
        if all_procedures:
            row = len(all_procedures)
            col_row = 0
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(3)
            self.data_table.setHorizontalHeaderLabels(
                ['Название', 'Описание', 'Цена']) 
            
            for procedur in all_procedures:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(procedur[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(procedur[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(procedur[3]) + ' руб.'))
                col_row += 1
                
    def create_procedure(self):
        self.main_window = CreateProcedureWindow()
        self.main_window.show()
                
    def print_all_orders(self):
        self.clear_table()
        all_orders = orders.get_orders()['data']
        
        if all_orders:
            row = len(all_orders)
            col_row = 0
            
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(3)
            self.data_table.setHorizontalHeaderLabels(
                ['Дата', 'Заметка', 'Процедура', 'Доктор', 'Пациент']) 
            
            for order in all_orders:
                proc = procedure.get_procedure(order[3])
                usr = user.get_user(order[4])
                patien = patient.get_patient(order[5])
                
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(order[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(order[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(proc['name'])))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(usr['fio'])))
                self.data_table.setItem(col_row, 4, QTableWidgetItem(str(patien['name'])))
                col_row += 1