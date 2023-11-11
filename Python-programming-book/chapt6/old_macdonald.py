# old_macdonald.py
# A script to print the lyrics of the song "Old MacDonald."
# Prints the lyrics for five different animals

def firstAndLastVerse():
    return ("Old MacDonald had a farm, Ei-igh, Ee-igh, Oh")

def secondVerse(animal):
    return(f"And on that farm he had a {animal}, Ee-igh, Ee-igh, Oh")

def thirdAndForthVerse(sound):
    return(f"With a {sound}, {sound} here and a {sound}, {sound} there.\nHere a {sound}, there a {sound}, everywhere a {sound}, {sound}")

def verseFor(animal, sound):
    lyrics = firstAndLastVerse() +"\n" + secondVerse(animal)+"\n" + thirdAndForthVerse(sound)+"\n" + firstAndLastVerse() +"\n"
    return lyrics


def main():
    for animals, sound in [("cow", "moo"), ("chicken", "cloock"), ("pig", "oink"), ("sheep", "baa"), ("lama","spit")]:
        print(verseFor(animals, sound))



main()
