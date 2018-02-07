from django.db import models
# Create your models here.

class Eggs(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length=100)
    payEmail = models.EmailField(max_length = 100)
    number = models.CharField(max_length=10)
    eggs = models.CharField(max_length = 3)

    def __str__(self):
        return self.name
