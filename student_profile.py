
print("====================================================================")
print("Name: Akpobomowei Ayibanua Rebecca")
print("Matriculation number: VUG/SEN/26/16671")
print("Programme: B.Sc. Software Engineering")
print("Level: 100")
print("====================================================================")
print()
print("COS101 PRACTICAL ASSIGNMENT 2")
print("Calculations with python")
print()
# This program calculate a student weekly expence
Name = "Ada Okeke"
daily_transport_cost=float(input("Daily transport cost:"))
daily_feeding_cost=float(input("Daily feeding cost:"))
days_on_campus=int(input("Days on campus:"))
other_weekly_expences=float(input("other weekly expenses:"))

Total_transport = daily_transport_cost * days_on_campus
Total_feeding = daily_feeding_cost * days_on_campus
weekly_expense = Total_feeding + Total_feeding + other_weekly_expences
print()
print("Student:", Name)
print("Transport total: NGN{transport:.2}")
print("Feeding total: NGN{feeding:.2")
print("Other expenses: NGN{other_expenses:.2}")
print("weekly total: NGN{weeklytotal:.2}")
print(weekly_expense)
