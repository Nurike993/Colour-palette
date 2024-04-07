from django.db import models

class Palette(models.Model):
    name = models.CharField(max_length=100, null=True)
    color1 = models.CharField(max_length=100, null=True)
    hex_code1 = models.CharField(max_length=7, null=True)
    color2 = models.CharField(max_length=100, null=True)
    hex_code2 = models.CharField(max_length=7, null=True)
    color3 = models.CharField(max_length=100, null=True)
    hex_code3 = models.CharField(max_length=7, null=True)
    color4 = models.CharField(max_length=100, null=True)
    hex_code4 = models.CharField(max_length=7, null=True)
    