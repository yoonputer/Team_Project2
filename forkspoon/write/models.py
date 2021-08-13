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
    제목 = models.TextField()
    점수 = models.IntegerField()
    질문 = models.TextField()
    답변 = models.TextField()
