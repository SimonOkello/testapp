from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.
from quizes.models import Quiz

class Result(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quiz = models.ForeignKey(to=Quiz, on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return f"{self.user}=>{self.score}"