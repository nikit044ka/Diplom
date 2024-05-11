from .BD.base_manager import base_manager as db

class Doctors:
    
    id = int
    name = str
    
    """Создание пользователя (для создания доктора, но я поздно понял что это не надо)"""
    def create_doco(self, name, password):
        res = db.execute("INSERT INTO users(name, password) "
                        "VALUES (?, ?) ", 
                        args=(name, password, ), many=False)
        
        last = db.execute("SELECT id, name "
                          "FROM users "
                          "WHERE id= ? ", args=(res['lastrowid'], ), many=False)
        return {'code': res['code'], 'data': last['data']}


    def check_doco(self, name, password):
        """Проверка пользователя"""
        res = db.execute("SELECT id, name "
                        "FROM users "
                        "WHERE password= ? AND name = ? ", 
                        args=(password, name, ), many=False)    
        return res


    def delete_doco(self, id):
        """Удаление доктора"""
        res = db.execute("DELETE FROM users WHERE id = ?", 
                        args=(id, ))
        return res['code']
        
    def activ_user(self, id, name):
        self.id = int(id)
        self.name = name


docors = Doctors()
