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

class lotto_data(models.Model):
    a = models.DecimalField(max_digits=20,decimal_places=20)
    b = models.DecimalField(max_digits=20,decimal_places=20)
    c = models.DecimalField(max_digits=20,decimal_places=20)
    d = models.DecimalField(max_digits=20,decimal_places=20)
    e = models.DecimalField(max_digits=20,decimal_places=20)
    f = models.DecimalField(max_digits=20,decimal_places=20)
    g = models.DecimalField(max_digits=20,decimal_places=20)
    h = models.DecimalField(max_digits=20,decimal_places=20)
    i = models.DecimalField(max_digits=20,decimal_places=20)
    j = models.DecimalField(max_digits=20,decimal_places=20)
    k = models.DecimalField(max_digits=20,decimal_places=20)
    l = models.DecimalField(max_digits=20,decimal_places=20)
    m = models.DecimalField(max_digits=20,decimal_places=20)

