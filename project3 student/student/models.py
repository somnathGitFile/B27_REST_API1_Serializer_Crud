from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    sname = models.CharField(max_length=100)
    smail = models.EmailField()
    sadd = models.CharField(max_length=200)

    def __str__(self):
        return self.sname