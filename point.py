#1 take the number of points one team is ahead
points_str=input("Enter the lead points: ")
points_remaining_int = int(points_str)

#2 subtract 3
lead_calc_float = float(points_remaining_int - 3)

#3 add half-point if team that is ahead has ball, subtract three if other team has ball
has_ball_str = input("Does the lead team have the ball? (Y/N): ")

if has_ball_str=='Y':
	lead_calc_float = lead_calc_float + 0.5
else:
	lead_calc_float = lead_calc_float - 0.5
	
# (No. less than zero become zero)
if lead_calc_float<0:
	lead_calc_float = 0
	
#4 square that:
lead_calc_float = lead_calc_float**2

#5 if the result > no. of seconds left in game.
#lead is safe
seconds_remaining_int = int(input("Enter remaining seconds: "))

if lead_calc_float>seconds_remaining_int:
	print ("Lead is safe")
else:
	print ("Lead is not safe.")
