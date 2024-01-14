emails = [
    "vamsi@jjtech.com",
    "ironman@amazon.in",
    "hulk@accenture.org",
    "spiderman@microsoft.com",
    "capain.america@google.us"
]

companies = []

for i in emails:
    print(i)
    data = i.split("@")
    company_details = data[1].split(".")
    print(company_details)
    print(company_details[0])
    companies.append(company_details[0])


print(companies)
