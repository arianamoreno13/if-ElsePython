#Write a program named check_month that prompts a user to enter a birth month. 
#If the value entered is greater than 12 or less than 1, display an error message; otherwise, display the valid month

#Ex:

#if the user enter 3,  you display "March"
#if the user enter 5,  you display "May"
#if the user enter 12,  you display "December"
#... do the same with all valid months. i.e. January, February, March, etc...
 

#if the user enters 13 or greater,  you display "ERROR"
#if the user enter 0 or smaller,  you display "ERROR"
 


birthMonth = int(input("Please enter the month you were born."))
if birthMonth == 1:
    month = "January" 
elif birthMonth == 2:
    month = "Febuary"
elif birthMonth == 3:
    month = "March"
elif birthMonth == 4:
    month = "April"
elif birthMonth == 5:
    month = "May"
elif birthMonth == 6:
    month = "June"
elif birthMonth == 7:
    month = "July"
elif birthMonth == 8:
    month = "August"
elif birthMonth == 9:
    month = "September"
elif birthMonth == 10:
    month = "October"
elif birthMonth == 11:
    month = "November"
elif birthMonth == 12:
    month = "December"
else birthMonth
    month = "Invalid month"

 