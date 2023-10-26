# Exercise 2: Magic-8-Ball (v2)

import random
question = input("I am the Magic 8 Ball. State your question: ")
def magic8Ball():
    randomPhrase = ["Why doesn't anyone ever ask if I have any questions?","Idk, is the mitochondria the powerhouse of the cell?","I shall consult with the counsel...","The signs are pointing... But I'm directionally challenged.","Sorry, I fell asleep mid question.","Let's put it like this, life gave you lemons, but you're also deathly allergic to lemons.","I would say yes, but that would be a lie.","Let's just pretend like you never asked that." ]
    return random.choice(randomPhrase)
    

magic8Ball()