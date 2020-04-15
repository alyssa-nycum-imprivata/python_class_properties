class Student:

    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.age = 0
        self.cohort_number = 0

# Use the __str__ method on your class to specify what an object's string representation should be.

    def __str__(self):
        return f"{self.full_name} is {self.age} years old and is in cohort {self.cohort_number}"

# Define getters for all properties.
# Define a setter for all but the read only property.
# Ensure that only the appropriate value can be assigned to each.

    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return 0

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError("Please provide a string value for first name")

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return 0

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError("Please provide a string value for last name")

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError("Please provide a number for age")

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except TypeError:
            return 0

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError("Please provide a number for cohort number")

# The full name property should return first name and last name separated by a space. It's value cannot be set.

    @property
    def full_name(self):
        try: 
            return self.first_name + " " + self.last_name
        except AttributeError:
            return 0



