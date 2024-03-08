from django.db import models


# Create your models here.
# Blueprint of database
class Form(models.Model):
    firstname = models.CharField(max_length=80)
    lastname = models.CharField(max_length=80)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=80)
    humanorbot = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.firstname}"

