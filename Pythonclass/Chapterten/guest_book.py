filename = 'book.txt'
user = input()

while user == True:
    user = input(" Please enter your name here: ")


with open(filename, 'w') as file_object:
    file_object.write("Greeetings welcome to the otherside." + user.title())

with open(filename, 'a') as file_object:
    file_object.write("Thank you for your visit. It's nice to see you again Mr." + user.title())

return user
