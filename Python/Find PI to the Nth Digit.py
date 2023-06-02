# Find PI to the Nth Digit - 
# Enter a number and have the program generate PI up to that many decimal places. 
# Keep a limit to how far the program will go.

#KNOWN ISSUE:
     # entering 0 will yield '3.0' Which is technically correct but is still printing a decimal point. The program should continue within the while loop as the input is less than 1. Changing error catching methods do not seem to prevent this. Unable to find relevant notes in documentation.


#import libraries
from mpmath import mp

# set variable to control while loop. The loop will determine the number of pi digits.
within_range = False

while within_range == False:
     #asking for the user input and storing it in a variable. the variable is assigned the type of int.
     user_selected_decimal_places = int(input("Enter a number and have the program generate PI up to that many decimal places: ")) +1
     
     if user_selected_decimal_places >= 1 and user_selected_decimal_places < 102:
          mp.dps = user_selected_decimal_places
          print(mp.pi, type(mp.pi))
          within_range = True
     elif user_selected_decimal_places < 1:
          print("Please enter a number between 1 and 100")
     else:
          print("Please enter a number between 1 and 100")
 
  
