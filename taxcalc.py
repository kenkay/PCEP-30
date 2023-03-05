income = float(input("Enter the annual income: "))

x = income

if x < 85528:
    tax = (0.18 * x) - 556.02
elif x > 85528:
    tax = (0.32 * (x - 85528)) + 14839.02

tax = round (tax, 0)

if tax <= 0:
    tax = 0
    print ("The tax is:",tax, "thalers")
else:
    print ("The tax is:",tax, "thalers")