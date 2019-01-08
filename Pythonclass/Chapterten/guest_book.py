filename = 'book.txt'
prompt= " Please enter your name here: "
prompt += "\nEnter 'quit' to after you have entered in your name"


mesasge = " "
while  message != 'quit':
    message = input(prompt)
    user = unregistered_users

    with open(filename, 'w') as file_object:
        file_object.write("Greeetings welcome to the otherside." + user.title() + "\n")

    with open(filename, 'a') as file_object:
        file_object.write("Thank you for your visit. It's nice to see you again Mr." + user.title() + "\n")
