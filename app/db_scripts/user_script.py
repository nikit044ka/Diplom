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
        
        
user = UserDatabaseScripts()