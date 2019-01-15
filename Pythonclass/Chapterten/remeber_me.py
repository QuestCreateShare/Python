import json
# Load the username, if it has been stored previously.
# Otherwise, prompt for the username and store it.
filename = 'username.json'
try:
 with open(filename) as f_obj:
    username = json.load(f_obj)
except FileNotFoundError:
    username = input("What is your name? ")
    json.dump(username, f_obj)
    print("we'll remember you when you come back, " + username + "!")

else:
    print("Welcome back " + username + "!")
