"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__ (self,
                  self.first_name,
                  self.last_name,
                  self.email,
                  self.password
                  ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

    def __repr__(self):
        """convenience method to show information about 
        customer object in console
        """

        return "<Customer: Name is {} {} Email is {}>".format(self.first_name,
            self.last_name, self.email)


def read_customers_from_file(filepath):
    """ Read customer information file and populate 
    dictionary of customer
    
    """


