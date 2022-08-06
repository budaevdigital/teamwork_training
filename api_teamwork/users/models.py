from pickle import TRUE
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class CustomUser(AbstractUser, PermissionsMixin):

    USER = 'User'
    MODERATOR = 'Moderator'
    ADMIN = 'Admin'

    ROLE_CHOICES = (
        (USER, 'Пользователь'),
        (MODERATOR, 'Модератор'),
        (ADMIN, 'Админ'),
    )
    
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    role = models.CharField(max_length = 20,
                            choices = ROLE_CHOICES,
                            default = "Пользователь", blank=True
                            )
    join_date = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-id"]
