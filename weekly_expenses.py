# Student Profile
print("Name:Akpobomowei Ayibanua Rebecca")
print("Matriculation number:VUG/SEN/26/16671")
print("Programme:B.Sc.Software engineering")
print("Level:100")
print("======================================================================")
print("COS101 PRACTICAL ASSIGNMENT")
print("Calculations with python")
print("======================================================================")

# this program calculates a student weekly expense
Name= "Ada Okafor"
daily_transport_cost = float(input("Daily transport cost:"))
daily_feeding_cost = float(input("Daily feeding cost:"))
days_on_campus = int(input("Days on campus:"))
other_weekly_expenses = float(input("Other weekly expenses:"))

# Calculations
total_transport = daily_transport_cost * days_on_campus
total_feeding = daily_feeding_cost * days_on_campus
weekly_expense = total_transport + total_feeding + other_weekly_expenses

# Output
print()
print("Student:",Name)
print(f"Transport total: NGN{total_transport:.2f}")
print(f"Feeding total:NGN{total_feeding:.2f}")
print(f"Other expenses:NGN{other_weekly_expenses:.2f}")
print(f"Weekly total:NGN{weekly_expense:.2f}")
