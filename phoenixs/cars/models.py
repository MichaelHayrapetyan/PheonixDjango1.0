from django.db import models
from django.contrib.auth.models import User

ENGINE_TYPE_CHOICES = (
    ('gasoline', 'Gasoline'),
    ('diesel', 'Diesel'),
    ('electric', 'Electric')
)
BODY_TYPE_CHOICES = (
    ('sedan', 'Sedan'),
    ('suv', 'SUV'),
    ('supercar', 'Supercar'),
    ('pickup', 'Pickup'),
    ('hatchback', 'Hatchback'),
    ('convertible', 'Convertible'),
    ('minivan', 'Minivan'),
    ('coupe', 'Coupe'),
    ('sportscar', 'Sports car'),
    ('fastback', 'Fastback')
)


class Car(models.Model):
    exclusive = models.BooleanField(null=True, blank=True)
    company = models.ForeignKey('Company', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='cars_images/')
    description = models.TextField(null=True, blank=True)
    engine_type = models.CharField(max_length=100, choices=ENGINE_TYPE_CHOICES, null=True, blank=True)
    body_type = models.CharField(max_length=100, choices=BODY_TYPE_CHOICES, null=True, blank=True)
    overclocking = models.FloatField(null=True, blank=True)
    horsepower = models.IntegerField(null=True, blank=True)
    max_speed = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.company} {self.name}'


class Company(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    country = models.CharField(max_length=40, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to=f'logo/')

    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
