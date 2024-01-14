import boto3
import requests

BASE_URL = "https://reqres.in"

# list users
def list_users():
    print("Request: List users...")
    response = requests.get("{}/api/users".format(BASE_URL))
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

users = list_users()
print(users)

# single user
def list_user(user_id):
    print("Request: List user...", user_id)
    response = requests.get("{}/api/users/{}".format(BASE_URL, user_id))
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

print()
list_user(1)
list_user(5)
list_user(6)

# create user
def create_user(user_information):
    print("Request: Create user...", user_information)
    response = requests.post("{}/api/users".format(BASE_URL), user_information)
    print("ResponseCode: ", response)
    print("ResponseBody: ", response.json())
    return response.json()

create_user({
    "name": "ironman",
    "job": "save the world"
})
create_user({
    "name": "black panther",
    "job": "save the wakanda"
})
create_user({
    "name": "naruto",
    "job": "save hidden leaf"
})

# To store the  BASE_URL in secret place using SSM
# ssm_client = boto3.client('ssm')

# def get_ssm_parameter(parameter_name):
#     response = ssm_client.get_parameter(
#         Name=parameter_name, WithDecryption=True)
#     parameter_value = response['Parameter']['Value']
#     # print(parameter_value)
#     return parameter_value


# credentials = get_ssm_parameter("netflix-user-db")
# print("connect to the database using credentials:", credentials)
# # get_ssm_parameter("netflix-movies-db")
# # get_ssm_parameter("/jjtech/dev/instancetype")
# # get_ssm_parameter("/jjtech/dev/amiid")
