from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone

TELEFON_REGEX = RegexValidator(r'^[+]\d{3}( \d{3}){3}$', 'Nesprávně zadané telefonní číslo')


class Speaker(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno mluvícího", help_text="Zadejte jméno mluvčiho",
                             error_messages={'blank': 'Jméno musí být vyplněno'}, blank=False)
    prijmeni = models.CharField(max_length=50, verbose_name="Příjmeni mluvícího", help_text="Zadejte příjmení mluvčiho",
                                error_messages={'blank': 'Příjmení musí být vyplněno'}, blank=False)
    narozeni = models.DateField(verbose_name='Datum narození', help_text='Zadejte datum narození', blank=False)
    telefon = models.CharField(max_length=16, verbose_name='Telefon klienta',
                               help_text='Zadejte telefon v podobě: +420 777 777 777', blank=True,
                               validators=[TELEFON_REGEX])
    bydliste = models.CharField(max_length=200, verbose_name='Adresa', help_text='Zadejte adresu mluvčího', blank=False)
    email = models.EmailField(max_length=254, verbose_name='E-mail', help_text='Zadejte e-mailovou adresu mluvčího',
                              validators=[EmailValidator('Neplatný e-mail.')], blank=False)
    foto = models.ImageField(null=True, blank=True, verbose_name='Fotka mluvčího',
                             help_text='Zde můžete vložit fotografii mluvčího', upload_to='speaker/')
    zivotopis = models.TextField(blank=True, verbose_name='Životopis', help_text='Zadejte další životopis mluvčího')

    def clean(self):
        super().clean()
        if self.narozeni > timezone.now().date():
            raise ValidationError('Datum narození nemůže být v budoucnosti.')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Mluvčí'
        verbose_name_plural = 'Mluvčí'

    def __str__(self):
        return f'{self.prijmeni}, {self.jmeno}'


class Conference(models.Model):
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název konference",
                             help_text="Zadejte název konference", error_messages={'blank': 'Název musí být vyplněn'},
                             blank=False)
    lokace = models.CharField(max_length=200, verbose_name="Lokace konference", help_text="Zadejte lokaci konference",
                              error_messages={'blank': 'Lokace musí být vyplněna'}, blank=False)
    datum = models.DateField(verbose_name='Datum konference', help_text='Zadejte datum konference', blank=False)
    logo = models.ImageField(blank=True, upload_to='loga', verbose_name='Logo konference',
                             help_text='Zadejte logo konference')
    description = models.TextField(blank=True, verbose_name="Popis konference", help_text="Zadejte popis konference")
    def clean(self):
        super().clean()
        if self.datum < timezone.now().date():
            raise ValidationError('Datum konference nemůže být v minulosti.')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Konference'
        verbose_name_plural = 'Konference'

    def __str__(self):
        return self.nazev


class Session(models.Model):
    SESSION_TYPE = [
        ("Keynote Přednáška", "Keynote Přednáška"),
        ("Panelová Diskuze", "Panelová Diskuze"),
        ("Workshop", "Workshop"),
        ("Posterové Sezení", "Posterové Sezení"),
        ("Breakout Sezení", "Breakout Sezení"),
        ("Q&A Session", "Q&A Session"),
        ("Roundtable Diskuze", "Roundtable Diskuze"),
        ("Lightning Talks", "Lightning Talks"),
    ]
    nazev = models.CharField(max_length=100, unique=True, verbose_name="Název schůze", help_text="Zadejte název schůze",
                             error_messages={'blank': 'Název musí být vyplněn'}, blank=False)
    cas = models.DateTimeField(verbose_name="Čas schůze", blank=False)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE, verbose_name="Mluvčí", blank=False)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE, verbose_name="Konference", blank=False)
    typ = models.CharField(verbose_name="Typ schůze", default="Workshop", max_length=20, choices=SESSION_TYPE,
                           blank=False)
    description = models.TextField(blank=True, verbose_name="Popis schůze", help_text="Zadejte popis schůze")

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Schůze'
        verbose_name_plural = 'Schůze'

    def __str__(self):
        return self.nazev
