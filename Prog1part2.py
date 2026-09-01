total_pennies = int(input("Enter total pennies: "))

quarters = total_pennies // 25
remaining_pennies = total_pennies % 25

dimes = remaining_pennies // 10
remaining_pennies = remaining_pennies % 10

nickels = remaining_pennies // 5
pennies = remaining_pennies % 5

print("Quarters:", quarters)
print("Dimes:", dimes)
print("Nickels:", nickels)
print("Pennies:", pennies)
