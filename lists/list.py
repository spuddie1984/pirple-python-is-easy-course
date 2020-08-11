"""
create a function that allows you to add things to the global list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should return False.

add some code below your function that tests it out
it should print the value of myUniqueList to show that it worked.
"""
# Create a global variable called myUniqueList
myUniqueList = []

# Create a global array calle myLeftovers for all of the rejected items
# from the arrayAdder function
myLeftovers = []

def arrayAdder(item):
    # check the myUniqueList array to see if the item exists
    if(myUniqueList.count(item) == 0):
        # add the new unique item to the myUniqueList array
        # print out showing the new item and the updated array
        myUniqueList.append(item)
        print(f"Successfully added \"{item}\" to myUniqueList Array")
        print(f"Your list now looks like this {myUniqueList}")
        return True
    else:
        # any items that are rejected send to the rejectedItems functions
        rejectedItems(item)
        return False

"""
Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

# push any rejected items from the arrayAdder function to the myLeftovers array
def rejectedItems(item):
    myLeftovers.append(item)
    print(f"\"{item}\" is part of the {myLeftovers} rejected item Array")

"""
The arrayAdder function is called after the rejectedItems function is defined (as shown below)
because python doesn't hoist functions to the top of its scope.
python is read from top to bottom.
that is why the arrayAdder function is called after the rejectedItems function
"""

# Add your tests here
arrayAdder("hello")
arrayAdder("world")
arrayAdder("how")
arrayAdder("how")
arrayAdder("are")
arrayAdder("you")
arrayAdder("you")