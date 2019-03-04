class User:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def get_name(self):
        return self._name

    def get_email(self):
        return self._email

    def do_something(self):
        pass

    def __str__(self):
        return self._name + " ," + self._email


users = [User("Anish", "anish@gmail.com"), User("george", "george@gmail.com")]

for user in users:
    print(user.__str__())

user = User("tets","dfdfdf")
print(user.__str__())
