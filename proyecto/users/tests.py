from django.test import TestCase
from django.core.exceptions import ValidationError
from users.validators import seguridad


class seguridadTests(TestCase):

    # Clave valida
    def test01(self):
        print("Case 1: Password OK")
        self.assertEqual(seguridad.validate(self,"11aaBBaa"), None)
        print("Status:  PASSED\n")