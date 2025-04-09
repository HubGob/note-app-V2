from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    note = models.TextField()

    def __str__(self):
        return self.title