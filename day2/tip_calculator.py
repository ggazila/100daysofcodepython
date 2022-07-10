print("Welcome to the tip calculator")
total_bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_count = int(input("How many people to split the bill? "))

result = (total_bill + (total_bill / 100 * percentage)) / people_count

print(f"Each person should pay: ${round(result, 2)}")
