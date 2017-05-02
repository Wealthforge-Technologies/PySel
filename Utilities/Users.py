class Users:

    def __init__(self):
        self.lookup = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):
        self.lookup["CCO.email"] = "oquelland@wealthforge.com"
        self.lookup["CCO.password"] = "Test123!"
