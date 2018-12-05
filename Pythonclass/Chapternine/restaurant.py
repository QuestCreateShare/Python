class Restaurant ():
    """ A description of a restaurant. """
    def  __init__(self, restaurant_name , cuisine_type):
        """ Initializatize restaurant and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served =

    def  describe_restaurant(self):
        """ Describe the restaurant"""
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + ".")


    def set_number_served(self):++
        """Show customers that have been serverd"""
        print(" The restaurant has served: " + str(self.number_served) + " customers.")

    def  open_restaurant(self):
      """ The Restaurant is open"""
      print(self.restaurant_name.title() + " is now open for business!")


restaurant = Restaurant('Hi',' Japanese')
restaurant.describe_restaurant()

restaurant.number_served = 10
restaurant.set_number_served()
restaurant.open_restaurant()


print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('Hola', ' Tex-Mex')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('LOL', ' Mexican')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")

restaurant = Restaurant('Yo', ' American')
restaurant.describe_restaurant()

print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant serves :" + restaurant.cuisine_type + " cuisine ")
