message = "Hi Vamsi, How are you?"

print(message)

name = "spiderman"

greeting = "Hi {}, How are you?".format(name)
print(greeting)


user_id = 20
url = "https://reqres.in/api/users/{}".format(user_id)
print(url)

a = "Hi {}, Whats your age {}, which country: {}".format("vamsi", 28, "India")
print(a)


user_id = 20
BASE_URL = "https://reqres.in"
url = "{}/api/users/{}".format(BASE_URL, user_id)
print(url)
