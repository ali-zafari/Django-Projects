from django.db import models

# Create your models here.

class QuestionBank(models.Model):
    question = models.TextField()
    choice1 = models.TextField()
    choice2 = models.TextField()
    choice3 = models.TextField()
    choice4 = models.TextField()
    answer = models.IntegerField()