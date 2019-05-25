from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    reg_date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name
    
class Caso(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/')
    upload_to = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    