def calculate_bmi():
    """Calculates the Body Mass Index (BMI) based on user input."""

    # Get the user's weight in kilograms
    try:
        weight_kg = float(input("Enter your weight in kilograms: "))
        if weight_kg <= 0:
            print("Weight cannot be zero or negative. Please enter a valid weight.")
            return
    except ValueError:
        print("Invalid input for weight. Please enter a numerical value.")
        return

    # Get the user's height in meters
    try:
        height_m = float(input("Enter your height in meters: "))
        if height_m <= 0:
            print("Height cannot be zero or negative. Please enter a valid height.")
            return
    except ValueError:
        print("Invalid input for height. Please enter a numerical value.")
        return

    # Calculate BMI using the formula: BMI = weight (kg) / height^2 (m^2)
    bmi = weight_kg / (height_m ** 2)

    # Print the calculated BMI, formatted to two decimal places
    print(f"\nYour BMI is: {bmi:.2f}")

    # Provide a BMI category based on common guidelines
    print("BMI Categories:")
    if bmi < 18.5:
        print("Underweight")
    elif 18.5 <= bmi < 25:
        print("Normal weight")
    elif 25 <= bmi < 30:
        print("Overweight")
    elif 30 <= bmi < 35:
        print("Obese (Class I)")
    elif 35 <= bmi < 40:
        print("Obese (Class II)")
    else:
        print("Obese (Class III)")

# Start the BMI calculator when the script is run directly
if __name__ == "__main__":
    calculate_bmi()