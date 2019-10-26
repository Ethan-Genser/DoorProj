from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=15, default="DefaultUserName")
    status =  models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)
