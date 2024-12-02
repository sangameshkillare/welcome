n=4
if n==0:
    print("zero value")
elif n<=5:
    print("n is less than 5:")
else:
    print("n is greater than 5")

azad = 11
if azad >= 7:
    print("Impressive azad!")


score = 60
passing_score = 70
if score >= passing_score:
    print("Congratulations, you passed!")
else:
    if score >= passing_score - 5:
        print("You almost passed.")
    else:
        print("You didn't pass.")



score = 85
result = "Pass" if score >= 70 else "Fail"
print(f"You {result}.")




is_weekend = False
is_sunny = False

if is_sunny:
    if is_sunny:
        print("Go for a picnic.")
    else:
        print("Stay in and relax.")
else:
    print("It's a workday.")





is_vip = True
age = 30

if is_vip:
    if age >= 18:
        if age < 65:
            print("Welcome, VIP customer!")
        else:
            print("You're a VIP, but you qualify for senior discounts.")
    else:
        print("VIP status is for adults only.")
else:
    print("Regular pricing applies.")
