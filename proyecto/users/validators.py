from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

def threeLetters(password):
    letters = 0
    for char in password:
        if char.isalpha():
            letters += 1
    return letters >= 3

class seguridad():

    def validate(self, password, user=None):
        return None

    def get_help_text(self):
        return ""