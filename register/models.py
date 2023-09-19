from django.db import models
import datetime

# Create your models here.
class RegisterModel(models.Model):

    # Fields
    # id = models.UUIDField(primary_key=True)
    name = models.CharField("name", max_length=20)
    mobile = models.IntegerField("mobile", unique=True)
    email = models.EmailField("email", max_length=254, unique=True)
    username = models.CharField("username", max_length=15, unique=True, null=True)
    password = models.CharField("password", max_length=20, null=True)
    created_on = models.DateTimeField("created_on", auto_now_add=True, null=True)
    
    class Meta:
        verbose_name = "Register"
        # verbose_name_prural = "Registers"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("register-details")
