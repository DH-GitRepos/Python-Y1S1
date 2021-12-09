# PROJECT: (WK-03) Telephone Bill
# Solution written by Darren Halpin

# VARIABLES
# constants
CHARGE_PER_MINUTE = 0.15
VAT_RATE_PERCENTAGE = 20

# INPUT
minutes_used = int(input("Enter number of minutes: "))

# PROCESS/CALCULATE
basic_call_charge = minutes_used * CHARGE_PER_MINUTE
vat_due = (basic_call_charge/100) * VAT_RATE_PERCENTAGE
total_bill = basic_call_charge + vat_due

# OUTPUT
print("Number of minutes used: {:} \nBasic call charge £{:.2f} \nVAT due: £ {:.2f} \nTotal bill: £{:.2f}"
      .format(minutes_used, basic_call_charge, vat_due, total_bill))

