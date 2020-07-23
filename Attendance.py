# User Input - Enter as long strings
attString = "swartzs@mskcc.org, bethusas@mskcc.org, wileya@mskcc.org, vemuris1@mskcc.org, rodrigh1@mskcc.org, wadea@mskcc.org, corteza1@mskcc.org, thomasj@mskcc.org, engk@mskcc.org, longd@mskcc.org, william0@mskcc.org,kosovoya@mskcc.org, knospler@mskcc.org, elligm@mskcc.org, murdyr@mskcc.org, gleyzeri@mskcc.org, dychesc@mskcc.org, feussc@mskcc.org, nwannec@mskcc.org, saporitt@mskcc.org, sivabalk@mskcc.org, lissadea@mskcc.org, tonga@mskcc.org, subramag@mskcc.org, morganj@mskcc.org, rom1@mskcc.org, magedb@mskcc.org, daviss2@mskcc.org"
regString = "ostrovsa@mskcc.org, bhattaca@mskcc.org, baldwina@mskcc.org, watsona1@mskcc.org, bijwea@mskcc.org, syeda1@mskcc.org, donga1@mskcc.org, harriota@mskcc.org, briscoa@mskcc.org, cooka@mskcc.org, kleinera@mskcc.org, marantza@mskcc.org, stevensa@mskcc.org, vellaa@mskcc.org, lissadea@mskcc.org, tonga@mskcc.org, kosovoya@mskcc.org, wileya@mskcc.org, corteza1@mskcc.org, johnsona@mskcc.org, palakuda@mskcc.org, joshia@mskcc.org, rodriga3@mskcc.org, coreaa@mskcc.org, kuzyszya@mskcc.org, iqbala1@mskcc.org, quinonea@mskcc.org, gorantla@mskcc.org, patela12@mskcc.org, pankevia@mskcc.org"

# Convert Strings to Sets
attEmails = set(attString.replace(" ","").split(","))
regEmails = set(regString.replace(" ","").split(","))

# Set Operations
regNotAttended = regEmails.difference(attEmails)
attButNotRegistered = attEmails.difference(regEmails)
regAndAttended = attEmails.intersection(regEmails)
notBoth = attEmails.symmetric_difference(regEmails)

# # Output Operations
print()
print("Number of Attendees: " + str(len(attEmails)))
print("Number of Registered: " + str(len(regEmails)) + "\n")
print("Registered, but not Attended: " + str(len(regNotAttended)))
print()
print(regNotAttended)
print()
print("Attended, but not Registered: " + str(len(attButNotRegistered)) + "\n")
print(attButNotRegistered)
print()
print("Registered and Attended: " + str(len(regAndAttended)) + "\n")
print(regAndAttended)
print()
print("Error Check: " + str(len(notBoth) - (len(regNotAttended) + len(attButNotRegistered))))