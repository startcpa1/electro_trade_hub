from django.db import models


class Factory(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    email = models.EmailField(verbose_name='Email')





class RetailNetwork(models.Model):
    pass


class IndividualEntrepreneur(models.Model):
    pass
