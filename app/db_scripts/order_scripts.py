from .BD.base_manager import DBManager

class OrderDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_orders(self):
        req = self.execute("SELECT * "
                        "FROM orders ")
            
        return req
        
orders = OrderDatabaseScripts()