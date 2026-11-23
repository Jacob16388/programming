#header idk
name = input("Enter student name: ")
score = int(input("Enter score: "))

if score < 0 or score > 100:
    print("Error: score must be 0 to 100.")
else:
    if score >= 90:
        article = "an"
        letter = "A"
    elif score >= 80:
        article = "a"
        letter = "B"
    elif score >= 70:
        article = "a"
        letter = "C"
    elif score >= 60:
        article = "a"
        letter = "D"
    else:
        article = "an"
        letter = "F"

    print(f"{name} got {article} {letter}.")

    if score >= 60:
        print(f"{name} passed.")
    else:
        print(f"{name} did not pass.")

    if score == 100:
        print("Perfect score!")