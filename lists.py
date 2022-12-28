# List of names
names = ["Harry", "Ron", "Hermione", "Ginny"]

# Print first name
print(names[0])

# Add a new name
names.append("Draco")

# Sort names alphabetically
names.sort()
names.append("Dumbledore")

# Print list of names
print(names)

#deletes an item of list
names.remove("Hermione")
names.pop(0)


# prints one name in a line till the end of the list
for name in names:
    print(name)