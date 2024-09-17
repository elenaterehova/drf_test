from django.db import models
from django.utils import timezone


class Country(models.Model):
    name = models.CharField(max_length=254, help_text="Название страны")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Manufacturer(models.Model):
    name = models.CharField(max_length=254, help_text="Название производителя.")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Manufacturers"


class Car(models.Model):
    name = models.CharField(max_length=254, help_text="Название автомобиля")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    year_of_release = models.DateField()
    year_of_completion = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Cars"


class Comment(models.Model):
    author_email = models.EmailField(max_length=254)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
    comment = models.TextField()

    def __str__(self):
        return self.author_email

    class Meta:
        verbose_name_plural = "Comments"
