############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""
    
    

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name
        

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        # Fill in the rest
        self.pairings.append(pairing)

        return self.pairing


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

        return self.code


def make_melon_types():
    """Returns a list of current melon types."""
    #instantiates the class MelonType for each melon type provided
    #we need to somehow append the melon types provided so that they appear in the empty list below

    all_melon_types = []

    # Fill in the rest
    #melon type is a class called melon type
    #everytime we need to access that class, we need to create an object
    #everytime you create a calss of a melon, you call it the name of the melon
    #everytime you do this, you can do this in a fucntion that appends to a list each type that you are creating
    #return the list of the funciton you created/ the fucniton will be a helper funciton that is called as a paramterer in this

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    # Fill in the rest
    # Needs __init__ and is_sellable methods

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 

#creating an instance
melon1 = MelonType()

watermelon = MelonType('WAtermelon')
watermelon.add_pairing('ice cream')
casaba.add_pairing('mint')

