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

    # Clave invalida (sin letra Mayuscula)
    def test03(self):
        print("Case 3: Password Without Uppercase")
        try:
            self.assertRaises(seguridad.validate(self,"a123456789"))
        except ValidationError:
                print("Status:  PASSED\n")

    # Clave invalida (sin letra Minuscula)
    def test04(self):
        print("Case 4: Password Without Lowercase")
        try:
            self.assertRaises(seguridad.validate(self,"A123456789"))
        except ValidationError:
                print("Status:  PASSED\n")

    # Clave invalida (sin tres letras)
    def test05(self):
        print("Case 5: Password With Less than 3 alphabeticCharacters")
        try:
            self.assertRaises(seguridad.validate(self,"Aa123456789"))
        except ValidationError:
                print("Status:  PASSED\n")