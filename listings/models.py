from django.contrib.gis.db import models
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.


class Listing(models.Model):
    choices_area = (
        ('Inner London', 'Inner London'),
        ('Outer London', 'Outer London'),
    )
    choices_listing_type = (
        ('House', 'House'),
        ('Appartment', 'Appartment'),
        ('Office', 'Office'),
    )
    choices_property_status = (
        ('Sale', 'Sale'),
        ('Rent', 'Rent'),
    )
    choices_rental_frequency = (
        ('Month', 'Month'),
        ('Week', 'Week'),
        ('Day', 'Day'),
    )

    title = models.CharField(max_length=150)
    seller = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    area = models.CharField(max_length=20, blank=True,
                            null=True, choices=choices_area)
    borough = models.CharField(max_length=50, blank=True, null=True)
    listing_type = models.CharField(
        max_length=20, choices=choices_listing_type)
    property_status = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_property_status)
    price = models.DecimalField(max_digits=50, decimal_places=0)
    rental_frequency = models.CharField(
        max_length=20, blank=True, null=True, choices=choices_rental_frequency)
    rooms = models.IntegerField(blank=True, null=True)
    furnished = models.BooleanField(default=False)
    pool = models.BooleanField(default=False)
    elavator = models.BooleanField(default=False)
    cctv = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    picture1 = models.ImageField(
        blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture2 = models.ImageField(
        blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture3 = models.ImageField(
        blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture4 = models.ImageField(
        blank=True, null=True, upload_to='pictures/%Y/%m/%d/')
    picture5 = models.ImageField(
        blank=True, null=True, upload_to='pictures/%Y/%m/%d/')

    def __str__(self):
        return self.title

class Poi(models.Model):
    choices_type = (
        ('University', 'University'),
        ('Hospital', 'Hospital'),
        ('Stadium', 'Stadium'),
    )

    name = models.CharField(max_length=120, blank=True, null=True)
    type = models.CharField(max_length=50, choices=choices_type)
    location = models.PointField(srid=4326, blank=True, null=True)

    def __str__(self):
        return self.name