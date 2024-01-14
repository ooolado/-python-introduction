# List is []

# fruit1 = "kiwi"

# fruit2 = "grapes"

# fruit3 = "apple"

# print(fruit1, fruit2, fruit3)
fruits = ["kiwi", "grapes", "apple"]
students = ["naruto", "sasuke", "orlando"]
speeds = [30, 50, 20, 75, 100]
my_custom_list = ["orlando", 28, 5.7, True, None]


print(fruits)
print(students)
print(speeds)
print(my_custom_list)

print(type(speeds))

print(len(fruits))
print(len(students))
print(len(my_custom_list))
print(len(speeds))

fruits = ["kiwi", "grapes", "apple"]
           # [0]      [1]
print(fruits[0])      #to print kiwi
print(students[2])
fruits = ["kiwi", "grapes", "apple", "orange", "banana", "strawberry", "watermelon", "pineapple", "mango", "pear", "cherry", "blueberry", "raspberry", "blackberry", "apricot", "plum", "peach", "nectarine", "pomegranate", "grapefruit", "lemon", "lime", "coconut", "fig", "guava", "passion fruit",
          "cantaloupe", "honeydew melon", "cucumber", "papaya", "kiwifruit", "persimmon", "cranberry", "avocado", "papaya", "dragon fruit", "date", "jackfruit", "kiwi berry", "lychee", "mangosteen", "persimmon", "quince", "rhubarb", "tangerine", "starfruit", "blackcurrant", "boysenberry", "elderberry", "gooseberry"]
fruits.sort()
print(fruits)

fruits.sort(reverse=True)
print(fruits)

print(fruits.index("kiwi"))  # the position number of kiwi item

fruits.append("kola")
print(fruits)
for each_fruit in fruits:
    print(each_fruit)