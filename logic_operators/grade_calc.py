import time

print("< --- SUBJECT GRADING SYSTEM --- >")
time.sleep(1)   #delay the next line after 1 second
name = str(input("What is your name: ").capitalize())
score = int(input("What did you score(/100): "))

if score >= 90:
    score = "A"
elif 80 <= score < 90:
    score = "B"
elif 70 <= score < 80:
    score = "C"
elif 60 <= score < 70:
    score = "D"
else:
    score = "F"

print("Hey {}, your score is {}".format(name, score))
