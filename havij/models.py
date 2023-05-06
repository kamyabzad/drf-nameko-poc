from django.db import models


class Havij(models.Model):
    name = models.CharField(max_length=20)
    length = models.PositiveSmallIntegerField(null=False)
