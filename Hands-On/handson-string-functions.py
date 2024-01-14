# """
# lower() and upper():
#     These methods return a new string with all the characters in lowercase or uppercase, respectively.

# capitalize():
#     This method capitalizes the first character of the string.

# strip(), rstrip(), and lstrip():
#     These methods remove any whitespace characters (spaces, tabs, etc.) from the beginning and/or end of the string.

# split():
#     This method splits a string into a list of substrings, based on a specified delimiter (e.g., space, comma, etc.).
#     Sample "1234567890,0987654321,2468013579,9876543210,0123456789,1357908642,3141592653,2718281828,9876543210,0123456789,2468013579,1357908642,3141592653,2718281828,9876543210,0123456789,1234567890,0987654321,1357908642,2468013579"
# join():
#     This method joins a list of strings into a single string, using a specified delimiter.

# replace():
#     This method replaces all occurrences of a specified substring with another substring. This will return another string

# find():
#     This method returns the index of the first occurrence of a specified substring in the string, or -1 if it is not found.

# startswith() and endswith():
#     These methods return a boolean value indicating whether the string starts or ends with a specified substring.

# len():
#     This function returns the length of the string.

# Slice():
#     A string can be sliced to extract a portion of the string. Slice method uses square bracket to wrap the start index and the end index. End index is not included in the return value.

# """


# # lower() and upper():
# #     These methods return a new string with all the characters in lowercase or uppercase, respectively.

# # greetings = "Hello Everyone!"
# # greetings = greetings.lower()
# # greetings = greetings.upper()
# # print(greetings)

# # capitalize():
# #     This method capitalizes the first character of the string.

# # greetings = greetings.capitalize()


# # strip(), rstrip(), and lstrip():
# #     These methods remove any whitespace characters (spaces, tabs, etc.) from the beginning and/or end of the string.
# # training = " Hello Class "
# # greetings = training.lstrip()
# # print(len(training)) # /13
# # print(len(greetings)) # /11

# # len():  " 912 603 38832 "
# #     This function returns the length of the string.
# # greetings = len(greetings)

# # print(greetings)


# # split():
# #     This method splits a string into a list of substrings, based on a specified delimiter (e.g., space, comma, etc.).
# # account_numbers = "1234567890,0987654321,2468013579,9876543210,0123456789,1357908642,3141592653,2718281828,9876543210,0123456789,2468013579,1357908642,3141592653,2718281828,9876543210,0123456789,1234567890,0987654321,1357908642,2468013579"
# # account_list  =   account_numbers.split(",")


# # join():
# #     This method joins a list of strings into a single string, using a specified delimiter.
# # accountWithSlash = "&".join(account_list )
# # print(accountWithSlash)
# # print(type(accountWithSlash))


# # replace():
# #     This method replaces all occurrences of a specified substring with another substring. This will return another string

# # greetings = "Hello Everyboard, how are you today Everyboard"
# # greetings = greetings.replace('Everyboard', "everyone")
# # print(greetings)


# # find():
# #     This method returns the index of the first occurrence of a specified substring in the string, or -1 if it is not found.

# # greetings = "Hello World!, Hello everyone"
# # greetings = greetings.find("zebra")
# # print(greetings)

# # startswith() and endswith():
# #     These methods return a boolean value indicating whether the string starts or ends with a specified substring.

# # greetings = "Hello World!, Hello everyone"  #boolean
# # greetings = greetings.startswith("Zebra")
# # if greetings == True:
# #     print("Yes! we did it")
# # else: print("oh On, we missed it.")


# # greetings = "Hello World!, Hello everyone"  #boolean
# # # slice_words = greetings["Start Index": "End Index"]
# # slice_words = greetings[3:]
# # print(slice_words)


# # =======================================================

name = "vamsi"
name1 = "IRONMAN"
username = "vamsi"
print(name.upper())
print(name1.lower())
print(name1.replace("IRON", "GOLD"))
print(len(username))

corrected_name = username.strip()

print(len(corrected_name))

message = "hello everyone, how are you"

print(message.split(","))

email = "vamsi@gmail.com"

print(email.split("@"))

msg = "hi, everyone, how is it going"

msg.split ()



