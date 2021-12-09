# PROJECT: (WK-03) Height converter
# Solution written by Darren Halpin

in_feet = int(input("Please enter your height in feet and inches > \nFeet: "))
in_inch = int(input("Inches: "))

feet_to_inches = in_feet * 12
total_inches = in_inch + feet_to_inches

convert_cm = float(total_inches * 2.54)
convert_mm = convert_cm * pow(10, 1)
convert_m = convert_cm * pow(10, -2)
convert_km = convert_cm * pow(10, -5)

print("Height in kilometers: {:.6f}\nHeight in meters: {:.3f}"
      "\nHeight in centimeters: {:.1f}\nHeight in millimeters: {:.1f}"
      .format(convert_km, convert_m, convert_cm, convert_mm))

