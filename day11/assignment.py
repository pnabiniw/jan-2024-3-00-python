"""
WAP to prompt the user for hours and rate per hour using input to compute gross pay.
Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours.
Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75).
You should use input to read a string and float() to convert the string to a number.

"""

rate = float(input("Enter rate per hour "))
worked_hrs = float(input("Enter total work hours "))

if worked_hrs <= 40:
    total_pay = rate * worked_hrs
else:
    normal_pay = 40 * rate
    ot_pay = (worked_hrs - 40) * 1.5 * rate
    total_pay = normal_pay + ot_pay
print("Total pay is ", total_pay)
