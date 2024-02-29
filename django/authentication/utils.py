import random



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



# REMOVE CHARACTER
def remove_char(string, chars_to_remove) -> str:

    result = string
    for i in range(0,len(chars_to_remove)):
        result = result.replace(chars_to_remove[i],'')

    return result



# FILE EXTENSION
def file_extension(filename):

    divisor = filename.split('.')

    return divisor[len(divisor)-1]