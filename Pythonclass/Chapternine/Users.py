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
         print(self.login_attempts)

    def increment_login_attempts(self,attempts):
        """ Show User attempts to login."""
        self.login_attempts += attempts + 1

    def reset_login_attempts(self):
        """ Reset login attempts to zero."""
        self.login_attempts = 0

    def greet_user(self):
        """Great User"""
        print("\nHello " + self.first_name.title() + " " + self.last_name.title()
        + " nice to meet you" + ".")

class Admin(User):
    "ALL MIGHTY ADMIN"
    def __init__(self,first_name, last_name, age, account_id):
        """ Initialize first and last name attributes"""

        super().__init__(first_name, last_name, age, account_id)
        self.privileges = privileges()

    def show_privileges(self):
        """ Show admin privileges"""
        print("Admin has the following privileges:")
        for priv in self.privileges:
            print(priv)

class Privileges():
   """ I got none """
   def __init__(self, first_name, last_name,):
     """Initialize privileges"""
     self.first_name = first_name
     self.last_name  = last_name
     self.privileges = ['I got none', ' White privilege', ' HA!']


   def describe_privileges(self, first_name, last_name):
      """Describe privileges"""
      print(self.first_name.title() + self.last_name.title())

   def show_privileges(self):
     """ Show privileges"""
     print(" \nI " + self.first_name.title() + " " + self.last_name.title() + " have the following privileges:")
     for priv in self.privileges:
       print(priv)

admin = Privileges('shawn', 'tarver')
admin.show_privileges()


admin = Admin('Bob', 'Saul', ' 24', '198')
admin.show_privileges()

user = User('John','Tovar', 123, 9)
user.describe_user()
user.increment_login_attempts(10)
user.reset_login_attempts()
user.greet_user()

print("\nUser: " + user.first_name.title() + " " + user.last_name + ".")
print("\nUser is " + str( user.age) + " years old.")
print("\nUser's ID is: " + str(user.account_id)  + " login attempts " + str(user.login_attempts))

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

user = User('Oscar', 'Is Over 9000!', 29, 99999)
user.greet_user()
