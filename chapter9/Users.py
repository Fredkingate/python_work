class Users:
    def __init__(self, first_name, last_name,login_attempts=0):
        #Attributes describing the user as well as the number of login attempts.
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
    def describe_user(self):
        print(f"User's name is {self.first_name} {self.last_name}.")
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0
user1 = Users('John', 'Doe')
user1.describe_user()
user1.greet_user()
user2 = Users('Pawlick', 'Bowers')
user2.describe_user()
user2.greet_user()
print(f"Login attempts for {user1.first_name} {user1.last_name}: {user1.login_attempts}")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"Login attempts for {user1.first_name} {user1.last_name}: {  user1.login_attempts}")