name = str(input("Enter your name: ").capitalize())
print("Welcome {}".format(name))
age = int(input("Please enter your age number: "))
is_member = str(input("Are you a member?(yes/no): "))
has_invitation = str(input("Do you have an invitation?(yes/no): "))

# verify invitation user
if has_invitation in 'yes':
    has_invitation = True
else:
    has_invitation = False

# verify membership
if is_member in 'yes':
    is_member = True
else:
    is_member = False

if is_member and age >= 18:
    print("Hey {}, you have access to Member's Event".format(name))
elif has_invitation or age >= 21:
    print("Hey {}, you have access to VIP Event".format(name))
elif is_member and has_invitation:
    print("Hey {}, you have access to Exclusive Event".format(name))
else:
    print("Hey {}, you have access to General Event".format(name))

# nesting conditionals
# if age >= 18:
#     if has_invitation:
#         print("You have access")
#     else:
#         print("Access denied: username not recognized")
# else:
#     print("access denied, you must be at least 18 yrs old")
