#Alexa Pollard (21075914)

def is_phone_number(number):
    'This function takes in a phone number, and tests if it is a Canadian phone number'
    try:
        number_list=list(number)
        if len(number_list)==12:
            possible_dash_1=number_list.pop(3)
            possible_dash_2=number_list.pop(6)
            new_number=''.join(map(str,number_list))
            if new_number.isdigit() and possible_dash_1=='-' and possible_dash_2=='-':
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

