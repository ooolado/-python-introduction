# Dictionary is { key: value }

student1 = {"name": "Joe", "age":20, "gender": "male", "course": "bachelor od arts"}

student2 = {"gender": "male", "name": "mark", "age": 16, "course": "higher secondary"}

student3 = {"name": "christina", "age":16, "gender": "female", "course": "higher secondary"}

print(student1)
print(type(student1))
print(student1["name"])
print(student2["course"])
print(student3["gender"])

# syntax to access age of student 1 
student1["age"] = 21

student1 = {"name": "Joe", "age": 20,
            "gender": "male", "course": "bachelor od arts"}

print(student1) 

student3["name"] = "Emma"  # i want to change the name of student 3 to Emma
print(student3)

student2["results"] = True

student3["hobbies"] = ["reading", "writing"]

print(student2)

print(student3) 

print(student3["hobbies"])

# > dir([])  #to see possible actions you can perform with dictionary

student3.pop("age")
 
print(student3)

print(student3.keys())

print(student3.values())

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# print(car.keys())
# print(car.values())

for i in car.keys():
    print(i)
    
print(car.items())

for i in car.items():
    print(i)

for key, val in car.items():
    print(key, val)

student3.clear()  # to make the list empty
print(student3)
