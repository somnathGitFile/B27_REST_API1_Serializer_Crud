from django.db import models

# Create your models here.
class Book(models.Model):
    bid = models.IntegerField()
    bname = models.CharField(max_length=50)
    author = models.CharField(max_length=200)
    bqty = models.IntegerField()

    def __str__(self):
        return self.bname