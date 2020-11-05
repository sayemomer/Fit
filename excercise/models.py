from django.db import models
from user.models import User

# Create your models here.

class Excercise(models.Model):
    id=models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=200)
    duration = models.FloatField(max_length=20)
    date = models.DateTimeField(("Date Created"), auto_now_add=True)