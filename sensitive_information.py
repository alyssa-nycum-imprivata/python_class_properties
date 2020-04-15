from patient import Patient

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.social_security_num = "838-31-2256"
# print(cashew.social_security_num)

# Neither should this
# cashew.date_of_birth = "01-30-90"
# print(cashew.date_of_birth)

# But printing either of them should work
# print(cashew.social_security_num)
# print(cashew.date_of_birth)

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)  