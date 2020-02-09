from django.test import TestCase
from django.core.exceptions import ValidationError
from users.validators import seguridad


class seguridadTests(TestCase):

    # Clave valida
    def test01(self):
        print("Case 1: Password OK")
        self.assertEqual(seguridad.validate(self,"11aaBBaa"), None)
        print("Status:  PASSED\n")

    # Clave invalida (tiene caracter alfanumerico)
    def test02(self):
        print("Case 2: Password With Special Character")
        try:
            self.assertRaises(seguridad.validate(self,"12345$TTuu"))
        except ValidationError:
                print("Status:  PASSED\n")