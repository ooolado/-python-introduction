import boto3
ssm_client = boto3.client('ssm')
# response = ssm_client.get_parameter(Name="netflix-movies-db", WithDecryption=True)
# parameter_value = response['Parameter']['Value']
# print(parameter_value)
# response = ssm_client.get_parameter(Name="netflix-user-db", WithDecryption=True)
# parameter_value = response['Parameter']['Value']
# print(parameter_value)
# response = ssm_client.get_parameter(Name="/jjtech/dev/instancetype", WithDecryption=True)
# parameter_value = response['Parameter']['Value']
# print(parameter_value)


# def get_ssm_parameter(parameter_name):
#     response = ssm_client.get_parameter(
#         Name=parameter_name, WithDecryption=True)
#     parameter_value = response['Parameter']['Value']
#     print(parameter_value)


# get_ssm_parameter("netflix-user-db")
# get_ssm_parameter("netflix-movies-db")
# get_ssm_parameter("/jjtech/dev/instancetype")
# get_ssm_parameter("/jjtech/dev/amiid")

# def greet(name, friend):
#     print("Hi there")
#     print("hows it going", name)
#     print("What are you working on these days!")
#     print("Haven't seen you in a while")
#     print("how is our other friend: ", friend)
    
    
# greet("Orlando", "vamsi")

# # greet("Vamsi")


    