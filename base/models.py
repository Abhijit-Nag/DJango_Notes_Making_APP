from email.policy import default
from operator import truediv
from pyexpat import model
from tkinter.tix import Tree
from turtle import title
import turtle
from venv import create
from xml.etree.ElementInclude import default_loader
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title= models.CharField(max_length=200)
    description=models.TextField(null=True, blank=True)
    complete=models.BooleanField(default=False)
    create=models.DateTimeField(auto_now_add=True)

def _str_(self):
    return self.title

class Meta:
    ordering=['complete']