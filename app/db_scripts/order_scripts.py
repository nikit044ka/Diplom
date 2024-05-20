from .BD.base_manager import DBManager

class OrderDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_orders(self):
        req = self.execute("SELECT * "
                        "FROM orders ")
            
        return req
        
    def create_order(self, data, comment, procedure_id, user_id, patient_id):
        req = self.execute("INSERT INTO orders(data, comment, procedure_id, user_id, patient_id) "
                        "VALUES (?, ?, ?, ?, ?) ", 
                        args=(data, comment, procedure_id, user_id, patient_id, ), many=False)
        
        return req
    
orders = OrderDatabaseScripts()