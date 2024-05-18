from .BD.base_manager import DBManager

class PatientDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_patients(self):
        req = self.execute("SELECT * "
                        "FROM patients ")
            
        return req
    
    def get_patient(self, patient_id):
        req = self.execute("SELECT * "
                        "FROM patients "
                        "WHERE id= ? ", 
                        args=(patient_id, ), many=False)
        
        if req['code'] == 200:
            resp = {
                'code': 200,
                'data':{
                    'id': req['data'][0],
                    'name': req['data'][1],
                    'date_birth': req['data'][2],
                    'kind_id': req['data'][3],
                    'breed_id': req['data'][4]
                }
            }
            
            return resp
            
        return req
    
    def get_kind(self, kind_id):
        req = self.execute("SELECT name "
                        "FROM kinds "
                        "WHERE id= ? ", 
                        args=(kind_id, ), many=False)
        if req['code'] == 200:
            return req['data'][0]
        
        return req
    
    def get_breed(self, breed_id):
        req = self.execute("SELECT name "
                        "FROM breeds "
                        "WHERE id= ? ", 
                        args=(breed_id, ), many=False)
        if req['code'] == 200:
            return req['data'][0]
        
        return req
        
patient = PatientDatabaseScripts()