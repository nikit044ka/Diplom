# Form implementation generated from reading ui file 'app\forms\forms.ui\create_patient.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CreatePatientWindow(object):
    def setupUi(self, CreatePatientWindow):
        CreatePatientWindow.setObjectName("CreatePatientWindow")
        CreatePatientWindow.resize(336, 138)
        self.centralwidget = QtWidgets.QWidget(parent=CreatePatientWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.date_birth = QtWidgets.QDateEdit(parent=self.centralwidget)
        self.date_birth.setObjectName("date_birth")
        self.horizontalLayout_2.addWidget(self.date_birth)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kindBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.kindBox.setMinimumSize(QtCore.QSize(100, 0))
        self.kindBox.setObjectName("kindBox")
        self.horizontalLayout_3.addWidget(self.kindBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.breedBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.breedBox.setMinimumSize(QtCore.QSize(200, 0))
        self.breedBox.setObjectName("breedBox")
        self.horizontalLayout_3.addWidget(self.breedBox)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_4.addWidget(self.create_btn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.cancel_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_4.addWidget(self.cancel_btn)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        CreatePatientWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreatePatientWindow)
        QtCore.QMetaObject.connectSlotsByName(CreatePatientWindow)

    def retranslateUi(self, CreatePatientWindow):
        _translate = QtCore.QCoreApplication.translate
        CreatePatientWindow.setWindowTitle(_translate("CreatePatientWindow", "MainWindow"))
        self.label.setText(_translate("CreatePatientWindow", "Кличка:"))
        self.label_2.setText(_translate("CreatePatientWindow", "Дата рождения:"))
        self.create_btn.setText(_translate("CreatePatientWindow", "Создать"))
        self.cancel_btn.setText(_translate("CreatePatientWindow", "Отмена"))
