def validate_card(card_number, pin_number, exp_date, ccv_number):
    print("validating the card with number:", card_number)
    print("calling the db to validate credentials:", card_number, pin_number, exp_date, ccv_number)
    
print("buying a shirt in the Levis store....")
validate_card(1231414, 1342, "2025-08", 765)

print("Making online payment for the wifi bill..")
validate_card(1256478, 1276, "2029-01", 543)


def withdraw_money(amount, card_number, pin, exp_date, ccv_number):
    print("withdraw money....", amount)
    validate_card(card_number, pin, exp_date, ccv_number)


withdraw_money(1000, 9312743, 1232, "2029-10", 982)
