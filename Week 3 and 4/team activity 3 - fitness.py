'''
Team Activity 3 - fitness.py
Abi Priebe
5/5/21
'''
'''
Write a Python program named fitness.py that does the following:

    1. Asks the user to enter four values:
        a. gender
        b. birthdate in this format: YYYY-MM-DD
        c. weight in US pounds
        d. height in US inches
    2. Converts the weight from pounds to kilograms (1 lb = 0.45359237 kg).
    3. Converts inches to centimeters (1 in = 2.54 cm).
    4. Calculates age, BMI, and BMR.
    5. Prints age, weight in kg, height in cm, BMI, and BMR.
Use the following design to write your program. Write code for each function that contains 
the keyword pass and then delete the keyword pass. The compute_age function is complete and 
correct, and you should not change it.
'''
# Import datetime so that it can be
# used to compute a person's age.
from datetime import datetime


def main():
    # Get the user's gender, birthdate, height, and weight.
    gender = input("Enter your gender: ")
    birth = input("Enter your birthdate (YYYY-MM-DD): ")
    weight = float(input("Enter your weight in US pounds: "))
    height = float(input("Enter your height in US inches: "))

    # Call the compute_age, kg_from_lb, cm_from_in, body_mass_index, and basal_metabolic_rate functions as needed.
    age = compute_age(birth)
    weight_kg = kg_from_lb(weight)
    height_cm = cm_from_in(height)
    bmi = body_mass_index(weight, height)
    bmr = basal_metabolic_rate(gender, weight, height, age)

    # Print the results for the user to see.
    print(f"Age (years): {age}")
    print(f"Weight (kg): {weight_kg}")
    print(f"Height: {height_cm}")
    print(f"Body Mass Index: {bmi}")
    print(f"Basal Metabolic Rate (kcal/day): {bmr}")

def compute_age(birth):
    """Compute and return a person's age in years.

    Parameter birth: a person's birthdate stored as
        a string in this format: YYYY-MM-DD
    Return: a person's age in years.
    """
    birthday = datetime.strptime(birth, "%Y-%m-%d")
    today = datetime.now()

    # Compute the difference between today and the birthday in years.
    years = today.year - birthday.year

    # If necessary, subtract one from the difference.
    if birthday.month > today.month or \
        (birthday.month == today.month and birthday.day > today.day):
        years -= 1

    return years


def kg_from_lb(lb):
    """Convert a mass in pounds to kilograms.
    Parameter lb: a mass in US pounds.
    Return: the mass in kilograms.
    1 lb = 0.45359237 kg
    """
    kg = lb * 0.45359237
    return round(kg, 1)


def cm_from_in(inch):
    """Convert a length in inches to centimeters.
    Parameter inch: a length in inches.
    Return: the length in centimeters.
    """
    cm = inch * 2.54
    return round(cm, 1)

def body_mass_index(weight, height):
    """Calculate and return a person's body mass index (bmi).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
    Return: a person's body mass index.
    """
    bmi = (10000 * kg_from_lb(weight))/(cm_from_in(height)**2)
    return round(bmi, 1)

def basal_metabolic_rate(gender, weight, height, age):
    """Calculate and return a person's basal metabolic rate (bmr).
    Parameters:
        weight must be in kilograms.
        height must be in centimeters.
        age must be in years.
    Return: a person's basal metabolic rate in kcal per day.
    """
    if gender.upper() == "F":
        return round(447.593 + 9.247 * kg_from_lb(weight) + 3.098 * cm_from_in(height) - 4.330 * age)
    elif gender.upper() == "M":
        return round(88.362 + 13.397 * kg_from_lb(weight) + 4.799 * cm_from_in(height) - 5.677 * age)

main()