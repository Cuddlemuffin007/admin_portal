class User:

    def __init__(self, username=None, password=None):
        self.username = username if username else input("Enter username:\n>> ")
        self.password = password if password else input("Enter password:\n>> ")

    def login(self, db_reader):
        return db_reader.validate_user(self.username, self.password)

    def logout(self):
        return False

    def create_new_user(self):
        new_user_username = input("Username: ")
        new_user_password = input("Password: ")
        new_user_full_name = input("Full name: ")
        return "{},{},{}".format(new_user_username, new_user_password, new_user_full_name)
