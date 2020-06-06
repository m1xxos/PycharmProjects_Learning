class User:
    n_active = 0
    users = []

    def __init__(self, active, name):
        self.active = active
        self.user_name = name
        User.users.append(name)
        User.n_active += 1
