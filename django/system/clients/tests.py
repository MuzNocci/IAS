from django.test import TestCase

# FILE EXTENSION
def file_extension(filename):


    divisor = filename.split('.')


    return divisor[len(divisor)-1]

# VALID TYPE
def valid_type(filename:str, types:list):

    
    extension = file_extension(filename)

    for type in types:
        if type == extension:
            return True
        

    return False


# Create your tests here.
photo = 'fdasfasfasdfasdfsad.jpg'

# VALID DATE
print(valid_type(photo, ['jpg','png','gif','svg','jpeg']))