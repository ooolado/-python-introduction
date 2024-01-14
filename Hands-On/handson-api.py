import requests

#  list users
response = requests.get("https://reqres.in/api/users")
print(response)
print(response.json())

#  list single user
response = requests.get("https://reqres.in/api/users/3")
print(response)
print(response.json())

print()

#create user
result = requests.post("https://reqres.in/api/users", {
    "name": "Orlando",
    "job": "DevOps"
})
print(result)
print(result.json())

# Informational responses(100 – 199)
# Successful responses(200 – 299)
# Redirection messages(300 – 399)
# Client error responses(400 – 499)
# Server error responses(500 – 599)
