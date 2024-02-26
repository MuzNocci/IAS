from django.test import TestCase

from authentication.utils import remove_char

# Create your tests here.
def valid_phone(phone):

    phone = remove_char(phone,'() -')

    if len(phone) == 11:
        for i in range(len(phone)):
            if not phone[i].isnumeric():
                return False
        return True
    
    return False


print(valid_phone("(22) 99999-9999"))