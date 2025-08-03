from datetime import datetime

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))

this_year = datetime.now().year
years_left = retirement_age - age

print()
print(f"It's {this_year}. You will retire in {this_year + years_left}.\n"
      f"You have only {years_left} years of work to go!")