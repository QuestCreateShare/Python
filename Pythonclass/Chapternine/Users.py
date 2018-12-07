class User():
    """ Make a user"""
    def __init__(self,first_name, last_name, age, account_id):
     """ Initialize first and last name attributes"""
     self.first_name = first_name
     self.last_name  = last_name
     self.age = age
     self.account_id = account_id
     self.login_attempts = 0

    def describe_user(self):
     """Describe user"""
     print(self.first_name.title() + self.last_name.title())
     print(self.age)
     print(self.account_id)

     def increment_login_attempts(self):
        """ Show User attempts to login."""
        self.login_attempts +1

     def reset_login_attempts(self,attempts):
       """ Reset login attempts to zero."""
              
     def greet_user(self):
      """Great User"""
     print("\nHello " + self.first_name.title() + " " + self.last_name.title()
      + " nice to meet you" + ".")

user = User('John','Tovar', 123, 9)
user.describe_user()
user.increment_login_attempts()
user.login_attempts()
user.greet_user()

print("\nUser: " + user.first_name.title() + " " + user.last_name + ".")
print("\nUser is " + str( user.age) + " years old.")
print("\nUser's ID is: " + str(user.account_id))

user = User('Miguel', ' Gonzales', 25, 22)
user.describe_user()
print("\nUser: " + user.first_name.title() + " " + user.last_name + ".")
print("\nUser is " + str( user.age) + " years old.")
print("\nUser's ID is: " + str(user.account_id))

user = User('Laura', 'Hernandez', 27, 29292)
user.greet_user()
print("\nUser: " + user.first_name.title() + " " + user.last_name + ".")
print("\nUser is " + str( user.age) + " years old.")
print("\nUser's ID is: " + str(user.account_id))
