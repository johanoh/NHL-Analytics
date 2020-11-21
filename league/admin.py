from django.contrib import admin
from .models import (
    Conference,
    Division,
    Team,
    Franchise
)
# Register your models here.

admin.site.register(
    [
        Conference,
        Division,
        Team,
        Franchise
    ]
)