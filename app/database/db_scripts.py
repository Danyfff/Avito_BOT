from .base_manager import DBManager


class Services(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_services(self):
        '''Получение всех услуг'''
        req = self.execute("SELECT * "
                        "FROM services ")
        
        return req
    
    def get_service(self, id):
        '''Получение одной услуги по ее id'''
        req = self.execute("SELECT * "
                        "FROM services "
                        "WHERE id = ?", 
                        args=(id, ), many=False)
        
        return req
        
    def create_service(self, url, name, last_update_time=None):
        '''Создание новой услуги'''
        
        req = self.execute("INSERT INTO services(url, name, last_update_time) "
                        "VALUES (?, ?, ?) ", 
                        args=(url, name, last_update_time, ), many=False)
        
        return req
    
    def update_service(self, id, url, name):
        '''Обновление информации о услуге'''
        
        req = self.execute("UPDATE services "
                           "SET url = ?, name = ? "
                           "WHERE id = ?", 
                        args=(url, name, id), many=False)
        
        return req
    
    def update_service_time(self, id, time):
        '''Обновление информации о услуге'''
        
        req = self.execute("UPDATE services "
                           "SET last_update_time = ? "
                           "WHERE id = ?", 
                        args=(time, id), many=False)
        
        return req
    
    def delete_service(self, id):
        '''Удаление услуги по ее id'''
        
        req = self.execute("DELETE FROM services "
                         "WHERE id = ?",
                        args=(id, ))
        
        return req
    
serv = Services()