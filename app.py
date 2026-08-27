# Inputs
rent = float(input("Enter Flat/Hostel Rent: "))
food = float(input("Enter Food Expense: "))
persons = int(input("Enter Number of People: "))

a = float(input("Rate for 0 to 200 units (a): "))
b = float(input("Rate for 201 to 500 units (b): "))
c = float(input("Rate for 501 to 700 units (c): "))
d = float(input("Rate for 701 to 1000 units (d): "))
e = float(input("Rate for above 1000 units (e): "))

units = float(input("\nEnter Total Electricity Units Used: "))

# Electricity Bill Calculation
if units <= 200:
    electricity_bill = units * a
elif units <= 500:
    electricity_bill = (200 * a) + ((units - 200) * b)
elif units <= 700:
    electricity_bill = (200 * a) + (300 * b) + ((units - 500) * c)
elif units <= 1000:
    electricity_bill = (200 * a) + (300 * b) + (200 * c) + ((units - 700) * d)
else:
    electricity_bill = (
        (200 * a) + (300 * b) + (200 * c) + (300 * d) + ((units - 1000) * e)
    )

# Total Calculation
total_expense = rent + food + electricity_bill
per_person_share = total_expense / persons

# Summary Output
print("\n         BILL SUMMARY          ")
print(f"Electricity Bill : {electricity_bill:.2f}")
print(f"Total Expense    : {total_expense:.2f}")
print(f"Each Person Pays : {per_person_share:.2f}")
