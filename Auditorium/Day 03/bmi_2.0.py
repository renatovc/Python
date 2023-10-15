# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

height = float(height)
weight = float(weight)

bmi = ((weight) / (height ** 2))

if bmi >= 35:
  print(f"Your BMI is {bmi}, you are clinically obese.")
elif bmi >= 30 and bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
elif bmi >= 25 and bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi > 18.5 and bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 18.8:
  print(f"Your BMI is {bmi}, you are underweight.")