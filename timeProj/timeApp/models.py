from django.db import models

# Create your models here.

# MODEL FOR TIMECARD
class TimeModel(models.Model):
    teachName = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    hours = models.IntegerField()
    workDate = models.DateField()
    entryDate = models.DateField()
    school = models.CharField(max_length=100)

   # TO GET NAME TO SHOW IN ADMIN SITE
    def __str__(self):
        return f'{self.teachName}'

