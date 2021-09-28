def verifyInput(inputStr, selections):
	validSelection = False

	while not validSelection:
		userSelect = input(inputStr)

		if userSelect.lower() not in selections:
			print("Sorry, that was an invalid selection. Try again.")

		return userSelect


provinces = {"Canada": ["Alberta"],
				"USA": ["California", "New York"],
				"United Kingdom": ["England", "Wales"],
				"Italy": ["Calabria", "Liguria"],
				"Netherlands": ["Zeeland"]}

userSelect = verifyInput("Alter countries or provinces (c/p): ", ["p", "c"])

if userSelect == "p":
	userSelect = "province"
else:
	userSelect = "country"

addDelete = verifyInput(f"Add or delete {userSelect} (a/d): ", ["a", "d"])

# Not done. 