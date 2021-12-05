"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
while sales >=0:
    if sales < 500:
        print('user get 10% bonus')
        sales = float(input("Enter sales: "))
    else:
        print('user get 15% bonus')
        sales = float(input("Enter sales: "))
while sales < 0:
    print ('invalid sales')
    sales = float(input("Enter sales: "))