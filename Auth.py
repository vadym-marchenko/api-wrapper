class Auth:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self):
        if self.username == 'admin' and self.password == 'admin':
            return True