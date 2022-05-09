from django.db import models

# Create your models here.
class Customer(models.Model):
    cid = models.IntegerField()
    cname = models.CharField(max_length=100)
    cmail = models.EmailField()
    cadd = models.CharField(max_length=200)

    def __str__(self):
        return self.cname