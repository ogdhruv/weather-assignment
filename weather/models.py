from django.db import models
from django.contrib.auth.models import AbstractUser

# authentication model
class CustomUser(AbstractUser):
    """ A custom user model for signup,login and logout funcationaluty

    Args:
        AbstractUser (Class): Full User model, complete with fields, as an abstract class so that you can inherit from it.
    """
    pass


# Weather for specific city model
class City(models.Model):
    """A model for city with its data of weather

    Args:
        models (Class): Model

    Returns:
        None
    """
    city_name = models.CharField(max_length=300,primary_key=True)
    city_country = models.CharField(max_length=20, null=True, blank=True)
    temp = models.FloatField(max_length=10, null=True, blank=True)
    pressure = models.CharField(max_length=10, null=True, blank=True)
    humidity = models.CharField(max_length=10, null=True, blank=True)
    weather = models.CharField(max_length=20, null=True, blank=True)
    icon = models.CharField(max_length=10, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.city_name
