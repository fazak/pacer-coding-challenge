from django.db import models
from django.contrib.auth.models import User

class Score(models.Model):
    input = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "score"