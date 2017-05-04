class TestInfo:

    def __init__(self):
        self.testinfo = {}

    #TODO write the json object reader to use outside data in the test cases
    def load_json(self):
        pass

    def load_defaults(self):
        self.testinfo["CCO.email"] = "oquelland@wealthforge.com"
        self.testinfo["CCO.password"] = "Test123!"
