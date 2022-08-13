from datetime import datetime
from datetime import date
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import DateField


def no_future(value):
    today = date.today()
    if value > today:
        raise ValidationError('Дата выпуска не может быть дальше сегодняшнего дня.')


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(max_length=50, unique=True)


class Title(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre)
    name = models.CharField(max_length=256)
    date_release = models.PositiveIntegerField(DateField(help_text="Введите дату выхода",
                                                         validators=[no_future]),
                                               blank=True,
                                               null=True)

    def __str__(self):
        return self.name
