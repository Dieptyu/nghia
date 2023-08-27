from django.db import models

class Students(models.Model):
    age = models.IntegerField()
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    grade = models.IntegerField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name
