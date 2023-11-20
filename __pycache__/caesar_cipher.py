#Alexa Pollard (21075914)

def caesar_cipher(answer,movement):
    'This function moves the letters of a word/phrase a certain number of times ahead in the alphabet'
    if type(answer)!=str or type(movement)!=int:
        print("Invalid input")
        return None
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    answer=list(answer)
    list1=[]

    for i in answer:
        if i==" ":
            list1.append(" ")
        else:
            try:
                index_first_letter=alphabet.index(i)
                index_new_letter=index_first_letter+movement
                if index_new_letter>25:
                    new_movement=movement-(25-index_first_letter)
                    index_new_letter=-1+new_movement
                new_letter=alphabet[index_new_letter]
                list1.append(new_letter)
            except:
                print("Invalid input")
                return None
    new_word=''.join(map(str,list1))
    print(new_word)

caesar_cipher('pendar',1)

    