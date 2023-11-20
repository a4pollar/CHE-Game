#Alexa Pollard (21075914)

def is_phone_number(number):
    'This function takes in a phone number, and tests if it is a Canadian numebr'
    try:
        number=list(number)
        if len(number)==12:
            a=number.pop(3)
            b=number.pop(6)
            x=''.join(map(str,number))
            if x.isdigit() and a=='-' and b=='-':
                return True
            else:
                return False
        else:
            return False
    except:
        print("Invalid Input")
        return None

print('Is 226-895-5426 a Canadian phone number?')
print(is_phone_number('226-895-5426'))

