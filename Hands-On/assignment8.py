# def greeting():
#     print("hello everyone")

# greeting()
# result = greeting()
# print(result)

# response = len("ironman")
# print(response)

def validate_account(account_number):
    print("validating account: ", account_number)
    print("connecting to the database...")
    print("verifying in the database, for account:", account_number)
    # print("account is valid")
    return True  # return is to return the end value of a function

# validate_account(12344555)  # invoking the function
print("Money to withdraw 1000")   
is_valid = validate_account(12344555)  #invoking the function
if is_valid == True:
    print("withdrawing amount: 1000")
    

# i will like to withdraw money, hence need to validate account first, before you can withdraw
