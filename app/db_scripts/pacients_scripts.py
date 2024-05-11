from BD.base_manager import base_manager as db


class Pacients:
    """Создание пациента"""

    def create_pacient(self, name, surname, patrony, passport, meeting, gender, address, num_telefone, email, num_card,
                       num_polis, data_meeting, data_last, data_next, data_stop_polis):
        res = db.execute(
            "INSERT INTO patients (name, surname, patrony, passport, meeting, gender, adress, num_telefone, email, num_card, num_polis, data_meeting, data_last, data_next, data_stop_polis) "
            "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ",
            args=(name, surname, patrony, passport, meeting, gender, address, num_telefone, email, num_card, num_polis,
                  data_meeting, data_last, data_next, data_stop_polis,))
        return res
