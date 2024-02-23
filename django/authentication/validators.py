import re



# VALID NAME
def valid_name(name):

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
    

# VALID MAIL
def valid_mail(email):
    
    return re.search(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+', email) != None


# VALID FILE
def valid_file(fullname):
    
    divisor = fullname.split('.')
    extension = len(divisor)-1
    
    return divisor[extension]
