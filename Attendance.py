# Import Libraries
import pandas as pd
import numpy as np

# Import Attendees
attXl = pd.read_excel("Attendance Example.xlsx", usecols='A')
attList = np.hstack(attXl.to_numpy().tolist())
attEmails=set(attList)

# Import Registered
regXl = pd.read_excel("Registration Roster.xlsx", usecols='E')
regList = np.hstack(regXl.to_numpy().tolist())
regEmails =set(regList)

# Set Operations
regNotAttended = regEmails.difference(attEmails)
attButNotRegistered = attEmails.difference(regEmails)
regAndAttended = attEmails.intersection(regEmails)
notBoth = attEmails.symmetric_difference(regEmails)

# Output Operations
print()
print("Number of Attendees: " + str(len(attEmails)))
print("Number of Registered: " + str(len(regEmails)))
print("Registered, but not Attended: " + str(len(regNotAttended)))
#print()
#print(regNotAttended)
#print()
print("Attended, but not Registered: " + str(len(attButNotRegistered)))
#print()
#print(attButNotRegistered)
#print()
print("Registered and Attended: " + str(len(regAndAttended)))
#print()
#print(regAndAttended)
#print()
print("Diff Check: " + str(len(notBoth) - (len(regNotAttended) + len(attButNotRegistered))))