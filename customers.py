"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    def __init__ (self,
                  first_name,
                  last_name,
                  email,
                  password
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
    customer_dict = {}
    with open(filepath) as file:
        for line in file:
            (first_name,
             last_name,
             email,
             password) = line.strip().split("|")


            customer_dict[email]=Customer(first_name,
                                          last_name,
                                          email,
                                          password)
    return customer_dict


def get_customer_by_email(email):
    """ return customer given customer email """
    # needs access to the global dicctionary 'customer dic'
    return customer_dict[email]

customer_dict = read_customers_from_file("customers.txt")

