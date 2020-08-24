"""
Return to your first homework assignments, when you described your favorite song. 
Refactor that code so all the variables are held as dictionary keys and value. 
Then refactor your print statements so that it's a single loop that passes through each item
in the dictionary and prints out it's key and then it's value.
"""
myFavouriteSong = {
    "song": "Wild at Heart",
    "album": "Birds of Tokyo",
    "releaseYear": 2010,
    "releaseDate": "17th of December 2010",
    "songLengthInSeconds": 240,
    "artist": "Birds of Tokyo",
    "band": "Yes",
    "placeBandFormed": "Perth, Western Australia",
    "genre": "Hard Rock"
}

for item in myFavouriteSong:
    print(f"{item}: {myFavouriteSong[item]}")

"""
Extra Credit:
Create a function that allows someone to guess the value of any key in the dictionary, 
and find out if they were right or wrong. This function should accept two parameters: 
Key and Value. If the key exists in the dictionary and that value is the correct value, 
then the function should return true. In all other cases, it should return false.
"""
def guessTheValue(Key,Value):
    print()