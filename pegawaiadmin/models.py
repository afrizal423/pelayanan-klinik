from django.db import models
from pasien.models import Pasien

# Create your models here.

class Pendaftaran(models.Model):
    norm = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    gejalaawal = models.CharField(max_length=200)
    tujuanpoli = models.CharField(max_length=50)
    tglantrian = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.norm

class Antrian(models.Model):
    STATUSNYA_CHOICES = (
        ('selesai', 'Selesai'),
        ('proses', 'Proses'),
        ('belum', 'Belum'),
    )
    idpendaftaran = models.OneToOneField(Pendaftaran, on_delete=models.CASCADE)
    noantrian = models.IntegerField(blank=False, null=False)
    statusdokter = models.CharField(max_length=10, blank = True, null = True, choices=STATUSNYA_CHOICES)
    statusapoteker = models.CharField(max_length=10, blank = True, null = True, choices=STATUSNYA_CHOICES)
    # statusdokter = models.CharField(max_length=10, blank = True, null = True, choices=STATUSNYA_CHOICES)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return "{}. {}".format(self.idpendaftaran, self.noantrian)
