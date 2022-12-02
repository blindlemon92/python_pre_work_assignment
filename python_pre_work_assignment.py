# Python Prework Assignment
# Jessie Baker - bakerjessie54@yahoo.com

question_one: 
writing a fn to print "hello_USERNAME!"

def hello_name(user_name):
    print(f'"hello_{user_name}!"')

hello_name('USERNAME')

# question_two: 
# write a fn to print odds from 1-100 and returns nothing

def first_odds():
    for i in range(1,101,2):
        print(i)

first_odds()

# question_three:
# write a fn to return max() number in given list

def max_num_in_list(a_list):
    return(max(a_list))

print(max_num_in_list(a_list=[56, 1, 64, 15, 92]))

# question_four:
# write a fn to return if a given year is a leap year

def is_leap_year(a_year):
    if a_year % 100 == 0 and a_year % 400 != 0:
        return False
    elif a_year % 4 == 0:
        return True
    else:
        return False

print(is_leap_year(2000))

# question_five:
# write a fn to see if all numbers in list are consecutive


def is_consecutive(a_list):
    a_list.sort()
    test_value = a_list[0]
    for number in a_list:
        while number == test_value:
            test_value += 1
            continue
    if test_value - 1 == a_list[-1]:
        return True
    else:
        return False

print(is_consecutive(a_list=[1,3,5,7,9,11,4,4,4,8,8,8,10,9,6]))
    

    
    

        




