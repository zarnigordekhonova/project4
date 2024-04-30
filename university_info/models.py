from django.db import models

# Create your models here.
class university_info1(models.Model):
    name = models.CharField(max_length=255)
    established_year = models.IntegerField()


    def __str__(self):
        return f'{self.name} {self.established_year}'


class university_info2(models.Model):
    number_majors = models.IntegerField()
    number_students = models.IntegerField()
    number_teachers = models.IntegerField()


    def __str__(self):
        return f'{self.number_majors} {self.number_students}'