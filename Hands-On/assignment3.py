# IF COMPANY IS jjTECH OR MICROSOFT, WE WILL SEND 70% PARTNER DISCOUNT COUPON TO EMAIL ADDRESS 
# ELSE SEND 10% RGULAR DISCOUNT
emails = [
    "vamsi@jjtech.com",
    "ironman@amazon.in",
    "hulk@accenture.org",
    "spiderman@microsoft.com",
    "capain.america@google.us"
]

companies = []

for i in emails:
    # print(i)
    data = i.split("@")
    company_details = data[1].split(".")
    # print(company_details)
    # print(company_details[0])
    companies.append(company_details[0])

    if company_details[0] == "jjtech" or company_details[0] == "microsoft":
        print("Sending COUPON70 to email ",i)
    else:
        print("Sending COUPON10 to email ",i)
        

# print(companies)

