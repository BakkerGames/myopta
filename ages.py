user_age = input("What is your age? ")
if int(user_age) < 18:
    print("Would you like some ice cream?")
elif int(user_age) < 21:
    print("You can vote!")
elif int(user_age) < 67:
    print("You can buy alcohol!")
else:
    print("Welcome to retirement!")
