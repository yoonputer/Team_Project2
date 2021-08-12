from django.db import models

# Create your models here.


# class Essay(models.Model):
#     score = models.IntegerField()
#     essayA = models.TextField()
#     essayQ = models.TextField()
#     name = models.CharField(max_length=20)
#
#     def __str__(self):
#         return self.score

class choice(models.Model):
    score = models.DecimalField(max_digits=20,decimal_places=5)
    group = models.TextField()
    group = models.TextField()
    Q1 = models.TextField()
    A1 = models.TextField()
    Q2 = models.TextField()
    A2 = models.TextField()
    Q3 = models.TextField()
    A3 = models.TextField()
    Q4 = models.TextField()
    A4 = models.TextField()
