# Whats your Favourite Song ?

# My Favourite Song
song = "Wild at Heart"

# The album the song is from 
album = "Birds of Tokyo"

# Album Release Year
releaseYear = 2010

# Album Release Date
releaseDate = "17th of December 2010" 

# Length of Song (Seconds)
songLengthInSeconds = 240

# The Artist
artist = "Birds of Tokyo"

# Is this an individual or a band
band = True

# Band's Birthplace
placeBandFormed = "Perth, Western Australia"

# From What Music Genre ?
genre = "Hard Rock"

# Just used some template literal like syntax much more readable then concatenation
print(f"My Favourite Song is \"{song}\" it is {songLengthInSeconds} seconds long and its sung by {artist}. It is from their album \"{album}\".")
if band:
    print(f"They are a Band that released their album in the year {releaseYear} on the {releaseDate}")
print(f"They come from {placeBandFormed} and the band is under the Genre \"{genre}\"")