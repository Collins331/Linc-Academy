from django.db import models

# Create your models here.
class Quize(models.Model):
    question = models.CharField(max_length=400, blank=False, null=False) 
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    author = models.CharField(max_length=200, default='Anonymous')
    date_created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.question