from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from .forms.main_window import Ui_MainWindow
from .db_scripts.event_scripts import events


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.get_all_events()

    def get_all_events(self):
        row = 0
        evnts = events.get_all_events()["data"]
        for evnt in evnts:
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(evnt[1])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(str(evnt[3])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(str(evnt[4])))
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.horizontalHeader().setStretchLastSection(True)
            row += 0
