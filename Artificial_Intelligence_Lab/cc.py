# grade based system
# Artificial Intelligence is a, Operating System is o, DElD is e, Data Structures is d, Digital finance is f

print("This is a grade based system where we calculate your grades")

a=int(input("Enter your Artificial Intelligence marks"))
o=int(input("Enter your Operating System marks"))
e=int(input("Enter your DELD marks"))
d=int(input("Enter your Data Structures marks"))
f= int(input("Enter your finance marks"))

if (0 <= a <= 100 and 0 <= o <= 100 and 0 <= e <= 100 and 0 <= d <= 100 and 0 <= f <= 100):
 total = (a+o+e+d+f)
 per = (total)/5
 print(f"Your Percentage is={per}")

if (per>=75):
 print("Disinction")
elif (per<75 and per>60):
 print(" First Class")
elif (per<60 and per>45):
 print("Second Class")
elif (per <45 and per>35):
 print("Third Class")
elif (per<35 and per>=0):
 print("Fail")
elif (per>100 and per<0):
 print("Invalid Input")
else:
 print("Invalid input in one of the marks")
 
