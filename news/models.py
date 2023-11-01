from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    category = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.catergory}'
    
class News(models.Model):
    
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL , null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    added_on = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.title} added in {self.category}'
    
    