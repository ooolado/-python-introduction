# we use if when we have a single condition
# we use if-else if we have 2 conditions

marks = int(input("Enter your marks: "))

if marks >= 85 and marks <= 100:
    print("Grade A")
elif marks >= 75 and marks < 85:
    print("Grade B")
elif marks >= 50 and marks < 75:
    print("Grade C")
elif marks >= 40 and marks < 50:
    print("Grade D")
else:
    print("Fail")
    print("Please contact the school administrator")
