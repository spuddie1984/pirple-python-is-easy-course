# Let's use the variables from the variables Assignment and return each one of them in a function

# My Favourite Song

# song title function
def songTitle():
    return "\"Wild at Heart\""

# Album Title Function
def albumTitle():
    return "\"Birds of Tokyo\""

# Album Release Year Function
def releaseYear():
    return 2010

# Album Release Date Function
def releaseDate():
    return "17th of December 2010" 

# Length of Song Function (In Seconds)
def songLengthInSeconds(): 
    return 240

# The Artist Function
def artist(): 
    return "Birds of Tokyo"

# Check to see if the Artist is a band or just Solo
band = True
# check to see if the band variable is True or False
def isBand(band):
    return band

# Band's Birthplace Function
def placeBandFormed():
    return "Perth, Western Australia"

# From What Music Genre ?
def genre(): 
    return "\"Hard Rock\""

# instead of string concatenation we will use template literal like syntax so that its easier to read
print(f"My Favourite Song is {songTitle()} it is {songLengthInSeconds()} seconds long and its sung by {artist()}.  It is from their album {albumTitle()}")
if isBand(band):
    print(f"They are a Band that released their album in the year {releaseYear()} on the {releaseDate()}.")
    print(f"They come from {placeBandFormed()} and the band is under the Genre {genre()}.")
else:
    print("That isnt a band its an Artist")