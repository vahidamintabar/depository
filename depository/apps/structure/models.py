from django.db import models
from django.utils.translation import ugettext as _

# Create your models here.
from depository.apps.structure.helpers import CodeHelper


class Depository(models.Model):
    name = models.CharField(max_length=100)


class Cabinet(models.Model):
    code = models.CharField(max_length=20)
    depository = models.ForeignKey(Depository, on_delete=models.CASCADE)
    order = models.FloatField(default=1)
    is_asc = models.BooleanField(default=True)


class Row(models.Model):
    code = models.PositiveIntegerField(default=1)
    cabinet = models.ForeignKey(Cabinet, on_delete=models.CASCADE, related_name='rows')


class Cell(models.Model):
    SIZE_SMALL = 0
    SIZE_LARGE = 1
    SIZE_CHOICES = (
        (SIZE_SMALL, _('Small')),
        (SIZE_LARGE, _('Large'))
    )
    code = models.PositiveIntegerField(default=1)
    row = models.ForeignKey(Row, on_delete=models.CASCADE, related_name='cells')
    is_healthy = models.BooleanField(default=True)
    size = models.IntegerField(choices=SIZE_CHOICES, default=SIZE_SMALL)

    def get_code(self):
        return CodeHelper().to_str(self.row.cabinet.code, self.row.code, self.code)


class Constant(models.Model):
    key = models.CharField(max_length=100)
    value = models.TextField()
