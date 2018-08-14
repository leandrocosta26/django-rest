from django.db import models

class User(models.Model):

    class Meta:

        db_table = 'users'

    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def __str__(self):
        return self.user_name