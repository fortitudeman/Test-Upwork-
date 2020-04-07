from django.db import models
from django_countries.fields import CountryField

class Team(models.Model):
    name = models.CharField(max_length = 100)
    club_status = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name

class Player(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    jersey_number = models.IntegerField()
    country = CountryField(blank_label='(select country)')
    
    def __str__(self):
        return self.first_name
    
    