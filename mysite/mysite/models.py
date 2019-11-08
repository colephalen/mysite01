from django.db import models

# Create your models here.
class View(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title
