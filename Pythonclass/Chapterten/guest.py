filename = 'new_guest.txt'
name = input("Write name")

with open(filename, 'w') as file_object:
    file_object.write("Their name is: " + name.title())
