class Restaurant ():
    """ A description of a restaurant. """
    def  __init__(self, restaurant_name , cuisine_type):
        """ Initializatize restaurant and cuisine attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def  describe_restaurant(self):
        """ Describe the restaurant"""
        print(self.restaurant_name.title() + " serves " + self.cuisine_type.title() + ".")

    def  open_restaurant(self):
      """ The Restaurant is open"""
      print(self.restaurant_name.title() + " is now open for business!")


restaurant = Restaurant('Hi',' Japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print("\nThe restaurant is called :" +  restaurant.restaurant_name.title())
print("The restaurant servers :" + restaurant.cuisine_type + " cuisine ")
