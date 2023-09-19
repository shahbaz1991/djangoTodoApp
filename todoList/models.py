from django.db import models
import datetime 

# Create your models here.
class TodoListModal(models.Model):

    # Fields
    # id = models.UUIDField(primary_key=True)
    title = models.CharField("title", max_length=150, help_text='Enter Title')
    description = models.CharField("description", help_text='Enter Description', max_length=300)
    dateTime = models.DateTimeField("dateTime",blank=True, null=True) 
    completed = models.BooleanField("completed", default=False)
    user_FK = models.ForeignKey("register.RegisterModel", verbose_name="user_FK", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['user_FK'] 
        verbose_name = "TodoList"
        # verbose_name_prural = "Registers"

    def __str__(self):
        return self.title