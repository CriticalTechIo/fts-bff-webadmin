from uuid import UUID
from fts_webadmin_api.rest.user import RestUser

class UserService():
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def create_user(self, input_user:RestUser)->RestUser:
        pass
    
    def get_user(self, uuid: UUID)->RestUser:
        pass

    def get_users(self)->RestUser:
        pass

    def update_user(self, input_user:RestUser)->RestUser:
        pass

    def change_password(self, input_user:RestUser)->None:
        pass
    
    def toggle_active(self, uuid: UUID)->bool:
        pass
    
    def delete_user(self, uuid: UUID)->None:
        pass
    
    