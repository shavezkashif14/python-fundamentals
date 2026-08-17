income = int(input("Enter your monthly income: "))
saving = int(input("Enter how much you save each month: "))
spending = int(input("Enter how much you spend each month: "))

print("Your money left after saving is", str(income - saving) + "!")
print("Your money left after spending is", str((income - saving) - spending) + "!")
print("You save", saving * 12, "each year!")
print("You spend", spending * 12, "each year!")
