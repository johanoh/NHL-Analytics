from django.db import models

# Create your models here.

class Conference(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    short_name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Division(models.Model):

    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    active = models.BooleanField(default=False)
    conference_id = models.ForeignKey(Conference, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Franchise(models.Model):

    id = models.BigIntegerField(primary_key=True)
    first_year_of_play = models.DateField()
    most_recent_team_id = models.IntegerField()
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Team(models.Model):
    
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=10)
    team_name = models.CharField(max_length=100)
    location_name = models.CharField(max_length=100)
    first_year_of_play = models.DateField()
    venue_name = models.CharField(max_length=100)
    venue_city = models.CharField(max_length=100)
    venue_tz_id = models.CharField(max_length=100)
    venue_tz_offset = models.IntegerField()
    venue_tz_name = models.CharField(max_length=10)
    team_short_name = models.CharField(max_length=100)
    active = models.BooleanField(default=False)
    division_id = models.ForeignKey(Division, on_delete=models.CASCADE)
    conference_id = models.ForeignKey(Conference, on_delete=models.CASCADE)
    franchise_id = models.ForeignKey(Franchise, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




