print("Welcome to the tip calculator.")

#Variables
bill = float(input("What was the total bill?\n$"))
tip = int(input("How much tip would you like to give?\n"))
split = int(input("How many people to split the bill?\n"))

#Calculus
tipPorcentaje = tip / 100
totalTipAmount = bill * tipPorcentaje
totalBill = bill + totalTipAmount
splitPersons = totalBill / split
finalAmount = round(splitPersons, 2)

print(f"Each person should pay: ${finalAmount}.")