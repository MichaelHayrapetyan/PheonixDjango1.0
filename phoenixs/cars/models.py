from django.db import models


class Car(models.Model):
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='cars_images/')
    description = models.TextField(null=True, blank=True)
    overclocking = models.FloatField(null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    max_speed = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return f'{self.company} {self.name}'


class Company(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'
