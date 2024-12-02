no1 = 1
no2 = 2
no3 = 3

if no1 > no2 and no1 > no3:
    print("no1 is the greatest:", no1)
elif no2 > no1 and no2 > no3:
    print("no2 is the greatest:", no2)
elif no3 > no1 and no3 > no2:
    print("no3 is the greatest:", no3)
else:
    print("The numbers are equal or there is a tie.")
