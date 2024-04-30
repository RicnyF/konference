from django.core.exceptions import ValidationError
from django.db import models

"""def birth_number_validate(value):
    if len(value)is not 11:
        raise ValidationError("Rodné číslo musí být 11 číslic")
    if not value.isdigit():
        raise ValidationError("Rodné číslo může obsahovat pouze číslice")
    birth_number = [int(x) for x in value]
    if ((birth_number[2]*10+birth_number[3])>12 or (((birth_number[2]*10+birth_number[3])<50)and(birth_number[2]*10+birth_number[3])>62)):
        raise ValidationError("Špatně zadané RČ")

    weights = [2, 7, 6, 5, 4, 3, 2, 7, 6]
    control = sum(a * b for a, b in zip(birth_number[:9], weights)) % 11
    if control == 10:
        control = 0
    if birth_number[9] != control:
        raise ValidationError('Neplatné rodné číslo.')"""
# Create your models here.
class Speaker(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno mluvícího",help_text="Zadejte jméno mluvčiho",error_messages={'blank': 'Jméno musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name="Příjmeni mluvícího", help_text="Zadejte příjmení mluvčiho",
                             error_messages={'blank': 'Příjmení musí být vyplněno'})
    #rodnecislo = models.IntField(max_length=11, unique=True,help_text="Zadejte rodné číslo bez "/" ",validators=[birth_number_validate])
