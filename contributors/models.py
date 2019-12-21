from django.db import models


# Create your models here.
class Contributor(models.Model):
    commits = models.IntegerField(default=0)
    login = models.CharField(max_length=100, default='Stranger')

    def __str__(self):
        return self.login
