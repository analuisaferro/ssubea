import random
import string
from .models import Tutor, Animal

def generateToken(id):
    token = str(id)
    token += ''.join(random.choices(string.ascii_uppercase + string.digits, k=9))
    return token