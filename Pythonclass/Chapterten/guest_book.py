filename = 'book.txt'
prompt= " \nPlease enter your name here: "
prompt += "\nEnter 'quit' to after you have entered in your name"


while True:
    user = input(prompt)

    with open(filename, 'a') as file_object:
        if user =='quit':
            break
        else:
            file_object.write("Greeetings welcome to the otherside." + user.title() + "\n")
            file_object.write("Thank you for your visit. It's nice to see you again Mr." + user.title() + "\n")

    with open(filename) as file_object:
         lines = file_object.readlines()

         for line in lines:
             print(line.strip())

#TestFunction 
def reset():
    with open(filename,'w') as file_object:
        file_object.write('')
