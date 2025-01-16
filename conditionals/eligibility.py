print("< === Driver's License Eligibility Checker === >")
# Details of the user
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))

if age <= 13:
    print("You're too young to consider touching a steering wheel!")
    exit()

country = str(input("Enter your Country: ").lower())

# minimum age in countries
if country not in ["america", "usa"]:
    min_age = 18
else:
    min_age = 16

# validation
if age >= min_age:  # and country in ["america", "usa"]:
    print(f"Hello {name.capitalize()}, You are eligible to apply for a driver's license in {country.capitalize()}")
# elif age < 16 and country in ["america", "usa"]:
#     print(f"Hello {name}, Wait for {16 -age} more years")
# elif age >= 18:
#    print(f"Hello {name.capitalize()}, You are eligible to apply for a driver's license in {country.capitalize()}")
else:
    print(
        f"Hello {name.capitalize()}, Please wait for {min_age - age} more year(s) to apply a Driver's License in {country.capitalize()}")
