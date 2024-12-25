# BMI Calculator App

def calculate_bmi(weight, height):
    """Calculate the BMI based on weight (kg) and height (m)."""
    try:
        bmi = weight / (height ** 2)
        return bmi
    except ZeroDivisionError:
        return "Height cannot be zero."

def classify_bmi(bmi):
    """Classify the BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    """Main function to run the BMI calculator app."""
    print("Welcome to the BMI Calculator!")
    
    # Take user input
    try:
        weight = float(input("Enter your weight (in kg): "))
        height = float(input("Enter your height (in meters): "))
        
        # Validate inputs
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        # Calculate BMI
        bmi = calculate_bmi(weight, height)
        
        if isinstance(bmi, str):  # Check for errors like height being zero
            print(bmi)
        else:
            # Classify BMI
            classification = classify_bmi(bmi)
            print(f"Your BMI is: {bmi:.2f}")
            print(f"Classification: {classification}")
    
    except ValueError:
        print("Please enter valid numeric values.")

# Run the app
if __name__ == "__main__":
    main()
