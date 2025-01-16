# check odd or even
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number")
else:
    print(f"{number} is an odd number")


# Grading scheme
student_name = str(input("Enter your name: "))
score_value = int(input("Enter your score: "))
if score_value >= 90:
    print(f"Hello {student_name}, your grade is A")
elif score_value >= 80:
    print(f"Hello {student_name}, your grade is B")
elif score_value >= 70:
    print(f"Hello {student_name}, your grade is C")
else:
    print(f"Hello {student_name}, Your Grade is F")