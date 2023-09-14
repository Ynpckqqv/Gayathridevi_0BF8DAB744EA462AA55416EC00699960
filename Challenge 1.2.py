"write a program  that determines wheather a y3ar entered by the user is a leap year or not using ifelif-else statements."
year= int(input("Enter thevyear:"))
if year%4==0:
  if year%100==0:
    if year%400==0:
        print("Leap year")

    else:
         print("Not a leap year")
      