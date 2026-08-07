def factorial(n):
    if n == 0 or n ==1:
       return 1
    return n * factorial(n-1)
    
num = int(input("ENTER A NO.:"))

if num < 0:
   print("FACTORIAL DOES NOT EXIST FOR NEGATIVE NO.")
else:
   print("FACTORIAL=",factorial(num))   
