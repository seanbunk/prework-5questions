# # Question 1
# # Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# # The first line of the code has been defined as below.

def hello_name(user_name):
    """Make a fuction to print hello_USERNAME!"""
    user_name = input('Enter USERNAME:')
    print("Hello " + user_name.upper() + "!")
    

hello_name(user_name='')

# # Question 2
# # Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

for first_odds in range (1,101,2):
    print(first_odds)

# #Question 3
# # Please write a Python function, max_num_in_list to return the max number of a given list. 
# # The first line of the code has been defined as below.

def max_num_in_list(a_list):
    max_number= a_list[0]
    for i in a_list:
        if i > max_number:
            max_number = i
    return max_number

print(max_num_in_list(range(1,101)))

# #Question 4
# #Write a function to return if the given year is a leap year. 
# # A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# # The return should be boolean Type (true/false).

def is_leap_year(a_year):
    leap = False

    if (a_year%400 == 0) and (a_year%100 == 0) :
        leap = True
    elif (a_year%4 == 0) and (a_year % 100 !=0):
        leap = True
    else:
        pass
    
    return leap

print(is_leap_year(a_year= 2022))


#Question 5
#Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) 
    
a_list= [3,4,5,1,2]
print(is_consecutive(a_list))








        


