import math

cheta_height = 20
cheta_mass = 45

chidera_height = 25
chidera_mass = 40

cheta_bmi = cheta_mass / math.pow(cheta_height, 2)
chidera_bmi = chidera_mass / math.pow(chidera_height, 2)

if cheta_bmi > chidera_bmi:
	print("Cheta's BMI is higher than Chidera's")
else:
	print("Cheta's BMI is lesser than Chidera's")
