#Using a try exception without a while loop.
try:
   print(10 + "Hello")
except TypeError:
    print("You can't add strings and intergers")



#Write a program that prevent you from seeing an error.
#When you try to add a string and a interger

print(" Give me two numbers and I will add them for you.")
print("Enter 'q' to quit.")


while True:
     first_number = input("\nFirst number: ")
     if first_number == 'q':
         break

     second_number = input("\nSecond_number: ")
     try:
        answer = int(first_number) + int(second_number)
     except ValueError:
        print( "you can't add intergers and strings!")

     else:
        print(answer)
