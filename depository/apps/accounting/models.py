from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import CASCADE, PROTECT

from depository.apps.structure.models import Depository


class Pilgrim(models.Model):
    first_name = models.CharField(max_length=254, null=True, blank=True)
    last_name = models.CharField(max_length=254)
    phone = models.CharField(max_length=50)
    gender = models.IntegerField(default=0)  # male 0 female 1 other 2
    country = models.CharField(max_length=50)
    birthday = models.DateField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    passport_id = models.CharField(max_length=20, null=True, blank=True)
    passport_pic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.country} {self.passport_id}'

    def get_full_name(self):
        if self.first_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.last_name

    def get_four_digit_phone(self):
        if self.phone:
            return self.phone[-4:]
        return ''

    def is_iranian(self):
        if self.country.lower() == 'iran':
            return True
        return False


class User(AbstractUser):
    last_depository = models.ForeignKey(Depository, null=True, blank=True, on_delete=PROTECT)
