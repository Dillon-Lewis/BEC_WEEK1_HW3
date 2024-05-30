
#Task 1

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2

customer = input("Can I reccomend a vegitarian dish?")
print("Veggie Delight Caterers") if customer == "yes" else print("Gourmet Meals Caterers")