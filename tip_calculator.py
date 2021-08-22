print('Welcome to the tip calculator.')
total_amount = float(input('What was the total bill? $'))
number_people = int(input('How many people to split the bill? '))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? ')) 
per_person = (total_amount * (1 + (.01 * tip_percentage))) / number_people
final_amount = "{:.2f}".format(per_person)
print("Each person should pay: $" + str(final_amount))