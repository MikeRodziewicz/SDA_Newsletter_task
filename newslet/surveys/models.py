from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=128)
    price = models.FloatField()

    def __str__(self):
        return self.name


class Survey(models.Model):
    question = models.CharField(max_length=128)
    answer = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.question
