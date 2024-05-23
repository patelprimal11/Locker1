from django.db import models


# Create your models here.
class user2(models.Model):
   user_name = models.CharField(max_length=20)
   image=models.FileField(max_length=330,null=True,default=None)
