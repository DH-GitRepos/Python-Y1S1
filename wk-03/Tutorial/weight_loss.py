# lecture exercise - weight loss calculator

CALS_PER_HR_CYCLE = 200
CALS_PER_HR_RUN = 475
CALS_PER_HR_SWIM = 275
CALS_PER_LB = 3500

hrs_cycling = float(input("Please enter hours spent cycling: "))
hrs_running = float(input("Please enter hours spent running: "))
hrs_swimming = float(input("Please enter hours spent swimming: "))

calories_cycling = CALS_PER_HR_CYCLE * hrs_cycling
calories_running = CALS_PER_HR_RUN * hrs_running
calories_swimming = CALS_PER_HR_SWIM * hrs_swimming

total_calories_burnt = calories_swimming + calories_running + calories_cycling

total_lbs_lost = total_calories_burnt / CALS_PER_LB

print("\nYou have burnt {:.2f} calories and lost {:.2f} pounds".format(total_calories_burnt, total_lbs_lost))

