"""
Zeilen, die mit from oder import beginnen, sind Anweisungen, um Sachen
aus anderen Dateien mitzunutzen. Anstatt häufig genutzen Code in jede Datei
einzeln zu kopieren, binden wir ihn ein mit: from... import ... .
"""

from django.db import models
from django.utils import timezone

"""
class ist ein spezielles Schlüsselwort, womit wir angeben, dass wir hier
eine Klasse, eine Vorlage für zukünftige Objekte, definieren wollen.

Post ist der Name unseres Models. Wir können ihm auch einen anderen Namen geben
(aber wir müssen Sonderzeichen und Leerzeichen vermeiden).
Beginne einen Klassennamen immer mit einem Großbuchstaben.

models.Model gibt an, dass das Post-Model ein Django-Model ist,
so weiß Django, dass es in der Datenbank gespeichert werden soll.
"""

class Post(models.Model):  # diese Zeile definiert unser Model
    author = models.ForeignKey('auth.User')  # definiert eine Verlinkung zu einem anderen Model
    title = models.CharField(max_length=200)  # Textfeld mit limitierter Anzahl Zeichen
    text = models.TextField()  # langes Textfeld ohne Limit --> z.B. für Blogpostinhalte
    created_date = models.DateTimeField(  # Feld für eine Uhrzeit & ein Datum
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

# more info: https://docs.djangoproject.com/en/1.8/ref/models/fields/#field-types

def publish(self):  # def zeigt an, dass es sich nachfolgend um Fkt./Methode handelt; publish ist Name der Methode
    self.published_date = timezone.now()
    self.save()

def __str__(self):
    return self.title
