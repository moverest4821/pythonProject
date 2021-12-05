items_total = 0
items_number = int(input("number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))
for i in range(items_number):
    price = float(input("Price of items: "))
    items_total += price
if items_total >100:
    items_total *= 0.9
print("Total price for ", items_number, " items is $", items_total, sep='')