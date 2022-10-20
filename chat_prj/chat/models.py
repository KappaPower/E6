from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

class Room(models.Model):
    name = models.CharField(max_length=64, verbose_name='Название')
    user = models.ManyToManyField(User)

class Messages(models.Model):
    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Дата сообщения')
    text = models.TextField()
    room = models.ManyToManyField('Room')
    

