from django.db import models

# Create your models here.


class student_info1(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.name} {self.surname}'


class student_info2(models.Model):
    university = models.CharField(max_length=255)
    year = models.IntegerField()
    major = models.CharField(max_length=255)


    def __str__(self):
        return f'{self.university} {self.year}'



