from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=50, default='Empty Header')
    text = models.CharField(max_length=1000, default='Empty Text')
    views = models.IntegerField(default=0)
    publication_date = models.DateField()

    def __str__(self):
        return self.header
