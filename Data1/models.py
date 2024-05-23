from django.db import models

# Create your models here.
class user1(models.Model):
    mobile_no = models.IntegerField()
    user_name = models.CharField(max_length=20)
    email_id = models.EmailField(max_length=50)
    pin_no = models.IntegerField()


