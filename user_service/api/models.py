from django.db import models

# Create your models here.
class Account(models.Model):
    name    = models.CharField(max_length=30)
    email   = models.EmailField(max_length=70, unique=True)

    def __str__(self):
        return f'{self.email}'
    