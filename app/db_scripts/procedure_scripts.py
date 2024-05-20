from .BD.base_manager import DBManager

class ProcedureDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_procedures(self):
        req = self.execute("SELECT * "
                        "FROM procedures ")
            
        return req
    
    def get_procedure(self, procedure_id):
        req = self.execute("SELECT * "
                        "FROM procedures "
                        "WHERE id= ? ", 
                        args=(procedure_id, ), many=False)
        
        if req['code'] == 200:
            resp = {
                'code': 200,
                'data':{
                    'id': req['data'][0],
                    'name': req['data'][1],
                    'comment': req['data'][2],
                    'price': req['data'][3]
                }
            }
            
            return resp
            
        return req
    
    def create_procedure(self, name, comment, price):
        req = self.execute("INSERT INTO procedures(name, comment, price) "
                        "VALUES (?, ?, ?) ", 
                        args=(name, comment, price, ), many=False)
        
        return req
    
    def delete_procedure(self, id_procedure):
        req = self.execute("DELETE FROM procedures "
                         "WHERE id = ?",
                        args=(id_procedure, ))
        
        return req
        
procedure = ProcedureDatabaseScripts()