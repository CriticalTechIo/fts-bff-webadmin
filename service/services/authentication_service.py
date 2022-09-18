
class AuthenticationService():
    def __init__(self, db, logger):
        self.db = db
        self.logger = logger

    def authenticate(self, email, password)->User:
