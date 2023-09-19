from django.db import models
from register.models import RegisterModel
# Create your models here.
class ActivateUser(models.Model):

    # Fields
    token = models.CharField("token", max_length=50, unique=True)
    # todo_details = models.ForeignKey("TodoList", on_delete=models.SET_NULL, null=True)
    user_details = models.OneToOneField(RegisterModel, on_delete=models.CASCADE, null=True)

    # class Meta:
    #     verbose_name = _("Login")
    #     verbose_name_plural = _("Logins")

    def __str__(self):
        return self.user_details.name

    def get_absolute_url(self):
        return reverse("login-details")
