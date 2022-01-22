from django.db import models

# Create your models here.

class PrimaryPosition(mdoels.Model):
    position_code = models.CharField(max_legth=16)
    position_name = models.CharField(max_length=32)
    position_type = models.CharField(max_length=32)
    position_abbrev = models.CharField(max_length=16)


class Player(models.Model):
    id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    primary_number = models.CharField(max_length=2)
    birth_date = 
    birth_city = 
    birth_state = 
    birth_country = 
    nationality = 
    height = 
    weight = models.
    active = models.BooleanField(default=False)
    rookie = models.BooleanField(default=False)
    shoot_catches = models.CharField(max_length=32)
    roster_status = models.BooleanField(default=False)
    primary_position = models.ForeignKey(PrimaryPosition, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_height_cm(self):
        height = self.height
        height_list = height.strip('\"').replace(' ','').split("'")
        feet_cm = float(height_list[0]) * 30.48
        inch_cm = float(height_list[2]) * 2.54
        return feet_cm + inch_cm

    @property
    def get_weight_grams(self):
        weight = self.weight