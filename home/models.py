from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class HitterReport(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    team = models.IntegerField()
    position = models.CharField(max_length=3)
    bats = models.CharField(max_length=1)
    throws = models.CharField(max_length=1)
    date = models.DateField()
    summary = models.TextField()
class HitterStats(models.Model):
    player = models.ForeignKey(HitterReport, on_delete=models.CASCADE)
    stat = models.CharField(max_length=15)
    value = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(80)])
    futurevalue = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(80)])
    comment = models.TextField(null=True, blank=True)




