from .BD.base_manager import base_manager as db
from datetime import datetime

class Events:
    
    """Создание заметки"""
    def create_event(self, data_event, doctor, name_event, results):
        res = db.execute("INSERT INTO notes(name_notes, text, user_id, time_create, time_update) "
                        "VALUES (?, ?, ?, ?)",
                        args=(data_event, doctor, name_event, results, ))
        return res

        """Получение всех мероприятий"""
    def get_all_events(self):
        res = db.execute("SELECT * "
                        "FROM events ")
        return res
    
    """Удаление мероприятия"""
    def delete_event(self, id):
        res = db.execute("DELETE FROM notes "
                         "WHERE id = ?",
                        args=(id, ))    
        return res['code']
        
        
events = Events()
