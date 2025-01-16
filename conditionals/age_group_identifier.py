print("<---------- AGE GROUP IDENTIFIER ---------->")
# input
name = str(input("Enter your Name: "))
age = int(input("Enter your Age: "))

if age < 13:
    print(f"Hey {name}, You are a Child")
elif age <= 19:
    print(f"Hey {name}, You are a Teenager")
else:
    print("You are an Adult, you just don't know!")
