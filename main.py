while True:
	try:
		myBill = float(input("What was the bill?: "))
		numberOfPeople = int(input("How many people?: "))
		tip = int(input("What % of bill would you like to leave for a tip?: "))
		tip = tip / 100
		tip = myBill * tip
		total = myBill + tip
		answer = total / numberOfPeople
		answer = round(answer, 2)
		print("You each owe", answer)

		break # I use this to break the loop assuming the inputs are valid.

	except ValueError:
		print("Please enter valid numeric values for the calculator to work")
 
