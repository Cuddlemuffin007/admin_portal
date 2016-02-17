class DBReaderException(Exception):
    pass

class DBReader:

    def __init__(self, file_contents=[]):
        file_contents = self.read_file() if not file_contents else file_contents
        self.cleaned_data = self.clean_file(file_contents)

    def read_file(self):
        with open("admin_portal_db") as infile:
            data = infile.readlines()
            return data

    @staticmethod
    def clean_file(file_contents):
        return [line.split(",") for line in file_contents]

    def get_by_name(self, name):
        results = self.filter_by_name(name)
        if len(results) > 1:
            raise DBReaderException("Found more than one record for {}".format(name))
        elif len(results) == 0:
            raise DBReaderException("No records found for {}".format(name))
        else:
            return results[0]

    def filter_by_name(self, name):
        return [line for line in self.cleaned_data if line[0].lower() == name.lower()]