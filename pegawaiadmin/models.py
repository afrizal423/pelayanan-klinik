from django.db import models
from pasien.models import Pasien

# Create your models here.

class Pendaftaran(models.Model):
    POLI_CHOICES = (
        ('Poli Umum', 'Poli Umum'),
        ('Poli Gigi', 'Poli Gigi'),
    )
    norm = models.ForeignKey(Pasien, on_delete=models.CASCADE)
    gejalaawal = models.TextField()
    tujuanpoli = models.CharField(max_length=20, blank = True, null = True, choices=POLI_CHOICES)
    tglantrian = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.norm.namapasien

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
    is_dokterumum = models.BooleanField(default=False)
    is_doktergigi = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return "{}. {}".format(self.idpendaftaran, self.noantrian)

class Pembayaran(models.Model):
    STATUSNYA_CHOICES = (
        ('selesai', 'Selesai'),
        ('belum', 'Belum'),
    )
    idpendaftaran = models.OneToOneField(Pendaftaran, on_delete=models.CASCADE)
    total_harga = models.BigIntegerField(blank = True, null = True,)
    uang_dibayarkan = models.BigIntegerField(blank = True, null = True,)
    statusbayar = models.CharField(max_length=10, blank = True, null = True, choices=STATUSNYA_CHOICES)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.idpendaftaran.norm.namapasien

class BiayaPemeriksaan(models.Model):
    biaya_pemeriksaan = models.BigIntegerField(blank = True, null = True,)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return "{}".format(self.biaya_pemeriksaan)