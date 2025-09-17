from django.db import models


# Create your models here.
class memo(models.Model):
    memo_title = models.CharField(max_length=100)
    memo_content = models.TextField(blank=True)
