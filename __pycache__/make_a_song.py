#Alexa Pollard (21075914)

def make_a_song(verse,chorus,effect,repeat=False):
    'Function takes in a verse, chorus, and effect, and prints it to the user in the form of a song'
    if type(verse)!=str or type(chorus)!=str or type(effect)!=str or type(repeat)!=bool:
        print("Invalid input")
        return None
    count = 2
    if repeat:
        count = 0
    while count<3:
        print(verse)
        print(chorus+'\t'+chorus)
        print(effect)
        count+=1
        
make_a_song('It\'s me','Hello!','ohh ahh')


