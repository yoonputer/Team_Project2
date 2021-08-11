from django.db import models

# Create your models here.
class Essay(models.Model):
    score = models.IntegerField()
    essayA = models.CharField(max_length=1000)
    essayQ = models.CharField(max_length=1000)
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.score


