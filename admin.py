from user import User


class Admin(User):

    def __init__(self, name, username, password, role):
        User.__init__(self, name, username, password, role)

    def __str__(self):
        return "Username: {}, Password: {}".format(self.username, self.password)

    __repr__ = __str__
