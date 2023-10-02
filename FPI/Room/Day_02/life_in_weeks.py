age = input("What is your current age? ")

age = int(age)

days_to_90 = 32850
weeks_to_90 = 4680
months_to_90 = 1080

days = days_to_90 - (age * 365)
weeks = weeks_to_90 - (age * 52)
months = months_to_90 - (age * 12)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")