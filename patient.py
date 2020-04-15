class Patient:

    def __init__(self, social_security_num, date_of_birth, insurance_acct_num, first_name, last_name, address):
        self.__social_security_num = social_security_num
        self.__date_of_birth = date_of_birth
        self.__insurance_acct_num = insurance_acct_num
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address

# The first three properties should be read-only. 

    @property
    def social_security_num(self):
        try: 
            return self.__social_security_num
        except AttributeError:
            return 0

    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return 0

    @property
    def insurance_acct_num(self):
        try:
            return self.__insurance_acct_num
        except AttributeError:
            return 0

# First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. 

    @property
    def full_name(self):
        try: 
            return self.__first_name + " " + self.__last_name
        except AttributeError:
            return 0


# Address should have a getter and setter.

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError("Please provide a string value for the address")
