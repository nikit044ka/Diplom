from PyQt6.QtWidgets import QMainWindow
from .forms.create_patient_form_ui import Ui_CreatePatientWindow
from .db_scripts.patient_scripts import patient
from datetime import datetime



class CreatePatient(QMainWindow, Ui_CreatePatientWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Создание пациента')
        
        self.kinds = patient.get_kinds()['data']
        self.breeds = patient.get_breeds()['data']
        
        self.filling_slots()
        
        self.kindBox.currentIndexChanged.connect(self.updatee_kind_box)
        self.breedBox.currentIndexChanged.connect(self.updatee_breed_box)
        self.create_btn.clicked.connect(self.create_patient)
        self.cancel_btn.clicked.connect(self.close)
    
    def get_correct_data(self):
        date = self.date_birth.date().getDate()
        date_birth = f'{date[0]}-{date[1]}-{date[2]}'
        return date_birth
    
    def create_patient(self):
        if self.breedBox.currentText() == 'Порода':
            return
        
        name = self.name_line.text()
        date_birth = self.get_correct_data()
        breed = next((breed for breed in self.breeds if breed[1] == self.breedBox.currentText()), None)
        kind = breed[2]
        
        if name and date_birth and breed and kind:
            print(patient.create_patient(name, date_birth, kind, breed[0]))
            self.close()
        
    
    def filling_slots(self):
        self.date_birth.setDate(datetime.now().date())
        self.date_birth.setCalendarPopup(True)
        self.date_birth.setMaximumDate(datetime.now().date())
        
        self.kindBox.addItem('Вид')
        for kind in self.kinds:
            self.kindBox.addItem(str(kind[1]))
        
        self.breedBox.addItem('Порода')
        for breed in self.breeds:
            self.breedBox.addItem(str(breed[1]))

    def updatee_kind_box(self):
        self.breedBox.clear()
        for item in self.kinds:
            if self.kindBox.currentText() == item[1]:
                self.breedBox.addItem('Порода')
                for breed in self.breeds:
                    if breed[2] == item[0]:
                        self.breedBox.addItem(str(breed[1]))
            elif self.kindBox.currentText() == 'Вид':
                self.breedBox.clear()
                self.breedBox.addItem('Порода')
                for breed in self.breeds:
                    self.breedBox.addItem(str(breed[1]))
    
    def updatee_breed_box(self):
        for item in self.breeds:
            if self.breedBox.currentText() == item[1]:
                for i in self.kinds:
                    if item[2] == i[0]:
                        self.kindBox.setCurrentIndex(i[0])