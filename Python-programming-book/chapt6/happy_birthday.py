# happy_birthday.py

def happy():
    return("Happy birthday to you!\n")

def verseFor(person):
    lyrics = happy()*2 + f"Happy birthday, dear {person}.\n" + happy()
    return lyrics

def main():
    for person in ["Fred", "Lucy", "Elmer"]:
        print(verseFor(person))    

main()