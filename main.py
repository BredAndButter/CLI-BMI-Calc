while True:
	System = input("[i] Imperial system, [m] Metric system, or [s] Shutdown: ")

	if System.lower() == "i":
		print("Imperial")
		print()

		while True:
			Weight = input("Enter your weight in pounds: ")
			try:
				Weight = float(Weight)
				break
			except:
				print("Enter a number.")

		while True:
			Height = input("Enter your height in inches: ")
			try:
				Height = float(Height)
				break
			except:
				print("Enter a number.")

		Top = Weight * 703
		Bottom = Height ** 2

		Answer = Top / Bottom

		print(Answer)
	elif System.lower() == "m":
		print("Metric")
		print()

		while True:
			Weight = input("Enter your weight in kilograms: ")
			try:
				Weight = float(Weight)
				break
			except:
				print("Enter a number.")

		while True:
			Height = input("Enter your height in meters: ")
			try:
				Height = float(Height)
				break
			except:
				print("Enter a number.")

		Top = Weight
		Bottom = Height ** 2

		Answer = Top / Bottom

		print(Answer)
	elif System.lower() == "s":
		quit()
	else:
		print("Did not understand that, try again.")