class User(object):

    def __init__(self, name, username, password, role):
        self._name = name
        self._username = username
        self._password = password
        self._role = role

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, role):
        self._role = role

    def __eq__(self, other):
        return self.name == other.name and \
              self.username == other.username and \
              self.password == other.password and \
              self.role == other.role
