#Password Generator
import random
import re


# GENERATOR SECURITY CODE
def security_code():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&','*', '+','@','Ç','/', '|',]

    nr_letters= 3 
    nr_symbols = 1
    nr_numbers = 2

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return password


def valid_cpf(CPF):

    try:

        CPF = CPF.replace('.','').replace('-','')

        def first_digit(CPF):

            CPF_sum = 0
            counter = 10

            for number in CPF[:9]:
                CPF_sum += int(number) * counter
                counter -= 1

            CPF_first_digit = (CPF_sum * 10) % 11
            CPF_first_digit = CPF_first_digit if CPF_first_digit < 10 else 0
            
            return True if CPF_first_digit == int(CPF[9]) else False

        def second_digit(CPF):

            CPF_sum = 0
            counter = 11

            for number in CPF[:10]:
                CPF_sum += int(number) * counter
                counter -= 1

            CPF_second_digit = (CPF_sum * 10) % 11
            CPF_second_digit = CPF_second_digit if CPF_second_digit < 10 else 0
            
            return True if CPF_second_digit == int(CPF[10]) else False


        return True if first_digit(CPF) and second_digit(CPF) and CPF != (CPF[0] * len(CPF)) else False 

    except:

        return False
    
    
def valid_mail(email):
    
    return re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None


def valid_file(fullname):
    
    divisor = fullname.split('.')
    extension = len(divisor)-1
    
    return divisor[extension]


def remove_char(string, chars_to_remove) -> str:

    result = string
    for i in range(0,len(chars_to_remove)):
        result = result.replace(chars_to_remove[i],'')

    return result