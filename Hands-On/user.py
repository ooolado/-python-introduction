from AWS import rds, s3


print("user creation process started....")
rds.insert_data("ironman", "ironman@avengers.com", "ironman")
s3.upload_profile_pic()