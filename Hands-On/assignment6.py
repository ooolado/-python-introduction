print("mobile PIN simulation")

total_limit = 5

attempt_count = 0

Correct_PIN = 1234

while attempt_count < total_limit:
    tried_PIN = int(input("Enter PIN: "))
    if tried_PIN == Correct_PIN:
        print("login successful")
        break
    attempt_count = attempt_count + 1