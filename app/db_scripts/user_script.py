from .BD.base_manager import DBManager

class UserDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
        self.id = int
        self.fio = str
        self.phone = int
        self.addres = str
        self.email = str
        self.post_id = int
        
    def check_user(self, login, password):
        req = self.execute("SELECT id, fio, phone, addres, email, post_id "
                        "FROM users "
                        "WHERE login= ? AND password = ? ", 
                        args=(login, password, ), many=False)
        
        if req['code'] == 200:
            self.id = req['data'][0]
            self.fio = req['data'][1]
            self.phone = req['data'][2]
            self.addres = req['data'][3]
            self.email = req['data'][4]
            self.post_id = req['data'][5]
            
        return req
    
    def create_user(self, fio, phone, addres, email, login, password, post_id=2):
        req = self.execute("INSERT INTO users(fio, phone, addres, email, login, password, post_id) "
                        "VALUES (?, ?, ?, ?, ?, ?, ?) ", 
                        args=(fio, phone, addres, email, login, password, post_id, ), many=False)
        
        return req
    
    def get_user(self, user_id):
        req = self.execute("SELECT id, fio, phone, addres, email, post_id "
                        "FROM users "
                        "WHERE id= ? ", 
                        args=(user_id, ), many=False)
        
        if req['code'] == 200:
            resp = {
                'code': 200,
                'data':{
                    'id': req['data'][0],
                    'fio': req['data'][1],
                    'phone': req['data'][2],
                    'addres': req['data'][3],
                    'email': req['data'][4],
                    'post_id': req['data'][5]
                }
            }
            
            return resp
            
        return req
    
    def get_users(self):
        req = self.execute("SELECT id, fio, phone, addres, email, post_id "
                        "FROM users ")
            
        return req
    
    def get_post(self, post_id):
        req = self.execute("SELECT name "
                        "FROM posts "
                        "WHERE id= ? ", 
                        args=(post_id, ), many=False)
        if req['code'] == 200:
            return req['data'][0]
        
        return req
        
user = UserDatabaseScripts()