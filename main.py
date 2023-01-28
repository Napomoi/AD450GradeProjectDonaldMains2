import itertools
import operator
import math

while True:
   percentGrade = input('Please enter your grade in percent: (an integer or number with decimal from 0 to 100)  ')
   try:
       percentGrade = (float(percentGrade))
       if percentGrade >= 95.0:
          print('Your  grade is  4.0')
       elif percentGrade <= 65.0:
          print('Your  grade is  0.0')
       else:
          grade = math.floor(((percentGrade - 65) * 0.1 + 1) * 10) / 10
          print('Your  grade is ' + str(grade))
       break;
   except ValueError:
      print("Remember your input must be a number between 0 and 100!")
   except:
      print("Something else went wrong")


