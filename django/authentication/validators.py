import re
from authentication import utils
import datetime



# VALID NAME
def valid_name(name):

    name = name.replace(' ','')

    if len(name) > 2:

        for i in range(len(name)):
            if not name[i].isalpha():
                return False
        return True
    
    return False


# VALID CPF
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
    

# VALID CNPJ
def valid_cnpj(cnpj):
    cnpj = cnpj.replace('.', '').replace('/', '').replace('-', '')

    if len(cnpj) == 14:
        validar = True
        digitos_verificadores = cnpj[13:]
    else:
        validar = False

    cnpj = cnpj[:12]

    try:
        dig_1 = int(cnpj[0]) * 6
        dig_2 = int(cnpj[1]) * 7
        dig_3 = int(cnpj[2]) * 8
        dig_4 = int(cnpj[3]) * 9
        dig_5 = int(cnpj[4]) * 2
        dig_6 = int(cnpj[5]) * 3
        dig_7 = int(cnpj[6]) * 4
        dig_8 = int(cnpj[7]) * 5
        dig_9 = int(cnpj[8]) * 6
        dig_10 = int(cnpj[9]) * 7
        dig_11 = int(cnpj[10]) * 8
        dig_12 = int(cnpj[11]) * 9
    except IndexError:
        return False

    dig_1_ao_12_somados = (dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 +
                           dig_7 + dig_8 + dig_9 + dig_10 + dig_11 + dig_12)

    dig_13 = dig_1_ao_12_somados % 11

    if dig_13 > 9:
        dig_13 = 0

    cnpj += str(dig_13)

    dig_1 = int(cnpj[0]) * 5
    dig_2 = int(cnpj[1]) * 6
    dig_3 = int(cnpj[2]) * 7
    dig_4 = int(cnpj[3]) * 8
    dig_5 = int(cnpj[4]) * 9
    dig_6 = int(cnpj[5]) * 2
    dig_7 = int(cnpj[6]) * 3
    dig_8 = int(cnpj[7]) * 4
    dig_9 = int(cnpj[8]) * 5
    dig_10 = int(cnpj[9]) * 6
    dig_11 = int(cnpj[10]) * 7
    dig_12 = int(cnpj[11]) * 8
    dig_13 = int(cnpj[12]) * 9

    dig_1_ao_13_somados = (dig_1 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 +
                           dig_7 + dig_8 + dig_9 + dig_10 + dig_11 + dig_12 + dig_13)

    dig_14 = dig_1_ao_13_somados % 11

    if dig_14 > 9:
        dig_14 = 0

    cnpj_validado = cnpj + str(dig_14)

    cnpj = (cnpj_validado[0:2] + '.' + cnpj_validado[2:5] + '.' +
            cnpj_validado[5:8] + '/' + cnpj_validado[8:12] + '-' + cnpj_validado[12:])

    if validar:
        if digitos_verificadores == cnpj_validado[13:]:
            return True
        else:
            return False
    else:
        return False


# VALID MAIL
def valid_mail(email):
    
    return re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None


# VALID PHONE
def valid_phone(phone):

    phone = utils.remove_char(phone,'() -')

    if len(phone) >= 10:
        for i in range(len(phone)):
            if not phone[i].isnumeric():
                return False
        return True
    
    return False


# VALID FILE
def valid_file(fullname):
    
    divisor = fullname.split('.')
    extension = len(divisor)-1
    
    return divisor[extension]


# VALID DATE
def valid_date(date):

    date_split = str(date).split('-')

    if datetime.date(year=1900, month=1, day=1) < datetime.date(year=int(date_split[0]), month=int(date_split[1]), day=int(date_split[2])) <= datetime.date.today():
        return True

    return False