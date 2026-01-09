import datetime
name = input("Hello! Please Enter your name:")
print("hello " + name)
age=int(input("Enter your age:"))
year_now=datetime.datetime.now()
print("You will turn 100 in " + str(int(100-age)+int(year_now.year)))
