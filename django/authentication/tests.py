from django.test import TestCase



def valid_type(filename:str, types:list):
    
    divisor = filename.split('.')
    extension = divisor[len(divisor)-1]

    for type in types:
        if type == extension:
            return "True"
        
    return "False"



file = 'afasdfasdfasdf'

print(valid_type(file, ['doc','xml','mp3']))