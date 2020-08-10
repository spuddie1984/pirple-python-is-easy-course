"""
Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
"""

def equalityChecker(param1,param2,param3):
    if param1 == param2:
        return True
    elif param2 == param3:
        return True
    else:
        return False

# modify the numbers below to test
# print(equalityChecker(2,1,1))# True

# lets do a few tests anyway
# print(equalityChecker("test","tested","testing"))# False
#print(equalityChecker("test","test","TEST"))# True
#print(equalityChecker(2,3,4))# False


"""
Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function:
6,5,"5"
You should modify it so that it returns true instead of false.
"""
# Compare Integers to integer like strings 2 ways:

# 1
def equalityIntChecker1(input1,input2,input3):
    # assign function arguements(converted to integers) to new locally scoped variables
    # if an non-integer string is passed then it will throw an error
    # maybe good for the error part of this course
    param1,param2,param3 = int(input1),int(input2),int(input3)
    if param1 == param2:
        return True
    elif param2 == param3:
        return True
    elif param1 == param3:
        return True
    else:
        return False

# print(equalityIntChecker1(1,"2",2))# True

# 2
def equalityIntChecker2(param1,param2,param3):
    if param1 == param2:
        return True
    elif param2 == param3:
        return True
    elif param1 == param3:
        return True
    else:
        return False

# convert any integer like strings to integers during function call
# print(equalityIntChecker2(int(1),int("2"),int(2)))# True
print(equalityIntChecker2(int("1"),int("2"),int("1")))# True 
