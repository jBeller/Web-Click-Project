from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class user_game_status(models.Model):
    score=models.IntegerField()
    double_upgrades_owned=models.IntegerField()
    the_user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
