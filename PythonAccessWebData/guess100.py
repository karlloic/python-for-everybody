
def print_greater_or_lesser(guess, target):
    if guess > target:
        print("Sorry " + str(guess) + " is not correct\n Your answer is greater than the target")
    elif guess < target:
        print("Sorry " + str(guess) + " is not correct\n Your answer is less than the target")


def print_even_or_odd(value):
    if value % 2 != 0:
        print("Sorry " + str(x) + " is not correct\n The answer is odd")
    else:
        print("Sorry " + str(x) + " is not correct\n The answer is even")


def print_divisible_by(value, divisor):
    if value % divisor == 0 & divisor == 3:
        print("The value is not divisible by 5\n The value is divisible by 5" + str(divisor))
    else:
        print("The value is not divisible by " + str(divisor) + "\nThe value is divisible by 5")


number = 85
trial = 1
x = 0
while trial < 5:
    x = int(raw_input("Enter a number: "))
    if x == number:
        print("Congratulations, you won. The number was " + str(number))
        exit()
    if trial == 1:
        print_greater_or_lesser(x, number)
    elif trial == 2:
        print_even_or_odd(number)
    elif trial == 3:
        print_divisible_by(number, 3)
    trial += 1

print("Too bad you lost. The answer was " + str(number))
