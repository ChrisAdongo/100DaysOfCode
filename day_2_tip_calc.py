bill = float(input("What is the total bill in $?\n"))
tip = int(input("What percentage tip would you like to give: 10, 12 or 15?\n"))
people = int(input("What is the number of people to split the bill?\n"))

total_bill = round(bill * (tip / 100 + 1) / people, 1)

print(f"Your total bill is ${total_bill}.")


