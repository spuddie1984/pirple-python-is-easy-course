"""
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".
"""

# went one step further and created a function that can accept a range of numbers to print
# not just from 1 to 100

def fizzBuzz(start,stop):
    # if modulo of num is equal to 0(no remainder) then print corresponding word else print the num
    # P.s we have added a 1 to the stop value if not the stop value itself wont be printed
    for num in range(start,stop+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
    
# fizzBuzz(1,100)

"""
Extra Credit:
Instead of only printing "fizz", "buzz", and "fizzbuzz", add a fourth print statement: "prime". You should print this whenever you encounter a number that is prime (divisible only by itself and one). As you implement this, don't worry about the efficiency of the algorithm you use to check for primes. It's okay for it to be slow.
"""

# tested for primes at least until 100
def fizzBuzzImproved(maximum):
    for num in range(1,maximum+1):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        elif num != 1:
            if num == 2 or num % 2 != 0:
                if num == 3 or num % 3 != 0:
                    if num == 5 or num % 5 != 0:
                        if num == 7 or num % 7 != 0:
                            print("prime")
                        else:
                            print(num)
        

fizzBuzzImproved(20)