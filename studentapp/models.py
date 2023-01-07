from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=21)
    last_name = models.CharField(max_length=21)
    test_score = models.FloatField()

    def __str__(self):
        return self.first_name
