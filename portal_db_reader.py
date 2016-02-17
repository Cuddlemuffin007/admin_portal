from A_db import DBReader, DBReaderException


class PortalDBReaderException(DBReaderException):
    pass


class PortalDBReader(DBReader):

    def read_file(self):
        with open("admin_portal_db") as infile:
            data = infile.readlines()
        return data

    def append_to_file(self, new_record):
        for line in self.cleaned_data:
            if line[0] == new_record.split(",")[0]:
                print("This username is taken!")
                return
        with open("admin_portal_db", "a") as outfile:
            outfile.write(new_record + "\n")

    def get_by_username(self, username):
        for line in self.cleaned_data:
            if line[0] == username:
                return line
        else:
            raise PortalDBReaderException

    def validate_user(self, username, password):
        try:
            line = self.get_by_username(username)
            if line[0] == username and line[1] == password:
                return True
        except PortalDBReaderException:
            pass
        print("Your username or password was incorrect.")
        return False
