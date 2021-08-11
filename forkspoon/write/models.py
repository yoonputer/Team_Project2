from django.db import models

# Create your models here.
class Essay(models.Model):
    score = models.IntegerField()
    essay = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name