myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tip = int(
    input("What percent tip do you want to leave: 15, 18, or 20 percent? "))
bill_with_tip = myBill + (myBill * tip / 100)
print(f"Your total bill with tip is {round(bill_with_tip, 2)}")

per_person = bill_with_tip / numberOfPeople

print(f"You all owe {round(per_person, 2)}")
