while True:
    weight = float(input("Enter your body weight in Kg: \n"))
    height = float(input("Enter your height in m: \n"))

    bmi = weight / (height * height)

    if bmi < 16:
        print(f"Your BMI is {round(bmi, 2)}, you are underweight (Severe thinness).")

    elif bmi >= 16.0 and bmi <= 16.9:
        print(f"Your BMI is {round(bmi, 2)}, you are underweight (Moderate thinness).")

    elif bmi >= 17.0 and bmi <= 18.4:
        print(f"Your BMI is {round(bmi, 2)}, you are underweight (Mild thinness).")

    elif bmi >= 18.5 and bmi <= 24.9:
        print(f"Your BMI is {round(bmi, 2)}, you have a Normal range.")

    elif bmi >= 25.0 and bmi <= 29.9:
        print(f"Your BMI is {round(bmi, 2)}, you are overweight (Pre-obese).")

    elif bmi >= 30.0 and bmi <= 34.9:
        print(f"Your BMI is {round(bmi, 2)}, you are Obese (Class I).")

    elif bmi >= 35.0 and bmi <= 39.9:
        print(f"Your BMI is {round(bmi, 2)}, you are Obese (Class II).")

    elif bmi >= 40.0:
        print(f"Your BMI is {round(bmi, 2)}, you are Obese (Class III).")

    choice = input("Do you want to continue? Enter 'y' or 'n': ")
    if choice != 'y':
        print("Goodbye!")
        break
