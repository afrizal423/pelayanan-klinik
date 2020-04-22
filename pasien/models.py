from django.db import models

# Create your models here.
class Pasien(models.Model):
    norm = models.CharField(max_length=25, unique=True)
    namapasien = models.CharField(max_length=200)
    alamat = models.TextField(blank = True)
    ttl = models.DateField()
    notelp = models.CharField(max_length=15)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.namapasien