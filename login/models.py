from django.db import models
class Pengguna(models.Model):
    username = models.CharField(max_length=100)
    nim = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=10)

    def __str__(self):
        return self.username
    class Meta:
        db_table = 'pengguna'
