# Write a script for printing address labels.
# Assign the information to a suitable variables: name, surname, country, city, street, number, postal code.
# Print the information in a pretty style.
name=str(input("Insert name: "))
surname=str(input("Insert surname: "))
country=str(input("Insert country: "))
city=str(input("Insert city: "))
street=str(input("Insert street: "))
number=int(input("Insert number: "))
postal_code=int(input("Insert postal code: "))
print(f"\n\n{name} {surname}\n{number}, {street}\n{city}, {postal_code}\n{country}")